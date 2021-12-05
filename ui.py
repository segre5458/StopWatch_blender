import bpy
from bpy.props import (
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
    EnumProperty,
    BoolProperty,
)


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
        scene = context.scene

        layout.prop(scene, "color")
        layout.prop(scene, "font_size")
        layout.prop(scene, "margin", text="margin")

        layout.separator()

        layout.label(text="Align:")
        layout.prop(scene, "align", text="")

        layout.separator()

        layout.label(text="Offset:")
        row = layout.row()
        row.prop(scene, "offset", text="")


# Initialize Properties
def init_props():
    scene = bpy.types.Scene

    scene.color = FloatVectorProperty(
        name="Color",
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0,
        subtype='COLOR_GAMMA',
        size=3
    )

    scene.font_size = IntProperty(
        name="Font Size",
        default=15,
        min=0,
        max=255
    )

# Erase Propeties


def clear_props():
    scene = bpy.types.Scene
    del scene.color
    del scene.font_size
