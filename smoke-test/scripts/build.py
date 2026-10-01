import json
import os
from datetime import datetime, timezone
from html import escape
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "data.json").read_text())
message = escape(str(data["message"]))
value = escape(str(data["value"]))
built = datetime.now(timezone.utc).isoformat(timespec="seconds")
revision = escape(os.environ.get("GITHUB_SHA", "local preview"))
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="60">
<title>Data refresh smoke test</title>
<style>
body {{ font: 18px system-ui, sans-serif; background: #edf2f7; color: #172b40; margin: 0; padding: 8vh 24px; }}
main {{ max-width: 720px; margin: auto; background: white; padding: 32px; border-radius: 16px; }}
h1 {{ font-size: 32px; }}
.value {{ font-size: 64px; margin: 16px 0; font-weight: 700; }}
dt {{ font-weight: 600; margin-top: 20px; }}
dd {{ margin: 6px 0; overflow-wrap: anywhere; }}
small {{ color: #52657a; }}
</style>
</head>
<body><main>
<small>GITHUB → AZURE · SAMPLE DATA</small>
<h1>{message}</h1>
<p class="value">{value}</p>
<dl><dt>Generated at (UTC)</dt><dd>{built}</dd>
<dt>Source revision</dt><dd>{revision}</dd></dl>
<p>This page reloads every 60 seconds to pick up the latest deployment.</p>
<p><a href="">Refresh now</a></p>
</main></body></html>
'''
(root / "site").mkdir(exist_ok=True)
(root / "site" / "index.html").write_text(page)
print(f"Generated {root / 'site' / 'index.html'}")
