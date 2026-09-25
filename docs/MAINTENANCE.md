# Maintenance Guide

GitHub AI Radar is designed to be maintainable with minimal manual intervention.

## Normal update cycle

When a meaningful AI signal is found:

1. Verify the repository and current facts from primary sources.
2. Create/update `daily/YYYY/MM/YYYY-MM-DD.md`.
3. Update `data/projects.json` for newly tracked projects.
4. Add a dated snapshot under `data/snapshots/YYYY/MM/` when quantitative observations are available.
5. Update relevant `trends/*.md` only when evidence supports a trend change.
6. Generate/archive the PDF when available.
7. Run:
   ```bash
   python3 scripts/maintain.py
   ```
8. Review `git diff`, commit, and push.

If there is no meaningful signal, **do not create a daily report or empty commit**.

## Safety rules

- Never overwrite an existing daily report silently.
- Preserve historical observations; dynamic metrics belong in snapshots.
- Do not publish unverified repository names or precise metrics.
- Prefer official GitHub repositories and primary project documentation.
- Treat Star/Trending as attention signals, not quality scores.
