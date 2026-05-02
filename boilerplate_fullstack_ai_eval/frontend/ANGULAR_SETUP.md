# Angular Frontend — AI Evaluation Dashboard

## Setup

```bash
# Prerequisites: Node.js 18+, Angular CLI 17+
npm install -g @angular/cli

# Create the project
ng new eval-dashboard --routing --style=scss --ssr=false
cd eval-dashboard

# Install dependencies
npm install @ngrx/store @ngrx/effects @ngrx/entity @ngrx/store-devtools
npm install ng2-charts chart.js
npm install @angular/material @angular/cdk
```

## Component Architecture

```
src/app/
├── core/
│   ├── services/
│   │   ├── evaluation-api.service.ts    # HTTP client for FastAPI backend
│   │   └── websocket.service.ts         # WebSocket for live progress
│   ├── models/
│   │   └── evaluation.model.ts          # TypeScript interfaces matching backend models
│   └── core.module.ts
│
├── store/                               # NgRx state management
│   ├── evaluation/
│   │   ├── evaluation.actions.ts        # Load, run, compare, delete
│   │   ├── evaluation.reducer.ts        # State shape + reducers
│   │   ├── evaluation.effects.ts        # Side effects (API calls)
│   │   ├── evaluation.selectors.ts      # Memoized selectors
│   │   └── evaluation.state.ts          # Interface definitions
│   └── app.state.ts                     # Root state
│
├── features/
│   ├── dashboard/
│   │   ├── dashboard.component.ts       # Main view: run list, status, quick stats
│   │   ├── dashboard.component.html
│   │   ├── dashboard.component.scss
│   │   ├── run-list/                    # Table of evaluation runs
│   │   │   └── run-list.component.ts
│   │   └── quick-stats/                 # Summary cards (total runs, avg score, etc.)
│   │       └── quick-stats.component.ts
│   │
│   ├── comparison/
│   │   ├── comparison.component.ts      # Side-by-side run comparison
│   │   ├── comparison.component.html
│   │   ├── comparison.component.scss
│   │   ├── diff-table/                  # Dimension-by-dimension diff
│   │   │   └── diff-table.component.ts
│   │   └── regression-list/             # Highlighted regressions
│   │       └── regression-list.component.ts
│   │
│   ├── detail/
│   │   ├── detail.component.ts          # Drill into a single run
│   │   ├── detail.component.html
│   │   ├── detail.component.scss
│   │   ├── result-table/                # Per-case results with expandable rows
│   │   │   └── result-table.component.ts
│   │   └── failure-panel/               # Failure analysis panel
│   │       └── failure-panel.component.ts
│   │
│   └── charts/
│       ├── score-trend/                 # Line chart: scores over time
│       │   └── score-trend.component.ts
│       ├── dimension-radar/             # Radar chart: multi-dimension view
│       │   └── dimension-radar.component.ts
│       └── pass-rate-bar/               # Bar chart: pass/fail/error breakdown
│           └── pass-rate-bar.component.ts
│
├── app.routes.ts                        # Route definitions
└── app.component.ts                     # Shell with nav sidebar
```

## Key TypeScript Interfaces

```typescript
// core/models/evaluation.model.ts

export interface EvaluationRun {
  id: string;
  suite_name: string;
  status: 'pending' | 'running' | 'completed' | 'failed' | 'cancelled';
  created_at: string;
  completed_at: string | null;
  summary: RunSummary;
  config: Record<string, any>;
  error: string | null;
}

export interface RunSummary {
  total_cases: number;
  passed: number;
  failed: number;
  errored: number;
  avg_score: number | null;
  dimension_averages: Record<string, number>;
  total_tokens: number;
  total_cost_usd: number;
  duration_seconds: number;
}

export interface EvaluationResult {
  id: string;
  test_case_name: string;
  evaluator_name: string;
  score: number | null;
  passed: boolean | null;
  explanation: string;
  metrics: EvaluationMetric[];
  error: string | null;
  latency_ms: number;
  tokens_used: number;
  cost_usd: number;
}

export interface EvaluationMetric {
  name: string;
  score: number;
  explanation: string;
}

export interface ComparisonReport {
  run_a_id: string;
  run_b_id: string;
  summary_comparison: Record<string, { run_a: any; run_b: any }>;
  dimension_comparison: Record<string, { run_a: number; run_b: number; delta: number }>;
  regressions: string[];
  improvements: string[];
}
```

## NgRx Store Pattern

This mirrors the learner's existing Angular patterns with NgRx.

### State Shape

```typescript
// store/evaluation/evaluation.state.ts
import { EntityState } from '@ngrx/entity';

export interface EvaluationState extends EntityState<EvaluationRun> {
  selectedRunId: string | null;
  comparisonReport: ComparisonReport | null;
  loading: boolean;
  error: string | null;
  liveProgress: Record<string, { completed: number; total: number }>;
}
```

### Actions

```typescript
// store/evaluation/evaluation.actions.ts
import { createActionGroup, props, emptyProps } from '@ngrx/store';

export const EvaluationActions = createActionGroup({
  source: 'Evaluation',
  events: {
    'Load Runs': emptyProps(),
    'Load Runs Success': props<{ runs: EvaluationRun[] }>(),
    'Load Runs Failure': props<{ error: string }>(),
    'Start Run': props<{ suite: TestSuite; model: string }>(),
    'Start Run Success': props<{ run: EvaluationRun }>(),
    'Select Run': props<{ runId: string }>(),
    'Compare Runs': props<{ runAId: string; runBId: string }>(),
    'Compare Runs Success': props<{ report: ComparisonReport }>(),
    'Update Progress': props<{ runId: string; completed: number; total: number }>(),
    'Delete Run': props<{ runId: string }>(),
  },
});
```

### Effects (API integration)

```typescript
// store/evaluation/evaluation.effects.ts
@Injectable()
export class EvaluationEffects {
  loadRuns$ = createEffect(() =>
    this.actions$.pipe(
      ofType(EvaluationActions.loadRuns),
      switchMap(() =>
        this.api.listRuns().pipe(
          map(runs => EvaluationActions.loadRunsSuccess({ runs })),
          catchError(error => of(EvaluationActions.loadRunsFailure({ error: error.message })))
        )
      )
    )
  );

  startRun$ = createEffect(() =>
    this.actions$.pipe(
      ofType(EvaluationActions.startRun),
      switchMap(({ suite, model }) =>
        this.api.startRun(suite, model).pipe(
          map(run => EvaluationActions.startRunSuccess({ run })),
          tap(({ run }) => this.ws.connect(run.id))  // Start WebSocket for live updates
        )
      )
    )
  );

  constructor(
    private actions$: Actions,
    private api: EvaluationApiService,
    private ws: WebSocketService,
  ) {}
}
```

## Routes

```typescript
// app.routes.ts
export const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'runs/:id', component: DetailComponent },
  { path: 'compare', component: ComparisonComponent },
];
```

## Chart Components

### Score Trend (ng2-charts)

```typescript
// features/charts/score-trend/score-trend.component.ts
@Component({
  selector: 'app-score-trend',
  template: `<canvas baseChart [datasets]="datasets" [labels]="labels"
                     [options]="options" type="line"></canvas>`,
})
export class ScoreTrendComponent {
  @Input() runs: EvaluationRun[] = [];

  get labels(): string[] {
    return this.runs.map(r => new Date(r.created_at).toLocaleDateString());
  }

  get datasets(): ChartDataset<'line'>[] {
    return [{
      data: this.runs.map(r => r.summary.avg_score ?? 0),
      label: 'Average Score',
      borderColor: '#3b82f6',
      tension: 0.3,
    }];
  }

  options: ChartOptions<'line'> = {
    responsive: true,
    scales: { y: { min: 0, max: 1 } },
  };
}
```

### Dimension Radar

```typescript
@Component({
  selector: 'app-dimension-radar',
  template: `<canvas baseChart [datasets]="datasets" [labels]="labels"
                     [options]="options" type="radar"></canvas>`,
})
export class DimensionRadarComponent {
  @Input() dimensions: Record<string, number> = {};

  get labels(): string[] { return Object.keys(this.dimensions); }
  get datasets(): ChartDataset<'radar'>[] {
    return [{ data: Object.values(this.dimensions), label: 'Scores' }];
  }
}
```

## WebSocket Service

```typescript
// core/services/websocket.service.ts
@Injectable({ providedIn: 'root' })
export class WebSocketService {
  private socket: WebSocket | null = null;

  connect(runId: string): Observable<any> {
    return new Observable(observer => {
      this.socket = new WebSocket(`ws://localhost:8000/ws/evaluations/${runId}`);
      this.socket.onmessage = (event) => observer.next(JSON.parse(event.data));
      this.socket.onerror = (error) => observer.error(error);
      this.socket.onclose = () => observer.complete();
    });
  }

  disconnect(): void {
    this.socket?.close();
  }
}
```

## Connecting to the Backend

```typescript
// core/services/evaluation-api.service.ts
@Injectable({ providedIn: 'root' })
export class EvaluationApiService {
  private baseUrl = 'http://localhost:8000/api/evaluations';

  constructor(private http: HttpClient) {}

  listRuns(): Observable<EvaluationRun[]> {
    return this.http.get<EvaluationRun[]>(this.baseUrl);
  }

  getRun(id: string): Observable<EvaluationRun> {
    return this.http.get<EvaluationRun>(`${this.baseUrl}/${id}`);
  }

  startRun(suite: TestSuite, model: string): Observable<EvaluationRun> {
    return this.http.post<EvaluationRun>(`${this.baseUrl}/run`, { suite, model });
  }

  compareRuns(runAId: string, runBId: string): Observable<ComparisonReport> {
    return this.http.post<ComparisonReport>(`${this.baseUrl}/compare`, {
      run_a_id: runAId,
      run_b_id: runBId,
    });
  }

  deleteRun(id: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }
}
```

## Next Steps

1. Generate the Angular project with `ng new`
2. Copy the interfaces from this document into `core/models/`
3. Implement the API service and WebSocket service
4. Set up NgRx store (actions, reducer, effects, selectors)
5. Build the dashboard component first (list runs, show stats)
6. Add the detail view (drill into results)
7. Add the comparison view
8. Add chart components last (they depend on having data to display)
