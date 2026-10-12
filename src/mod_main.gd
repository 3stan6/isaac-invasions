extends Node

const ManagerScript = preload("res://mods-unpacked/Stan-IsaacInvasions/isaac_manager.gd")
var manager: CanvasLayer

func _init() -> void:
	ModLoaderLog.info("Initializing Stan-IsaacInvasions mashup mod...", "Stan-IsaacInvasions")

func _ready() -> void:
	manager = ManagerScript.new()
	get_tree().root.call_deferred("add_child", manager)
	ModLoaderLog.info("Stan-IsaacInvasions active and attached to root SceneTree.", "Stan-IsaacInvasions")
