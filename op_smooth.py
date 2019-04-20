import bpy
import math

class SmoothOperator(bpy.types.Operator):

    bl_description = "Smooth selected faces (Mark boundary edges sharp)"
    bl_idname = "object.smoothing_operator"
    bl_label = "Smooth"
    
    #build a function that marks sharp the bountry edges around selected face''' 
    def execute(self, context):
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 3.14159   
             
        bpy.ops.mesh.faces_shade_smooth()
        bpy.ops.mesh.mark_sharp(clear=True)
        bpy.ops.mesh.region_to_loop()
        bpy.ops.mesh.mark_sharp()
        bpy.ops.mesh.select_mode(type='FACE')    
        return {'FINISHED'}

#custom operator to excute angle smooth function'''
class AngleSmoothOperator(bpy.types.Operator):

    bl_description = "Smooth similar angle faces (Mark edges sharp based on angle)"
    bl_idname = "object.anglesmoothing_operator"
    bl_label = "Smooth by:"

    #build a function that marks sharp the bountry edges around selected face'''
    def execute(self, context):        
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 3.14159   
        
        bpy.ops.mesh.select_all(action='SELECT')   
        bpy.ops.mesh.faces_shade_smooth()
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.mark_sharp(clear=True)
        bpy.ops.mesh.select_all(action='DESELECT')
        degrees = bpy.context.scene.angle_smooth   
        radians = math.radians(degrees)
        bpy.ops.mesh.edges_select_sharp(sharpness = radians)  
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.mark_sharp()     
        return {'FINISHED'}

#custom operator to excute hard function'''   
class HardOperator(bpy.types.Operator):

    bl_description = "Flat selected faces (Mark all edges sharp)"
    bl_idname = "object.hard_operator"
    bl_label = "Harden"
    
    #build alayout.label(text="Big Button:") function that marks sharp all the edges in the selected face'''
    def execute(self, context):        
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 3.14159   
        
        bpy.ops.mesh.mark_sharp()
        bpy.ops.mesh.select_mode(type='FACE')
        return {'FINISHED'}