# Isaac Invasions

> **A genuine game mashup of *Upload Labs* and *The Binding of Isaac: Rebirth*.**

[![Melty](https://img.shields.io/badge/Melty-Play%20in%20One%20Click-purple)](https://melty.gg/m/isaac-invasions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Demonic packets bearing Isaac telemetry infiltrate your network cables in Upload Labs. When they breach network nodes, they spawn Isaac pests (Red Flies, Spiders, and Monstro Malware) that siphon bandwidth and overheat system boards. Build automated **Tear Cannon Nodes**, **Brimstone Laser Routers**, and **Holy Water Coolers** using processed data bytes to defend your network!

---

## Features

- **Genuine Mashup Integration:** Plays directly inside *Upload Labs* (primary host) while dynamically reading real graphics and assets from your local *The Binding of Isaac: Rebirth* installation (companion game).
- **Zero Asset Piracy:** Complies with Melty's mashup standard—no game assets are packaged in the distribution. Assets are resolved at runtime from `{game:custom-the-binding-of-isaac-rebirth}` via the `ISAAC_GAME_DIR` environment variable.
- **Corrupted Packet Mechanics:** 
  - Low-level demonic packet telemetry spawning Red Flies, Spiders, and Monstro Malware.
  - Bandwidth siphon mechanics that degrade node processing speed.
- **Hardware Defense Nodes:**
  - **Tear Cannon Node:** Fires high-velocity tear projectiles at approaching entities.
  - **Brimstone Laser Router:** Sustained high-voltage laser piercing corrupted streams.
  - **Holy Water Cooler:** Cools overheated motherboards and slows enemies in radius.
- **Automated Verification:** Integrated with Godot Mod Loader (GML v6.2.4) and automated Melty test harness.

---

## One-Click Install via Melty

Install and launch directly from Melty:
**[Play on Melty: melty.gg/m/isaac-invasions](https://melty.gg/m/isaac-invasions)**

Melty automatically detects both games on your PC, mounts the mod, passes companion directory paths, and launches the mashup in one click.

---

## Project Structure

```
├── melty.json                 # Melty one-click install recipe & test hooks
├── sheets/                    # Design sheets (Source of Truth)
│   ├── corrupted_packets.json # Packet types, payload sizes, corruption rates
│   ├── defense_nodes.json     # Turret types, costs, fire rates, damage
│   ├── enemies.json           # Monster stats, sprites, behavior
│   └── systems.json           # Engine systems & verification contracts
├── src/                       # Godot Mod Loader scripts
│   ├── manifest.json          # GML mod manifest (v6.2.4)
│   ├── mod_main.gd            # Mod entrypoint & hook initializer
│   ├── isaac_manager.gd       # Invasion engine, HUD, and turret manager
│   ├── isaac_asset_bridge.gd  # Runtime companion asset loader
│   └── sheets_data.gd         # Generated code from design sheets
└── tools/                     # Build, validation, and packaging tools
    ├── preflight.py           # Design sheet validator & cross-reference checker
    ├── build_mod.py           # GML zip packager & code generator
    └── package_release.py     # Melty release bundle builder
```

---

## Building from Source

### Prerequisites
- Python 3.10+
- [Upload Labs](https://store.steampowered.com/app/3606890/Upload_Labs/)
- [The Binding of Isaac: Rebirth](https://store.steampowered.com/app/250900/The_Binding_of_Isaac_Rebirth/)

### Validation & Build
1. Validate sheets and assets:
   ```bash
   python tools/preflight.py
   ```
2. Build the GML mod package:
   ```bash
   python tools/build_mod.py
   ```
3. Package the release archive:
   ```bash
   python tools/package_release.py
   ```

---

## License

This project is licensed under the [MIT License](LICENSE). Open remixing is enabled.
