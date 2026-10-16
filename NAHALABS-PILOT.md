# NahaLabs internal RSS pilot

Based on https://github.com/sansan0/TrendRadar commit657094ed6a527441b917e16d9497fc8435ed091d. Original GPL-3.0 LICENSE retained unchanged. Internal research use, no product embedding. Repository and Actions logs/artifacts are public by owner choice to use standard free public runners. Reports contain public-news sources only. No Pages or hosted report site.

CargoIQ freight and NahaLabs opportunity keyword groups;12RSS feeds. Python3.12 and `python -m trendradar` match current upstream. Hotlists, AI analysis/filter/translation, all notifications and remote storage are off. MCP never started; minimal pinned RSS dependencies exclude LiteLLM/MCP. AI import made lazy so RSS-only startup does not load excluded components. No keys or repository secrets.

Only crawler workflow remains. No Pages, Cloudflare, webhook, Docker publication or repository-output commits. Actions HTML artifact retained14days; local output retention14days. Fresh runners intentionally do not preserve SQLite state across runs, so this pilot is scheduled snapshots rather than cross-run deduplicated alerts.

Schedule:05:17/11:17/16:17UTC (07:17/13:17/18:17SAST). Six-minute job ceiling. Public standard ubuntu-latest runners selected for free Actions compute. Do not switch to paid/larger runners. Feed availability can change; partial source failures must be reported rather than called full source coverage.

Upstream compatibility patch: platforms.enabled=false no longer exits before RSS; hotlist collector explicitly skipped. Preflight exercises the startup gate without any network collection.

Report mode is daily: upstream current mode requires hotlist history and fails when only RSS is enabled. Each fresh-runner snapshot summarizes the fetched RSS items.
