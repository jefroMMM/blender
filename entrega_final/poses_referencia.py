import bpy,math
from mathutils import Vector,Matrix

POSES=['brazos_arriba','codos','torso','cabeza_cuello','caminar','correr','agachado']
def reset(rig):
    rig.location=(0,0,0)
    for b in rig.pose.bones:b.matrix_basis.identity()
    bpy.context.view_layer.update()
def rotate(rig,name,axis,angle):
    b=rig.pose.bones[name];b.rotation_mode='XYZ';b.rotation_euler[axis]=angle
def aim(rig,name,direction):
    bpy.context.view_layer.update();b=rig.pose.bones[name];rest=b.bone
    target=(rig.matrix_world.inverted().to_3x3()@Vector(direction)).normalized()
    q=(rest.tail_local-rest.head_local).normalized().rotation_difference(target)
    matrix=(q.to_matrix()@rest.matrix_local.to_3x3()).to_4x4();matrix.translation=b.head
    b.rotation_mode='QUATERNION';b.matrix=matrix;bpy.context.view_layer.update()
def apply_pose(rig,name):
    reset(rig)
    if name=='brazos_arriba':
        for side,sign in [('L',1),('R',-1)]:
            aim(rig,'clavicle.'+side,(sign*.96,0,.28));aim(rig,'upper_arm.'+side,(sign*.50,0,.866))
    elif name=='codos':
        for side,sign in [('L',1),('R',-1)]:aim(rig,'upper_arm.'+side,(sign*.45,-.08,-.89));rotate(rig,'forearm.'+side,0,1.35)
    elif name=='torso':
        for b,a in [('pelvis',-.12),('spine',.18),('chest',.30),('neck',-.12),('head',-.12)]:rotate(rig,b,1,a)
    elif name=='cabeza_cuello':
        rotate(rig,'neck',1,.20);rotate(rig,'head',1,.35);rotate(rig,'head',2,.08)
    elif name in ['caminar','correr']:
        running=name=='correr'
        for b,a in [('thigh.L',.78 if running else .36),('thigh.R',-.45 if running else -.32),('shin.L',-1.20 if running else -.25),('shin.R',-1.10 if running else -.65),('foot.L',.30 if running else .05),('foot.R',.40 if running else .38),('toe.R',.12)]:rotate(rig,b,0,a)
        if running:
            rotate(rig,'spine',0,.12);rotate(rig,'chest',0,.10);rotate(rig,'neck',0,-.10)
        for side,sign in [('L',1),('R',-1)]:
            swing=(.55 if running else .22)*(1 if side=='L' else -1)
            aim(rig,'upper_arm.'+side,(sign*.28,swing,-.79 if running else -.93))
            rotate(rig,'forearm.'+side,0,(1.0 if side=='L' else 1.20) if running else (.25 if side=='L' else .45))
    elif name=='agachado':
        for side in ['L','R']:
            rotate(rig,'thigh.'+side,0,.80);rotate(rig,'shin.'+side,0,-1.45);rotate(rig,'foot.'+side,0,.65)
        rotate(rig,'spine',0,.22);rotate(rig,'chest',0,.04)
        rig.pose.bones['pelvis'].location=rig.data.bones['pelvis'].matrix_local.to_3x3().inverted()@Vector((0,0,-.24))
    bpy.context.view_layer.update()
    if name in ['caminar','correr','agachado']:
        for side in ['L','R']:
            h=rig.matrix_world@rig.pose.bones['thigh.'+side].head;k=rig.matrix_world@rig.pose.bones['shin.'+side].head;a=rig.matrix_world@rig.pose.bones['foot.'+side].head
            assert (k-h).cross(a-k).x>0,(name,side,'wrong knee flexion direction')
def evaluated_points(root):
    bpy.context.view_layer.update();dg=bpy.context.evaluated_depsgraph_get();points=[]
    for o in root.all_objects:
        if o.type!='MESH':continue
        ev=o.evaluated_get(dg);me=ev.to_mesh();points.extend(ev.matrix_world@v.co for v in me.vertices);ev.to_mesh_clear()
    return points
def ground(rig,root):
    points=evaluated_points(root);rig.location.z+=.001-min(p.z for p in points);bpy.context.view_layer.update()

# Ejemplo: apply_pose(bpy.data.objects["RIG | Caminante"], "caminar")
# Reposo: reset(bpy.data.objects["RIG | Caminante"])
