from typing import Text
import bpy
from bpy.props import (
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
    EnumProperty,
    BoolProperty,
    IntVectorProperty,
)


class SW_OT_Start(bpy.types.Operator):
    bl_idname = "sw.start"
    bl_label = "Start"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}


class SW_OT_Stop(bpy.types.Operator):
    bl_idname = "sw.stop"
    bl_label = "Stop"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}


class SW_OT_Reset(bpy.types.Operator):
    bl_idname = "sw.reset"
    bl_label = "Reset"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}


class SW_PT_Menu(bpy.types.Panel):
    bl_idname = "SW_Menu"
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
        wm = bpy.context.window_manager

        layout.prop(scene, "color")

        layout.prop(scene, "font_size")

        layout.prop(scene, "margin")

        layout.separator()

        layout.label(text="Align:")
        layout.prop(scene, "align", text="")

        layout.separator()

        layout.label(text="Offset:")
        row = layout.row()
        row.prop(scene, "offset", text="")

        layout.separator()

        layout.label(text="StopWatch:")
        layout.operator(SW_OT_Start.bl_idname, text="Start")
        layout.operator(SW_OT_Stop.bl_idname, text="Stop")
        layout.operator(SW_OT_Reset.bl_idname, text="Reset")

        layout.separator()

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

    scene.margin = IntProperty(
        name="Margin",
        description="Margin",
        default=0,
        min=0,
        max=1000
    )

    scene.align = EnumProperty(
        name="Align",
        items=[
            ('LEFT', "Left", ""),
            ('CENTER', "Center", ""),
            ('RIGHT', "Right", ""),
        ],
        default='LEFT'
    )

    scene.offset = IntVectorProperty(
        name="Offset",
        default=(0, 0),
        size=2,
        subtype='XYZ',
    )


# Erase Propeties
def clear_props():
    scene = bpy.types.Scene
    del scene.color
    del scene.font_size
    del scene.margin
    del scene.align
    del scene.offset
