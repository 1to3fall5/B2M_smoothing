import bpy

class ClearBevel(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Clear all bevel weight"
    bl_idname = "object.clearbevel_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Set selected bevel weight to 0
        bpy.ops.transform.edge_bevelweight(value=0.0) 
        return {'FINISHED'} 
    
class ClearSeam(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Clear all seams"
    bl_idname = "object.clearseam_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Clear seams
        bpy.ops.mesh.mark_seam(clear=True)
        return {'FINISHED'} 

class ClearSharp(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Clear all sharp mark"
    bl_idname = "object.clearsharp_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Clear sharp
        bpy.ops.mesh.mark_sharp(clear=True)
        return {'FINISHED'}