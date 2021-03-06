import bpy
d = bpy.context.active_object.data.archipack_fence[0]
bpy.ops.archipack.material(category='fence', material='DEFAULT')

d.angle_limit = 0.39269909262657166
d.da = 1.5707963705062866
d.handrail = True
d.handrail_alt = 1.100000023841858
d.handrail_expand = True
d.handrail_extend = 0.15000000596046448
d.handrail_offset = 0.0
d.handrail_profil = 'SQUARE'
d.handrail_radius = 0.029999999329447746
d.handrail_slice = True
d.handrail_slice_right = True
d.handrail_x = 0.07999999076128006
d.handrail_y = 0.03999999910593033
d.idmat_handrail = '0'
d.idmat_panel = '2'
d.idmat_post = '0'
d.idmat_subs = '0'
d.idmats_expand = True
d.panel = False
d.panel_alt = 0.30000001192092896
d.panel_dist = 0.0010000000474974513
d.panel_expand = False
d.panel_offset_x = 0.0
d.panel_x = 0.009999999776482582
d.panel_z = 0.800000011920929
d.parts_expand = False
d.post = True
d.post_alt = 0.0
d.post_expand = True
d.post_rotation = 1.5707963705062866
d.post_spacing = 1.0399999618530273
d.post_x = 0.05999999865889549
d.post_y = 0.05999999865889549
d.post_z = 1.100000023841858
d.radius = 0.699999988079071
d.rail = True
d.rail_expand = False
d.rail_n = 2
d.rails.clear()
item_sub_1 = d.rails.add()
item_sub_1.x = 0.027000000700354576
item_sub_1.profil = 'SQUARE'
item_sub_1.extend = 0.0
item_sub_1.z = 0.03999999910593033
item_sub_1.mat = '0'
item_sub_1.alt = 0.25
item_sub_1.offset = 0.017000000923871994
item_sub_1 = d.rails.add()
item_sub_1.x = 0.027000000700354576
item_sub_1.profil = 'SQUARE'
item_sub_1.extend = 0.0
item_sub_1.z = 0.03999999910593033
item_sub_1.mat = '0'
item_sub_1.alt = 0.8199999928474426
item_sub_1.offset = 0.017000000923871994
d.shape = 'RECTANGLE'
d.subs = True
d.subs_alt = 0.10000000149011612
d.subs_bottom = 'STEP'
d.subs_expand = True
d.subs_offset_x = 0.009999999776482582
d.subs_rotation = 1.5707963705062866
d.subs_spacing = 0.15000000596046448
d.subs_x = 0.027000000700354576
d.subs_y = 0.10000000149011612
d.subs_z = 0.8999999761581421
d.user_defined_post = ''
d.user_defined_post_enable = True
d.user_defined_resolution = 12
d.user_defined_subs = ''
d.user_defined_subs_enable = True
d.user_path_reverse = False
d.x_offset = 0.0
