import bpy
import math

class SelectAngle(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Select by angle"
    bl_idname = "object.angleselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        degrees = bpy.context.scene.angle_select   
        radians = math.radians(degrees)
        bpy.ops.mesh.faces_select_linked_flat(sharpness = radians) 
        return {'FINISHED'} 