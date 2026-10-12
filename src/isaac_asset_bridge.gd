extends RefCounted

const SheetsData = preload("res://mods-unpacked/Stan-IsaacInvasions/sheets_data.gd")

var isaac_root: String = ""
var icons_dir: String = ""
var texture_cache: Dictionary = {}
var is_companion_loaded: bool = false

func _init() -> void:
	resolve_paths()
	preload_icons()

func resolve_paths() -> void:
	var env_path = OS.get_environment("ISAAC_GAME_DIR")
	if env_path != "" and DirAccess.dir_exists_absolute(env_path):
		isaac_root = env_path
	else:
		var candidates = [
			"D:/SteamLibrary/steamapps/common/The Binding of Isaac Rebirth",
			"C:/Program Files (x86)/Steam/steamapps/common/The Binding of Isaac Rebirth",
			"E:/SteamLibrary/steamapps/common/The Binding of Isaac Rebirth"
		]
		for c in candidates:
			if DirAccess.dir_exists_absolute(c):
				isaac_root = c
				break
	
	if isaac_root != "":
		icons_dir = isaac_root.path_join("tools/RoomEditor/icons")
		if DirAccess.dir_exists_absolute(icons_dir):
			is_companion_loaded = true
			ModLoaderLog.info("Isaac Companion connected at: " + isaac_root, "Stan-IsaacInvasions")
		else:
			ModLoaderLog.warning("Isaac install found, but RoomEditor icons missing at: " + icons_dir, "Stan-IsaacInvasions")
	else:
		ModLoaderLog.warning("The Binding of Isaac Rebirth folder not found. Awaiting Melty companion mapping.", "Stan-IsaacInvasions")

func preload_icons() -> void:
	if not is_companion_loaded:
		return
	
	for enemy in SheetsData.ENEMIES:
		get_texture(enemy.sprite_icon)
	for node in SheetsData.DEFENSE_NODES:
		get_texture(node.sprite_icon)

func get_texture(filename: String) -> Texture2D:
	if texture_cache.has(filename):
		return texture_cache[filename]
	
	if is_companion_loaded:
		var file_path = icons_dir.path_join(filename)
		if FileAccess.file_exists(file_path):
			var img = Image.load_from_file(file_path)
			if img != null:
				var tex = ImageTexture.create_from_image(img)
				texture_cache[filename] = tex
				return tex
	
	var fallback_img = Image.create(32, 32, false, Image.FORMAT_RGBA8)
	fallback_img.fill(Color(0.8, 0.2, 0.2, 0.9))
	var fallback_tex = ImageTexture.create_from_image(fallback_img)
	texture_cache[filename] = fallback_tex
	return fallback_tex
