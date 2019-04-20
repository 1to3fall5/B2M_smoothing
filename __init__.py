# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "M2B",
    "author" : "Chen Chen",
    "description" : "",
    "blender" : (2, 80, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . panel              import Panel
from . op_smooth          import SmoothOperator
from . op_smooth          import AngleSmoothOperator
from . op_smooth          import HardOperator
from . op_convert         import SharpSelect
from . op_convert         import SharpBevel
from . op_convert         import SharpSeam
from . op_clear           import ClearBevel
from . op_clear           import ClearSeam
from . op_clear           import ClearSharp
from . op_align           import Xalign
from . op_align           import Yalign
from . op_align           import Zalign
from . op_select          import SelectAngle

def register():
    bpy.utils.register_class(Panel)
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
    bpy.utils.unregister_class(Panel)
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
    #del bpy.Scene.Object.angle_smooth
    #del bpy.Scene.Object.angle_select

if __name__ == "__main__":
    register()