import bpy

bl_info = {
    "name" : "SimpleStopwatch",
    "author" : "segre",
    "version" : (1,0),
    "blender" : (2,92,0),
    "location" : "3D View > Sidebar > SimpleStopwatch",
    "warning" : "warning",
    "support" : "TESTING",
    "wiki_url" : "",
    "doc_url" : "",
    "tracker_url" : "",
    "category" : "System",
}

class StopWatch(bpy.types.Panel):
    bl_idname = "StopWatch"
    bl_label = "SimpleStopoWatch"
    