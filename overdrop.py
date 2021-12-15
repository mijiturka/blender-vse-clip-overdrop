import bpy

bl_info = {
    "name": 'Apply Overdrop Settings',
    "blender": (2, 93, 0),
    "category": "Sequencer",
}

class OverdropSettings(bpy.types.Operator):
    '''Apply Overdrop Settings'''
    bl_idname = 'sequencer.overdrop_settings'
    bl_label = 'Apply Overdrop Settings'
    bl_options = {'REGISTER'}

    def execute(self, context):
        print('Applying OverdropSettings')

        strip = context.scene.sequence_editor.active_strip

        # Do the things we can do to the strip itself
        strip.blend_type = 'OVER_DROP'

        # Add a transform strip through which we'll apply the rest
        bpy.ops.sequencer.effect_strip_add(type="TRANSFORM")
        # Adding the transform strip will automatically select it
        transform = context.scene.sequence_editor.active_strip

        transform.scale_start_x = 0.38
        transform.scale_start_y = 0.38

        transform.translation_unit = 'PIXELS'
        transform.translate_start_x = 200
        transform.translate_start_y = -400

        transform.crop.max_x = 240
        transform.crop.min_x = 240

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OverdropSettings.bl_idname)

def register():
    bpy.utils.register_class(OverdropSettings)
    bpy.types.SEQUENCER_MT_context_menu.append(menu_func)

def unregister():
    bpy.types.SEQUENCER_MT_context_menu.remove(menu_func)
    bpy.utils.unregister_class(OverdropSettings)

if __name__ == '__main__':
    register()
