# Vault Setup Guide

> One-time setup. Takes about 10 minutes.

---

## Step 1: Install Obsidian

Download from https://obsidian.md and install.

---

## Step 2: Open the Vault

1. Launch Obsidian
2. Click **"Open folder as vault"**
3. Navigate to `C:\WOSRI-Workspace\curriculum`
4. Click **Open**

Obsidian will open with [[HOME]] as your starting point.
The `.obsidian/` config is already included — settings, plugins list, and graph colors are pre-configured.

---

## Step 3: Install Community Plugins

Obsidian will prompt you to enable community plugins. Do this:

1. Go to **Settings → Community plugins**
2. Turn off **Safe mode** (required for community plugins)
3. Click **Browse** and install:
   - **obsidian-git** (by Denis Olehov) — handles Git sync
   - **Dataview** (by Michael Brenan) — powers the session table on HOME

Both plugins are pre-configured via `.obsidian/plugins/*/data.json`.

---

## Step 4: Connect Git to GitHub

### 4a. Create a private GitHub repo

1. Go to https://github.com/new
2. Name it `ai-engineering-curriculum` (or whatever you prefer)
3. Set it to **Private**
4. **Do NOT** initialize with README (the vault already has content)
5. Copy the repo URL (e.g. `https://github.com/YOUR_USERNAME/ai-engineering-curriculum.git`)

### 4b. Connect the local vault to GitHub

Open a terminal in `C:\WOSRI-Workspace\curriculum\` and run:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/ai-engineering-curriculum.git
git branch -M main
git commit -m "initial vault: 30-day AI engineering curriculum"
git push -u origin main
```

### 4c. Verify in Obsidian

After pushing, in Obsidian:
- Press `Ctrl+P` → type `git` → run **"Obsidian Git: Open source control view"**
- You should see "Nothing to commit" — vault is synced

---

## Step 5: Configure Auto-Sync (optional but recommended)

The obsidian-git plugin is already configured to:
- **Auto-commit** 10 minutes after any file change
- **Auto-pull** every 10 minutes
- **Pull before push** (prevents conflicts)

To verify: **Settings → Community plugins → obsidian-git → Options**
Check that "Auto backup interval" = 10 and "Auto pull interval" = 10.

---

## Step 6: Set HOME as your startup file

1. **Settings → Files & Links**
2. Set **"Default new note location"** → `daily_notes`
3. **Settings → Core plugins → Templates** → confirm template folder = `templates`

To open HOME on every launch:
1. Open `HOME.md`
2. **Right-click the tab → Pin**

---

## Daily Workflow

| Action | Shortcut |
|--------|----------|
| Open HOME | `Ctrl+O` → type `HOME` |
| New daily note | `Ctrl+Shift+D` (Daily Notes plugin) |
| Search all notes | `Ctrl+Shift+F` |
| Open graph view | `Ctrl+G` |
| Manual git commit+push | `Ctrl+P` → `git push` |
| Switch between files | `Ctrl+E` (toggle edit/preview) |

---

## Using the Vault Day-to-Day

1. **Start of session:** Open [[HOME]] → check your current day → update "Today's Session" block
2. **During session:** `Ctrl+Shift+D` to create a daily note from the template → fill it in as you go
3. **Check off progress:** Open [[PROGRESS]] → tick completed items
4. **End of session:** Obsidian-git auto-commits. Or manual: `Ctrl+P → Git: Commit all changes`

---

## Sync to a Second Device (future)

When you add another Windows machine:
1. Install Obsidian
2. Clone the repo: `git clone https://github.com/YOUR_USERNAME/ai-engineering-curriculum.git`
3. Open the cloned folder as an Obsidian vault
4. Install the same community plugins (obsidian-git, Dataview)
5. obsidian-git will pull changes automatically on startup

---

## Troubleshooting

**Git push fails (authentication):**
GitHub no longer accepts passwords. Use a Personal Access Token (PAT):
1. GitHub → Settings → Developer settings → Personal access tokens → Generate new token
2. Check `repo` scope
3. Use the token as your password when git prompts

Or set up SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

**obsidian-git says "no git repo found":**
Make sure you opened the vault at `C:\WOSRI-Workspace\curriculum\` (where `.git/` lives), not a parent folder.

**Dataview table on HOME is empty:**
This is expected until you create daily notes with the template. The `daily_notes/` folder is pre-created.
