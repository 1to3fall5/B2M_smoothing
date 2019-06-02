import bpy

class LightRotate(bpy.types.Operator):

    bl_description = "Align along X axis"
    bl_idname = "object.lightrotate_operator"
    bl_label = "Select"

    
    
    def execute(self, context):
        bpy.data.screens["Shading"].shading.studiolight_rotate_z = 0.127409
        return {'FINISHED'}