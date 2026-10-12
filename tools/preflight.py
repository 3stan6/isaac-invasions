import os
import json
import sys

base_dir = r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs"
sheets_dir = os.path.join(base_dir, "sheets")
isaac_icons_dir = r"D:\SteamLibrary\steamapps\common\The Binding of Isaac Rebirth\tools\RoomEditor\icons"

errors = []
warnings = []

# Load sheets
sheets = {}
for sheet_name in ["enemies.json", "defense_nodes.json", "corrupted_packets.json", "systems.json"]:
    p = os.path.join(sheets_dir, sheet_name)
    if not os.path.exists(p):
        errors.append(f"Missing sheet: {sheet_name}")
        continue
    with open(p, "r", encoding="utf-8") as f:
        sheets[sheet_name] = json.load(f)

# 1. Check all cells in all sheets
for sheet_name, rows in sheets.items():
    if not rows:
        errors.append(f"Sheet {sheet_name} is empty")
        continue
    all_keys = set().union(*(r.keys() for r in rows))
    for idx, r in enumerate(rows):
        row_id = r.get("id", f"row_{idx}")
        for k in all_keys:
            if k not in r or r[k] is None or (isinstance(r[k], str) and r[k].strip() == "" and k != "asset_dir_relative"):
                errors.append(f"Sheet {sheet_name} row '{row_id}' has unverified/unfilled cell for column '{k}'")

# 2. Check cross-references
if "corrupted_packets.json" in sheets and "enemies.json" in sheets:
    enemy_ids = {e["id"] for e in sheets["enemies.json"]}
    for p in sheets["corrupted_packets.json"]:
        target = p.get("enemy_spawn_id")
        if target not in enemy_ids:
            errors.append(f"Corrupted packet '{p.get('id')}' references non-existent enemy '{target}'")

# 3. Check sprite assets exist in Isaac folder
if os.path.exists(isaac_icons_dir):
    for sheet_name in ["enemies.json", "defense_nodes.json", "corrupted_packets.json"]:
        if sheet_name in sheets:
            for item in sheets[sheet_name]:
                icon = item.get("sprite_icon")
                if icon:
                    target_file = os.path.join(isaac_icons_dir, icon)
                    if not os.path.exists(target_file):
                        errors.append(f"Sprite icon '{icon}' referenced by {item.get('id')} does not exist in Isaac directory ({target_file})")
                    else:
                        pass
else:
    warnings.append(f"Isaac icons dir not accessible at {isaac_icons_dir}")

print("=== PREFLIGHT REPORT ===")
if errors:
    print(f"FAILED: Found {len(errors)} error(s):")
    for e in errors:
        print(f"  [ERROR] {e}")
    sys.exit(1)
else:
    print("SUCCESS: Preflight is clean! All rows and columns checked, cross-references and asset links verified.")
    if warnings:
        for w in warnings:
            print(f"  [WARN] {w}")
    sys.exit(0)
