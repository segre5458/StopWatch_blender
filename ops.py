import bpy
import bpy.props

import time


def draw_timer(x, y, w, h, color=[1.0, 1.0, 1, 0], line_thickness=1):
    timer = [x, y, w, h]


class SW_OT_StopWatch(bpy.types.Operator):
    bl_name = "sw.sw_stop_watch"
    bl_label = "SimpleStopWatch"
    bl_description = "Display Stop Watch"
    bl_options = {'REGISTER'}

    runnning = False
