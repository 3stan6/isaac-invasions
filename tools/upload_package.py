import os
import sys
import hashlib
import json
import urllib.request

sys.path.append(r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\tools")
from melty_cli import call_tool, TOKEN

mod_id = "5c126ea1-0f46-4f82-bc08-c6a661a01bf5"
zip_path = r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\build\Stan-IsaacInvasions.zip"
zip_name = "Stan-IsaacInvasions.zip"

with open(zip_path, "rb") as f:
    zip_bytes = f.read()

zip_size = len(zip_bytes)
zip_sha256 = hashlib.sha256(zip_bytes).hexdigest()

print(f"Uploading {zip_name} ({zip_size} bytes, sha256: {zip_sha256})...")

start_res = call_tool("start_upload", {
    "fileName": zip_name,
    "size": zip_size,
    "sha256": zip_sha256,
    "modId": mod_id
})

print("start_upload response:")
print(json.dumps(start_res, indent=2))

structured = start_res.get("result", {}).get("structuredContent", {})
upload_id = structured.get("uploadId") or structured.get("id")
upload_url = structured.get("url")
upload_headers = structured.get("headers", {})

if not upload_url and "parts" in structured:
    # Single part url
    upload_url = structured["parts"][0]["url"]

print(f"Upload ID: {upload_id}, Target URL: {upload_url}")

# PUT bytes to upload_url
req = urllib.request.Request(
    upload_url,
    data=zip_bytes,
    headers=upload_headers,
    method="PUT"
)
with urllib.request.urlopen(req) as resp:
    print("PUT response status:", resp.status)

# finish_upload
finish_res = call_tool("finish_upload", {
    "uploadId": upload_id
})
print("finish_upload response:")
print(json.dumps(finish_res, indent=2))
