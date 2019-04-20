import bpy

class Panel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Smoothing Setting"
    bl_idname = "CC_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "mesh_edit"
    bl_category = "Smoothing"

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Smooth Setting")       
        col = layout.column(align=True)
                 
		# Smooth selected button                        
        col.operator("object.smoothing_operator", icon = "SPHERECURVE", text = "Smooth Selected")
		# Hard selected button
        col.operator("object.hard_operator", icon = "NOCURVE", text = "Harden Selected")  
        row = col.row(align=True)
		# Smooth button  
        row.operator("object.anglesmoothing_operator", icon = "LINCURVE", text = "Smooth")
		# Smoothing angle value   
        row.scale_x = 0.5
        row.prop(context.scene, "angle_smooth") 
        
        layout.label(text="Sharp Edges to")
        col = layout.column(align=True)

        # Button to select sharp edges button
        col.operator("object.sharpselect_operator", icon = "MESH_CUBE", text = "Selection")
        # Button set sharp edges's  bevel weight to 1
        col.operator("object.sharpbevel_operator", icon = "STYLUS_PRESSURE", text = "Weight 1") 
        # Button to convert sharp edges to seams
        col.operator("object.sharpseam_operator", icon = "DRIVER_DISTANCE", text = "Seams")
          
        layout.label(text="Clear")
        row = layout.row(align=True)
        # Button to clear selected sharp edges
        row.operator("object.clearsharp_operator", text = "Sharp")
        # Button to set selected sharp edges' bevel weight to 0
        row.operator("object.clearbevel_operator", text = "Weight")
        # Button to clear selected sharp edges' seams
        row.operator("object.clearseam_operator", text = "Seams")      
        
        layout.label(text="Align")
        row = layout.row(align=True)
        # Buttons to align seleted to X,Y,Z
        row.operator("object.xalign_operator", text = "X")
        row.operator("object.yalign_operator", text = "Y")
        row.operator("object.zalign_operator", text = "Z")
                  
        layout.label(text="Select by Angle")
        row = layout.row(align=True)

        # Button to selet faces by angle
        row.operator("object.angleselect_operator", icon = "RESTRICT_SELECT_OFF",text = "Select")
        # Angle select value
        row.scale_x = 0.5
        row.prop(context.scene, "angle_select")
        