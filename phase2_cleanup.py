#!/usr/bin/env python3
"""Phase 2: cleanup junk + recrawl missing + deep subdomain crawl (blog, www)."""
import json, re, shutil, pathlib, asyncio, time, hashlib
from urllib.parse import urlparse, urljoin, urldefrag
from datetime import datetime, timezone

DOCS = pathlib.Path("/data/opencode/cloudflare/docs")
STATE = pathlib.Path("/data/opencode/cloudflare/crawl_state.json")

def canon(u, base="https://developers.cloudflare.com"):
    abs_u, _ = urldefrag(urljoin(base, u.strip()))
    p = urlparse(abs_u)
    path = p.path
    if path.endswith("/index.md"): path = path[:-len("/index.md")] + "/"
    elif path.endswith("/index"): path = path[:-len("/index")] + "/"
    elif path in ("/index.md", "/index"): path = "/"
    elif path.endswith(".md"): path = path[:-3] + ("" if path[:-3].endswith("/") else "/")
    c = f"{p.scheme}://{p.netloc}{path}"
    if not c.endswith("/") and "." not in c.rsplit("/", 1)[-1]: c += "/"
    return c

# ---------- 1. cleanup ----------
print("== cleanup ==")
idx = [json.loads(l) for l in open(DOCS / "_index.jsonl")]
txt = open("/tmp/sitemap-0-new.xml").read()
sitemap = set(canon(u) for u in re.findall(r"<loc>([^<]+)</loc>", txt))
print(f"index {len(idx)}, sitemap {len(sitemap)}")

def is_junk(r):
    u = r["url"]
    if u in sitemap: return False, ""
    if "`" in u or "%60" in u or "%5C" in u: return True, "backtick"
    if u.endswith(".json/") or "/schema-output.json" in u or "/streaming-output.json" in u or "/batch-output.json" in u: return True, "json-api"
    if "404" in (r.get("title") or "") and "error-404" not in u and "static-site-generation" not in u: return True, "404-page"
    return False, ""

junk = [(r, reason) for r in idx for reason in [is_junk(r)[1]] if is_junk(r)[0]]
print(f"junk to exclude: {len(junk)}")
excl = DOCS / "_excluded"
(excl / "md").mkdir(parents=True, exist_ok=True)
(excl / "meta").mkdir(parents=True, exist_ok=True)
for r, reason in junk:
    try:
        (DOCS / r["file"]).rename(excl / "md" / (pathlib.Path(r["file"]).name + f"__{hashlib.md5(r['url'].encode()).hexdigest()[:6]}.md"))
    except Exception: pass
    try:
        mrel = str(pathlib.Path(r["file"])).replace(".md", ".json")
        (DOCS / "_meta" / mrel).rename(excl / "meta" / (pathlib.Path(mrel).name + ".excl"))
    except Exception: pass
junk_urls = set(r["url"] for r, _ in junk)
keep = [r for r in idx if r["url"] not in junk_urls]
with open(DOCS / "_index.jsonl", "w") as f:
    for r in sorted(keep, key=lambda x: x["url"]):
        f.write(json.dumps(r) + "\n")
print(f"kept {len(keep)}, moved {len(junk)} to _excluded/")
# update state: drop junk from visited
try:
    st = json.load(open(STATE))
    for u in list(st.get("visited", {}).keys()):
        if u in junk_urls: del st["visited"][u]
    json.dump(st, open(STATE, "w"), indent=2)
    print(f"state cleaned: visited {len(st.get('visited',{}))}")
except Exception as e: print("state clean err", e)
open(excl / "reasons.json", "w").write(json.dumps([{"url": r["url"], "file": r["file"], "reason": reason} for r, reason in junk], indent=2))
