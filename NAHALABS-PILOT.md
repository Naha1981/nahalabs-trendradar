# NahaLabs internal RSS pilot

Based on https://github.com/sansan0/TrendRadar commit657094ed6a527441b917e16d9497fc8435ed091d. Original GPL-3.0 LICENSE retained unchanged. Internal research only, no product embedding, no public reports.

CargoIQ freight and NahaLabs opportunity keyword groups;12RSS feeds. Python3.12 and `python -m trendradar` match current upstream. Hotlists, AI analysis/filter/translation, all notifications and remote storage are off. MCP never started; minimal pinned RSS dependencies exclude LiteLLM/MCP. AI import made lazy so RSS-only startup does not load excluded components. No keys or repository secrets.

Only crawler workflow remains. No Pages, Cloudflare, webhook, Docker publication or repository-output commits. Private HTML artifact retained14days; local output retention14days. Fresh runners intentionally do not preserve SQLite state across runs, so this pilot is scheduled snapshots rather than cross-run deduplicated alerts.

Schedule:05:17/11:17/16:17UTC (07:17/13:17/18:17SAST). Six-minute job ceiling. Private GitHub Actions usage is not inherently free: run only with included quota and paid Actions spending disabled. Feed availability can change; partial source failures must be reported rather than called full source coverage.
