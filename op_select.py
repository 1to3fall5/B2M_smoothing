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

class SelectBoundry(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Select by angle"
    bl_idname = "object.boundryselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.region_to_loop() 
        return {'FINISHED'}

class SelectInner(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Select by angle"
    bl_idname = "object.innerselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.loop_to_region()
        return {'FINISHED'}

class SelectLess(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Select by angle"
    bl_idname = "object.shrinkselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.select_less()
        return {'FINISHED'}

class SelectMore(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Select by angle"
    bl_idname = "object.growselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.select_more()
        return {'FINISHED'}

class SelectLoop(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Select by angle"
    bl_idname = "object.loopselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.loop_multi_select(ring=False)
        return {'FINISHED'}

class SelectRing(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Select by angle"
    bl_idname = "object.ringselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.loop_multi_select(ring=True)
        return {'FINISHED'}
        
