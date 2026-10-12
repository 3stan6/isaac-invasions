import os
import json

base_dir = r"C:\Users\3STAN\.gemini\antigravity\scratch\isaac-upload-labs"
os.makedirs(os.path.join(base_dir, "sheets"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "src"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "build"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "tools"), exist_ok=True)

enemies = [
    {
        "id": "fly",
        "name": "Demonic Red Fly",
        "sprite_icon": "013.00.00.png",
        "health": 25.0,
        "bandwidth_drain": 4.5,
        "heat_per_sec": 1.2,
        "speed": 80.0,
        "reward_bytes": 1024,
        "description": "Corrupted packet payload that spawns hovering pests draining bandwidth from host nodes."
    },
    {
        "id": "spider",
        "name": "Network Cable Spider",
        "sprite_icon": "015.00.00.png",
        "health": 40.0,
        "bandwidth_drain": 8.0,
        "heat_per_sec": 2.5,
        "speed": 110.0,
        "reward_bytes": 2048,
        "description": "Skittering arachnid malware that crawls along data cables, slowing packet transmission."
    },
    {
        "id": "monstro",
        "name": "Monstro Malware Boss",
        "sprite_icon": "020.00.00.png",
        "health": 250.0,
        "bandwidth_drain": 25.0,
        "heat_per_sec": 8.0,
        "speed": 45.0,
        "reward_bytes": 16384,
        "description": "Massive Trojan payload that slams into central router nodes, causing severe overheating and temporary packet lockups."
    }
]

defense_nodes = [
    {
        "id": "tear_turret",
        "name": "Tear Cannon Node",
        "sprite_icon": "005.10.0.png",
        "cost_bytes": 512,
        "range_pixels": 260.0,
        "fire_rate": 2.5,
        "damage_per_shot": 12.0,
        "cooling_rate": 0.0,
        "description": "Constructible network hardware node that fires spectral tears at nearby invading Isaac pests."
    },
    {
        "id": "brimstone_relay",
        "name": "Brimstone Laser Router",
        "sprite_icon": "005.100.00.png",
        "cost_bytes": 2048,
        "range_pixels": 380.0,
        "fire_rate": 0.8,
        "damage_per_shot": 45.0,
        "cooling_rate": -1.0,
        "description": "High-throughput demonic laser array that pierces through multiple infected packets and bosses along cable paths."
    },
    {
        "id": "holy_water_cooler",
        "name": "Holy Water Overclock Cooler",
        "sprite_icon": "005.150.00.png",
        "cost_bytes": 1024,
        "range_pixels": 200.0,
        "fire_rate": 0.0,
        "damage_per_shot": 6.0,
        "cooling_rate": 5.0,
        "description": "Purifying coolant tank that reduces node heat and creates a consecrated firewall aura purging nearby pests."
    }
]

corrupted_packets = [
    {
        "id": "packet_blood_tear",
        "name": "Blood Tear Packet",
        "sprite_icon": "005.10.0.png",
        "spawn_rate_per_sec": 0.2,
        "enemy_spawn_id": "fly",
        "heat_impact": 3.0,
        "description": "Demonic telemetry packet that hatches Red Flies when passing unshielded terminals."
    },
    {
        "id": "packet_spider_crawler",
        "name": "Web Crawler Packet",
        "sprite_icon": "015.00.00.png",
        "spawn_rate_per_sec": 0.12,
        "enemy_spawn_id": "spider",
        "heat_impact": 5.0,
        "description": "Malicious spider packet that infests network cables and slows packet processing."
    },
    {
        "id": "packet_trojan_monstro",
        "name": "Trojan Monstro Payload",
        "sprite_icon": "020.00.00.png",
        "spawn_rate_per_sec": 0.03,
        "enemy_spawn_id": "monstro",
        "heat_impact": 20.0,
        "description": "Heavy infected archive packet that unleashes Monstro onto high-tier nodes."
    }
]

systems = [
    {
        "id": "asset_loader",
        "name": "Isaac Asset Integration Bridge",
        "source_companion": "pc-the-binding-of-isaac-rebirth",
        "asset_dir_relative": "tools/RoomEditor/icons",
        "enabled": True,
        "description": "Dynamically resolves companion game installation path and loads native PNG sprites and audio into Godot at runtime."
    },
    {
        "id": "invasion_engine",
        "name": "Breach & Invasion Simulator",
        "source_companion": "pc-the-binding-of-isaac-rebirth",
        "asset_dir_relative": "",
        "enabled": True,
        "description": "Spawns and updates corrupted packets, roaming pests, health bars, tear projectile physics, and node bandwidth impacts."
    },
    {
        "id": "defense_builder",
        "name": "Hardware Node Construction & Management",
        "source_companion": "pc-upload-labs",
        "asset_dir_relative": "",
        "enabled": True,
        "description": "Renders defense node blueprints on the desktop interface, deducting bytes and managing firing AI."
    },
    {
        "id": "hud_overlay",
        "name": "Isaac Breach HUD & Terminal",
        "source_companion": "pc-upload-labs",
        "asset_dir_relative": "",
        "enabled": True,
        "description": "Displays invasion alert banner, corruption level meter, active defense quickbar, and test automation controls."
    }
]

with open(os.path.join(base_dir, "sheets", "enemies.json"), "w", encoding="utf-8") as f:
    json.dump(enemies, f, indent=2)

with open(os.path.join(base_dir, "sheets", "defense_nodes.json"), "w", encoding="utf-8") as f:
    json.dump(defense_nodes, f, indent=2)

with open(os.path.join(base_dir, "sheets", "corrupted_packets.json"), "w", encoding="utf-8") as f:
    json.dump(corrupted_packets, f, indent=2)

with open(os.path.join(base_dir, "sheets", "systems.json"), "w", encoding="utf-8") as f:
    json.dump(systems, f, indent=2)

print("Created sheets successfully in:", os.path.join(base_dir, "sheets"))
