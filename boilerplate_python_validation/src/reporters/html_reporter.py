"""HTML report generator.

Produces a self-contained HTML report from an EvaluationRun using Jinja2
templates. The report includes pass/fail summary, per-dimension scores,
failure analysis, and trend tracking (when historical data is available).
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..evaluators.base import EvaluationRun


# Self-contained HTML template (no external dependencies)
HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Evaluation Report — {{ suite_name }}</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
         background: #f5f5f5; color: #333; line-height: 1.6; padding: 2rem; }
  .container { max-width: 1000px; margin: 0 auto; }
  h1 { font-size: 1.8rem; margin-bottom: 0.5rem; }
  .meta { color: #666; margin-bottom: 2rem; font-size: 0.9rem; }
  .summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                   gap: 1rem; margin-bottom: 2rem; }
  .card { background: #fff; border-radius: 8px; padding: 1.2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
  .card .label { font-size: 0.8rem; color: #666; text-transform: uppercase; }
  .card .value { font-size: 1.8rem; font-weight: 700; }
  .pass { color: #22c55e; } .fail { color: #ef4444; }
  .warn { color: #f59e0b; } .neutral { color: #333; }
  table { width: 100%; border-collapse: collapse; background: #fff;
          border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1);
          margin-bottom: 2rem; }
  th, td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid #eee; }
  th { background: #f9fafb; font-size: 0.85rem; text-transform: uppercase; color: #666; }
  .score-bar { display: inline-block; height: 8px; border-radius: 4px; background: #e5e7eb; width: 100px; }
  .score-fill { height: 100%; border-radius: 4px; }
  .score-fill.high { background: #22c55e; }
  .score-fill.mid { background: #f59e0b; }
  .score-fill.low { background: #ef4444; }
  .badge { display: inline-block; padding: 0.15rem 0.5rem; border-radius: 4px;
           font-size: 0.75rem; font-weight: 600; }
  .badge-pass { background: #dcfce7; color: #166534; }
  .badge-fail { background: #fee2e2; color: #991b1b; }
  .badge-error { background: #fef3c7; color: #92400e; }
  .failure-detail { background: #fff; border-left: 4px solid #ef4444; padding: 1rem;
                    margin-bottom: 1rem; border-radius: 0 8px 8px 0; }
  .failure-detail h4 { margin-bottom: 0.5rem; }
  .failure-detail p { font-size: 0.9rem; color: #555; }
  h2 { font-size: 1.3rem; margin: 1.5rem 0 1rem; }
  .dimensions { margin-bottom: 2rem; }
</style>
</head>
<body>
<div class="container">
  <h1>Evaluation Report</h1>
  <p class="meta">Suite: <strong>{{ suite_name }}</strong> | Generated: {{ timestamp }} | Run ID: {{ run_id }}</p>

  <div class="summary-grid">
    <div class="card">
      <div class="label">Total Cases</div>
      <div class="value neutral">{{ summary.total_cases }}</div>
    </div>
    <div class="card">
      <div class="label">Passed</div>
      <div class="value pass">{{ summary.passed }}</div>
    </div>
    <div class="card">
      <div class="label">Failed</div>
      <div class="value fail">{{ summary.failed }}</div>
    </div>
    <div class="card">
      <div class="label">Errors</div>
      <div class="value warn">{{ summary.errored }}</div>
    </div>
    <div class="card">
      <div class="label">Avg Score</div>
      <div class="value {% if avg_score_num >= 0.7 %}pass{% elif avg_score_num >= 0.5 %}warn{% else %}fail{% endif %}">
        {{ summary.avg_score_display }}
      </div>
    </div>
    <div class="card">
      <div class="label">Duration</div>
      <div class="value neutral">{{ "%.2f"|format(summary.duration_seconds) }}s</div>
    </div>
  </div>

  {% if dimension_averages %}
  <h2>Dimension Scores</h2>
  <div class="dimensions">
    <table>
      <thead><tr><th>Dimension</th><th>Average Score</th><th></th></tr></thead>
      <tbody>
      {% for dim, score in dimension_averages %}
        <tr>
          <td>{{ dim }}</td>
          <td>{{ "%.3f"|format(score) }}</td>
          <td>
            <span class="score-bar">
              <span class="score-fill {% if score >= 0.7 %}high{% elif score >= 0.5 %}mid{% else %}low{% endif %}"
                    style="width: {{ (score * 100)|int }}%"></span>
            </span>
          </td>
        </tr>
      {% endfor %}
      </tbody>
    </table>
  </div>
  {% endif %}

  <h2>Detailed Results</h2>
  <table>
    <thead>
      <tr><th>Test Case</th><th>Evaluator</th><th>Score</th><th>Status</th><th>Explanation</th></tr>
    </thead>
    <tbody>
    {% for case_name, result in results %}
      <tr>
        <td>{{ case_name }}</td>
        <td>{{ result.evaluator }}</td>
        <td>{{ "%.3f"|format(result.score) if result.score is not none else "—" }}</td>
        <td>
          {% if result.error %}
            <span class="badge badge-error">ERROR</span>
          {% elif result.passed %}
            <span class="badge badge-pass">PASS</span>
          {% else %}
            <span class="badge badge-fail">FAIL</span>
          {% endif %}
        </td>
        <td>{{ result.explanation[:150] }}{% if result.explanation|length > 150 %}…{% endif %}</td>
      </tr>
    {% endfor %}
    </tbody>
  </table>

  {% if failures %}
  <h2>Failure Analysis</h2>
  {% for case_name, result in failures %}
    <div class="failure-detail">
      <h4>{{ case_name }} — {{ result.evaluator }}</h4>
      <p><strong>Score:</strong> {{ "%.3f"|format(result.score) if result.score is not none else "N/A" }}</p>
      <p><strong>Explanation:</strong> {{ result.explanation }}</p>
      {% if result.error %}<p><strong>Error:</strong> {{ result.error }}</p>{% endif %}
      {% if result.dimensions %}
      <p><strong>Dimensions:</strong>
        {% for dim, score in result.dimensions.items() %}
          {{ dim }}={{ "%.3f"|format(score) }}{% if not loop.last %}, {% endif %}
        {% endfor %}
      </p>
      {% endif %}
    </div>
  {% endfor %}
  {% endif %}

</div>
</body>
</html>
"""


class HTMLReporter:
    """Generates self-contained HTML reports from evaluation runs.

    Usage:
        reporter = HTMLReporter(output_dir="./reports")
        reporter.generate(evaluation_run)
    """

    def __init__(self, output_dir: str | Path = "./reports") -> None:
        self.output_dir = Path(output_dir)

    def generate(self, run: EvaluationRun, filename: str | None = None) -> Path:
        """Generate an HTML report from an evaluation run.

        Args:
            run: The completed evaluation run.
            filename: Output filename (default: auto-generated from suite name + timestamp).

        Returns:
            Path to the generated HTML file.
        """
        try:
            from jinja2 import Template
        except ImportError:
            raise ImportError("jinja2 is required for HTML reports: pip install jinja2")

        template = Template(HTML_TEMPLATE)

        # Prepare template context
        avg_score = run.summary.avg_score if run.summary.avg_score is not None else 0.0
        failures = [
            (name, result)
            for name, result in run.results
            if result.passed is False or result.error is not None
        ]
        dimension_averages = sorted(run.summary.dimension_averages.items())

        # Augment summary for template
        summary_data = {
            "total_cases": run.summary.total_cases,
            "passed": run.summary.passed,
            "failed": run.summary.failed,
            "errored": run.summary.errored,
            "avg_score_display": f"{avg_score:.3f}" if run.summary.avg_score is not None else "N/A",
            "duration_seconds": run.summary.duration_seconds,
            "total_tokens": run.summary.total_tokens,
            "total_cost_usd": run.summary.total_cost_usd,
        }

        html = template.render(
            suite_name=run.suite_name,
            run_id=run.id,
            timestamp=run.timestamp.strftime("%Y-%m-%d %H:%M:%S UTC"),
            summary=summary_data,
            avg_score_num=avg_score,
            dimension_averages=dimension_averages,
            results=run.results,
            failures=failures,
        )

        # Write output
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if not filename:
            ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            filename = f"{run.suite_name}_{ts}.html"

        output_path = self.output_dir / filename
        output_path.write_text(html, encoding="utf-8")
        return output_path

    def generate_json(self, run: EvaluationRun, filename: str | None = None) -> Path:
        """Generate a JSON report for programmatic consumption.

        Args:
            run: The completed evaluation run.
            filename: Output filename.

        Returns:
            Path to the generated JSON file.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if not filename:
            ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            filename = f"{run.suite_name}_{ts}.json"

        output_path = self.output_dir / filename
        data = {
            "id": run.id,
            "suite_name": run.suite_name,
            "timestamp": run.timestamp.isoformat(),
            "summary": run.summary.model_dump(),
            "results": [
                {"case_name": name, **result.model_dump()}
                for name, result in run.results
            ],
            "config": run.config,
        }
        output_path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
        return output_path
