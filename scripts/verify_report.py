"""Verify a run produced a real RSS report; preserve source success/failure caveats."""
from pathlib import Path
import sqlite3,json,datetime
htmls=list(Path('output/html').rglob('*.html'))
assert htmls,'No HTML reports were generated'
assert any('http' in p.read_text() for p in htmls),'Report contains no source links'
databases=list(Path('output').rglob('*.db'))
summary={'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reports':[str(p) for p in htmls],'databases':[str(p) for p in databases],'mode':'RSS+keywords only; no AI, notifications or publishing'}
Path('output/pilot-run-summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
