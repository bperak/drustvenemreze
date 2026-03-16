# Push to GitHub

The repository is initialized and the remote is set. If **commit** fails in Cursor (e.g. "unknown option trailer"), run these commands in a **system terminal** (e.g. Windows Command Prompt or PowerShell outside Cursor):

```bash
cd "d:\Kulturalni_studiji\IstrazivanjeDrustvenihMreza"

# Create the first commit
git add -A
git commit -m "Add course materials: content, code, examples, README, requirements"

# Push to GitHub (use main if your default branch is main)
git branch -M main
git push -u origin main
```

If the repo on GitHub already has a `main` branch with history (e.g. only LICENSE), you may need:

```bash
git pull origin main --allow-unrelated-histories
# resolve any conflicts, then:
git push -u origin main
```

You can delete this file after a successful push, or add `PUSH_INSTRUCTIONS.md` to `.gitignore` if you prefer not to track it.
