import bpy
# Function that select sharp edges
def sharp_select():
    bpy.ops.object.mode_set(mode='OBJECT') 
    for edge in bpy.context.object.data.edges:
        if edge.use_edge_sharp:
            edge.select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE') 
    
class SharpSelect(bpy.types.Operator):  
    bl_description = "Select marked sharp edges"
    bl_idname = "object.sharpselect_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Select sharp edges
        sharp_select()
        return {'FINISHED'} 
    
class SharpBevel(bpy.types.Operator):
    bl_description = "Set sharp edges' bevel weight to 1 (Use with bevel modifier)"
    bl_idname = "object.sharpbevel_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Clear selection
        bpy.ops.mesh.select_all(action='DESELECT')  
        # Select sharp esges and set bevel weight to 1       
        sharp_select()
        bpy.ops.transform.edge_bevelweight(value=1.0)       
        return{'FINISHED'}    
    
class SharpSeam(bpy.types.Operator):
    bl_description = "Make sharp edges to seams"
    bl_idname = "object.sharpseam_operator"
    bl_label = "Select"
    
    def execute(self, context):
        # Clear selection
        bpy.ops.mesh.select_all(action='DESELECT')
        # Select sharp esges and set seams
        sharp_select()
        bpy.ops.mesh.mark_seam(clear=False)
        return {'FINISHED'} 