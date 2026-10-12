import os
import zipfile

build_dir = r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs\build"
mod_zip_path = os.path.join(build_dir, "Stan-IsaacInvasions.zip")
release_zip_path = os.path.join(build_dir, "IsaacInvasions-Release.zip")

readme_text = """Isaac Invasions for Upload Labs
================================
A game mashup of Upload Labs and The Binding of Isaac: Rebirth.
Author: Stan
License: MIT

Corrupted Isaac data packets infiltrate your network lines, spawning demonic pests
that drain bandwidth. Build Tear Cannon Nodes, Brimstone Laser Routers, and
Holy Water Coolers to protect your system.
"""

with zipfile.ZipFile(release_zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(mod_zip_path, "Stan-IsaacInvasions.zip")
    z.writestr("README.txt", readme_text)

print("Created release archive at:", release_zip_path, "size:", os.path.getsize(release_zip_path))
