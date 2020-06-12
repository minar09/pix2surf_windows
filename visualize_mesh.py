import trimesh
import pyrender
import pickle
import numpy as np


def visualize_init_meshes():
    pants_trimesh = trimesh.load('assets/init_meshes/pants.obj')
    pants = pyrender.Mesh.from_trimesh(pants_trimesh)

    shirts_trimesh = trimesh.load('assets/init_meshes/shirts.obj')
    shirts = pyrender.Mesh.from_trimesh(shirts_trimesh)

    shorts_trimesh = trimesh.load('assets/init_meshes/shorts.obj')
    shorts = pyrender.Mesh.from_trimesh(shorts_trimesh)

    scene = pyrender.Scene()
    scene.add(pants)  # comment out if you don't want to visualize
    scene.add(shirts)  # comment out if you don't want to visualize
    scene.add(shorts)  # comment out if you don't want to visualize
    pyrender.Viewer(scene, use_raymond_lighting=True)


def visualize_smpl():
    smpl_file = 'assets/neutral_smpl.pkl'
    with open(smpl_file, 'rb') as fh:
        smpl = pickle.load(fh, encoding='latin1')

    # Form the scene, with smoothing turned on.
    tm = trimesh.Trimesh(vertices=smpl['v_template'], faces=smpl['f'])
    mesh = pyrender.Mesh.from_trimesh(tm, smooth=True)
    scene = pyrender.Scene()
    scene.add(mesh)

    pyrender.Viewer(scene, use_raymond_lighting=True)


if __name__ == '__main__':
    visualize_init_meshes()    # visualize garment template meshes
    visualize_smpl()
