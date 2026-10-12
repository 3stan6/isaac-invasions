import os
import sys
import json
import urllib.request

sys.path.append(r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\tools")
from melty_cli import call_tool, TOKEN

mod_id = "5c126ea1-0f46-4f82-bc08-c6a661a01bf5"
shot_path = r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\build\screenshot.png"
shot_name = "shot-1.png"

with open(shot_path, "rb") as f:
    shot_bytes = f.read()

shot_size = len(shot_bytes)

print(f"Uploading screenshot {shot_name} ({shot_size} bytes)...")

add_res = call_tool("add_screenshot", {
    "modId": mod_id,
    "fileName": shot_name,
    "contentType": "image/png",
    "size": shot_size
})
print("add_screenshot response:")
print(json.dumps(add_res, indent=2))

structured = add_res.get("result", {}).get("structuredContent", {})
upload_id = structured.get("uploadId")
upload_url = structured.get("url")
headers = structured.get("headers", {"content-type": "image/png"})

req = urllib.request.Request(
    upload_url,
    data=shot_bytes,
    headers=headers,
    method="PUT"
)
with urllib.request.urlopen(req) as resp:
    print("PUT response status:", resp.status)

finish_res = call_tool("finish_screenshot", {
    "uploadId": upload_id
})
print("finish_screenshot response:")
print(json.dumps(finish_res, indent=2))
