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

        #===============================================================================================================
        layout.label(text="Smooth Setting")   
        box = layout.box()    
        col = box.column(align=True) 
        row = col.row(align=True)
		# Smooth selected button
        row.operator("object.anglesmoothing_operator", icon = "LINCURVE", text = "Smooth")
		# Smoothing angle value   
        row.scale_x = 0.5
        row.prop(context.scene, "angle_smooth")
        # Smooth button 
        col.operator("object.smoothing_operator", icon = "SPHERECURVE", text = "Smooth Selected")
		# Hard selected button
        col.operator("object.hard_operator", icon = "NOCURVE", text = "Harden Selected")  
        #===============================================================================================================
        #===============================================================================================================
        layout.label(text="Selection")
        box = layout.box()
        col = box.column(align=True)
        
        row = col.row(align=True)
        row.operator("object.growselect_operator", text = "Grow")
        row.operator("object.shrinkselect_operator", text = "Shrink")

        row = col.row(align=True)
        row.operator("object.loopselect_operator", text = "Loop")
        row.operator("object.ringselect_operator", text = "Ring")

        row = col.row(align=True)
        # Button to selet faces by angle
        row.operator("object.angleselect_operator", icon = "RESTRICT_SELECT_OFF",text = "Select by")
        # Angle select value
        row.scale_x = 0.5
        row.prop(context.scene, "angle_select")   
        # Button to select sharp edges button
        col.operator("object.sharpselect_operator", icon = "OUTLINER_DATA_EMPTY", text = "Select Sharp Edges") 

        col = box.column(align=True) 
        col.operator("object.boundryselect_operator", icon = "DECORATE_ANIMATE", text = "Select Outter Loop")
        col.operator("object.innerselect_operator", icon = "DECORATE_KEYFRAME", text = "Select Inner Face")
        #===============================================================================================================
        #===============================================================================================================
        layout.label(text="Sharp Edges to")
        box = layout.box()
        col = box.column(align=True)

        # Button set sharp edges's  bevel weight to 1
        col.operator("object.sharpbevel_operator", icon = "STYLUS_PRESSURE", text = "Weight 1") 
        # Button to convert sharp edges to seams
        col.operator("object.sharpseam_operator", icon = "DRIVER_DISTANCE", text = "Seams")
        #===============================================================================================================
        #===============================================================================================================          
        layout.label(text="Clear")
        box = layout.box()
        row = box.row(align=True)
        # Button to clear selected sharp edges
        row.operator("object.clearsharp_operator", text = "Sharp")
        # Button to set selected sharp edges' bevel weight to 0
        row.operator("object.clearbevel_operator", text = "Weight")
        # Button to clear selected sharp edges' seams
        row.operator("object.clearseam_operator", text = "Seams")      
        #===============================================================================================================
        #===============================================================================================================       
        layout.label(text="Align")
        box = layout.box()
        row = box.row(align=True)
        # Buttons to align seleted to X,Y,Z
        split = row.split()
        col = split.column()
        col.operator('object.xalign_operator', text = "X")
        col = split.column()
        col.operator("object.yalign_operator", text = "Y")
        col = split.column()
        col.operator("object.zalign_operator", text = "Z")
        #===============================================================================================================
        #===============================================================================================================       
        layout.label(text="Align")
        box = layout.box()
        row = box.row(align=True)
        row.operator("object.lightrotate_operator")
        view = context.space_data
        shading = view.shading
        row.prop(shading, "studiolight_rotate_z", text="Rotation")