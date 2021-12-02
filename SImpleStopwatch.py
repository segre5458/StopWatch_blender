from typing import Text
import bpy

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


class StopWatch(bpy.types.Panel):
    bl_idname = "StopWatch"
    bl_label = "SimpleStopoWatch"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SimpleStopWatch"

    def draw_header(self, context):
        layout = self.layout
        layout.prop(context.window_manager, "enable_screencast_keys", text="")

    def draw(self, context):
        layout = self.layout

        layout.label(text="test")


def get_user_preferences(context):
    if hasattr(context, "user_preferences"):
        return context.user_preferences

    return context.preferences


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(StopWatch.bl_idname)


def register():
    bpy.utils.register_class(StopWatch)


def unregister():
    bpy.utils.unregister_class(StopWatch)


if __name__ == "__main__":
    register()
