import os
import sys
import hashlib
import json
import urllib.request

sys.path.append(r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\tools")
from melty_cli import call_tool, TOKEN

mod_id = "5c126ea1-0f46-4f82-bc08-c6a661a01bf5"
release_zip = r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\build\IsaacInvasions-Release.zip"
file_name = "IsaacInvasions-Release.zip"

with open(release_zip, "rb") as f:
    zip_bytes = f.read()

size = len(zip_bytes)
sha256 = hashlib.sha256(zip_bytes).hexdigest()

print(f"Uploading {file_name} ({size} bytes, sha256: {sha256})...")

start_res = call_tool("start_upload", {
    "fileName": file_name,
    "size": size,
    "sha256": sha256,
    "modId": mod_id
})

print("start_upload response:")
print(json.dumps(start_res, indent=2))

structured = start_res.get("result", {}).get("structuredContent", {})
upload_id = structured.get("uploadId")
upload_url = structured.get("url")
upload_headers = structured.get("headers", {})

req = urllib.request.Request(
    upload_url,
    data=zip_bytes,
    headers=upload_headers,
    method="PUT"
)
with urllib.request.urlopen(req) as resp:
    print("PUT response status:", resp.status)

finish_res = call_tool("finish_upload", {
    "uploadId": upload_id
})
print("finish_upload response:")
print(json.dumps(finish_res, indent=2))

recipe = {
    "schemaVersion": 1,
    "mode": "installed",
    "games": [
        {
            "slug": "custom-upload-labs",
            "role": "primary"
        },
        {
            "slug": "custom-the-binding-of-isaac-rebirth",
            "role": "companion"
        }
    ],
    "components": [
        {
            "id": "main",
            "fileName": file_name,
            "label": "IsaacInvasions-Release",
            "kind": "main",
            "required": True
        }
    ],
    "requirements": [],
    "mappings": [
        {
            "component": "main",
            "from": "Stan-IsaacInvasions.zip",
            "to": "{game}/mods/Stan-IsaacInvasions.zip"
        },
        {
            "component": "main",
            "from": "README.txt",
            "to": "{game}/mods/README-IsaacInvasions.txt"
        }
    ],
    "launch": {
        "kind": "game",
        "env": {
            "ISAAC_GAME_DIR": "{game:custom-the-binding-of-isaac-rebirth}"
        }
    },
    "test": {
        "args": ["--verbose"],
        "checks": ["breach-simulated", "assets-loaded", "turret-operational"],
        "minutes": 2
    }
}

print("Submitting release 1.0.0...")
submit_res = call_tool("submit_release", {
    "modId": mod_id,
    "version": "1.0.0",
    "recipe": recipe,
    "uploadIds": [upload_id]
})
print("submit_release response:")
print(json.dumps(submit_res, indent=2))
