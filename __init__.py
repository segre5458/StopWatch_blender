import bpy
from . import ui

bl_info = {
    "name": "SimpleStopwatch",
    "author": "segre",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "3D View > Sidebar > SimpleStopwatch",
    "warning": "warning",
    "support": "TESTING",
    "wiki_url": "https://github.com/segre5458/StopWatch_blender",
    "doc_url": "https://github.com/segre5458/StopWatch_blender",
    "tracker_url": "https://github.com/segre5458/StopWatch_blender",
    "category": "System",
}


# def menu_fn(self, context):
#     self.layout.separator()
#     self.layout.operator(ui.SW_PT_Menu.bl_idname)


classes = [
    ui.SW_PT_Menu,
    ui.SW_OT_Start,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    ui.init_props()


def unregister():
    ui.clear_props()
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
