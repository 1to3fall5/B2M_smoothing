import bpy

class Xalign(bpy.types.Operator):

    bl_description = "Align along X axis"
    bl_idname = "object.xalign_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Scale selected to 0 along X axis
        bpy.ops.transform.resize(value=(0, 1, 1))
        return {'FINISHED'}
        
class Yalign(bpy.types.Operator):

    bl_description = "Align along Y axis"
    bl_idname = "object.yalign_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Scale selected to 0 along Y axis
        bpy.ops.transform.resize(value=(1, 0, 1))
        return {'FINISHED'}
    
class Zalign(bpy.types.Operator):

    bl_description = "Align along Z axis"
    bl_idname = "object.zalign_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Scale selected to 0 along Z axis
        bpy.ops.transform.resize(value=(1, 1, 0))
        return {'FINISHED'} 