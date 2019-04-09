bl_info = {
    "name": "Smoothing",
    "author": "Chen Chen",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Smoothing > Smoothing Setting",
    "description": "Smoothing selected",
}

import bpy
import math

def sharp_select():
    bpy.ops.object.mode_set(mode='OBJECT')  

    for edge in bpy.context.object.data.edges:
        if edge.use_edge_sharp:
            edge.select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE') 
     
#custom operator to excute smooth function'''
class SmoothOperator(bpy.types.Operator):
    """Tooltip"""
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
    """Tooltip"""
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
    """Tooltip"""
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
    
class SharpSelect(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Select marked sharp edges"
    bl_idname = "object.sharpselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        sharp_select()
        return {'FINISHED'} 
    
class SharpBevel(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Set sharp edges' bevel weight to 1 (Use with bevel modifier)"
    bl_idname = "object.sharpbevel_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.select_all(action='DESELECT')         
        sharp_select()
        bpy.ops.transform.edge_bevelweight(value=1.0)       
        return{'FINISHED'}    
    
class SharpSeam(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Make sharp edges to seams"
    bl_idname = "object.sharpseam_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.select_all(action='DESELECT')
        sharp_select()
        bpy.ops.mesh.mark_seam(clear=False)
        return {'FINISHED'} 

class ClearBevel(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Clear all bevel weight"
    bl_idname = "object.clearbevel_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.transform.edge_bevelweight(value=0.0) 
        return {'FINISHED'} 
    
class ClearSeam(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Clear all seams"
    bl_idname = "object.clearseam_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.mark_seam(clear=True)
        return {'FINISHED'} 

class ClearSharp(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Clear all sharp mark"
    bl_idname = "object.clearsharp_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.mesh.mark_sharp(clear=True)
        return {'FINISHED'} 
    
class Xalign(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Align along X axis"
    bl_idname = "object.xalign_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.transform.resize(value=(0, 1, 1))
        return {'FINISHED'}
class Yalign(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Align along Y axis"
    bl_idname = "object.yalign_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.transform.resize(value=(1, 0, 1))
        return {'FINISHED'}
    
class Zalign(bpy.types.Operator):
    """Tooltip"""
    bl_description = "Align along Z axis"
    bl_idname = "object.zalign_operator"
    bl_label = "Select"
    
    def execute(self, context):
        bpy.ops.transform.resize(value=(1, 1, 0))
        return {'FINISHED'}    

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
         
#creates a panel in the 3d view N panel'''   
class SmoothingPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Smoothing Setting"
    bl_idname = "SmoothPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "mesh_edit"
    bl_category = "Smoothing"

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Smooth Setting")       
        col = layout.column(align=True)
        row = col.row(align=True)  
        row.operator("object.anglesmoothing_operator", icon = "LINCURVE", text = "Smooth")   
        row.scale_x = 0.5
        row.prop(context.scene, "angle_smooth")                                  
        col.operator("object.smoothing_operator", icon = "SPHERECURVE", text = "Smooth Selected")
        col.operator("object.hard_operator", icon = "NOCURVE", text = "Harden Selected")  
        
        layout.label(text="Sharp Edges to")
        col = layout.column(align=True)
        col.operator("object.sharpselect_operator", icon = "MESH_CUBE", text = "Selection")
        col.operator("object.sharpbevel_operator", icon = "STYLUS_PRESSURE", text = "Weight 1") 
        col.operator("object.sharpseam_operator", icon = "DRIVER_DISTANCE", text = "Seams")
        
        layout.label(text="Clear")
        row = layout.row(align=True)
        row.operator("object.clearsharp_operator", text = "Sharp")
        row.operator("object.clearbevel_operator", text = "Weight")
        row.operator("object.clearseam_operator", text = "Seams")      
        
        layout.label(text="Align")
        row = layout.row(align=True)
        row.operator("object.xalign_operator", text = "X")
        row.operator("object.yalign_operator", text = "Y")
        row.operator("object.zalign_operator", text = "Z")
                  
        layout.label(text="Select by Angle")
        row = layout.row(align=True)
        row.operator("object.angleselect_operator", icon = "RESTRICT_SELECT_OFF",text = "Select")
        row.scale_x = 0.5
        row.prop(context.scene, "angle_select")
        
        
        
        
def register():
    bpy.utils.register_class(SmoothingPanel)
    bpy.utils.register_class(SmoothOperator)
    bpy.utils.register_class(AngleSmoothOperator)
    bpy.utils.register_class(HardOperator)
    bpy.utils.register_class(SharpSelect)
    bpy.utils.register_class(SharpBevel)
    bpy.utils.register_class(SharpSeam)
    bpy.utils.register_class(ClearBevel)
    bpy.utils.register_class(ClearSeam)
    bpy.utils.register_class(ClearSharp)
    bpy.utils.register_class(Xalign)
    bpy.utils.register_class(Yalign)
    bpy.utils.register_class(Zalign)
    bpy.utils.register_class(SelectAngle)
    bpy.types.Scene.angle_smooth = bpy.props.FloatProperty(
        name = "",
        description = "Set Smoothing Angle",
        default = 30.0,
        min = 0.0,
        max = 180.0
    )
    bpy.types.Scene.angle_select = bpy.props.FloatProperty(
        name = "",
        description = "Set Select Angle",
        default = 30.0,
        min = 0.0,
        max = 180.0
    )
    wm = bpy.context.window_manager
    kc =  wm.keyconfigs.active
    km = kc.keymaps['3D View']
    kmi = km.keymap_items.new(idname='object.smoothing_operator', type='TWO', value='PRESS', shift=True)
def unregister():
    bpy.utils.unregister_class(SmoothingPanel)
    bpy.utils.unregister_class(SmoothOperator)
    bpy.utils.unregister_class(AngleSmoothOperator)
    bpy.utils.unregister_class(HardOperator)
    bpy.utils.unregister_class(SharpSelect)
    bpy.utils.unregister_class(SharpBevel)
    bpy.utils.unregister_class(SharpSeam)
    bpy.utils.unregister_class(ClearBevel)
    bpy.utils.unregister_class(ClearSeam)
    bpy.utils.unregister_class(ClearSharp)
    bpy.utils.unregister_class(Xalign)
    bpy.utils.unregister_class(Yalign)
    bpy.utils.unregister_class(Zalign)
    bpy.utils.unregister_class(SelectAngle)
    del bpy.Scene.Object.angle_smooth
    del bpy.Scene.Object.angle_select

if __name__ == "__main__":
    register()
