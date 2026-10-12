import os
import sys
import zipfile
import json
import hashlib
import urllib.request

sys.path.append(r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\tools")
from melty_cli import call_tool, TOKEN

mod_id = "5c126ea1-0f46-4f82-bc08-c6a661a01bf5"
zip_path = r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\build\Stan-IsaacInvasions.zip"
zip_name = "Stan-IsaacInvasions.zip"

# Read entries from zip
entries = []
files_content = {}
with zipfile.ZipFile(zip_path, "r") as z:
    for info in z.infolist():
        entries.append({
            "path": info.filename,
            "size": info.file_size
        })
        if info.filename.endswith((".json", ".txt", ".md")):
            files_content[info.filename] = z.read(info.filename).decode("utf-8", errors="ignore")

says_text = """Defend your Upload Labs network nodes against The Binding of Isaac dungeon invasions with corrupted packets and hardware defense turrets. Directly integrates authentic assets from your installed copy of The Binding of Isaac: Rebirth."""

print("=== 1. inspect_package ===")
inspect_res = call_tool("inspect_package", {
    "fileName": zip_name,
    "entries": entries,
    "files": files_content,
    "gameSlugs": ["custom-upload-labs", "custom-the-binding-of-isaac-rebirth"],
    "says": says_text
})
print(json.dumps(inspect_res, indent=2))

recipe = {
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
            "id": "isaac-invasions",
            "fileName": zip_name,
            "dest": "{game}/mods/Stan-IsaacInvasions.zip"
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

print("=== 2. validate_recipe ===")
val_res = call_tool("validate_recipe", {
    "recipe": recipe,
    "entries": {
        "isaac-invasions": entries
    }
})
print(json.dumps(val_res, indent=2))

print("=== 3. one_click_check ===")
occ_res = call_tool("one_click_check", {
    "recipe": recipe,
    "entries": {
        "isaac-invasions": entries
    },
    "says": says_text
})
print(json.dumps(occ_res, indent=2))
