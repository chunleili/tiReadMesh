from mesh_data import bunnyMesh
import taichi as ti
import numpy as np
ti.init()

numParticles = len(bunnyMesh['verts']) // 3
numEdges = len(bunnyMesh['tetEdgeIds']) // 2
numTets = len(bunnyMesh['tetIds']) // 4
numSurfs = len(bunnyMesh['tetSurfaceTriIds']) // 3

verts = np.array(bunnyMesh['verts'], dtype=float)
tetIds = np.array(bunnyMesh['tetIds'], dtype=int)
tetEdgeIds = np.array(bunnyMesh['tetEdgeIds'], dtype=int)
tetSurfaceTriIds = np.array(bunnyMesh['tetSurfaceTriIds'], dtype=int)

verts = verts.reshape((-1,3))
tetIds = tetIds.reshape((-1,4))
tetEdgeIds = tetEdgeIds.reshape((-1,2))
tetSurfaceTriIds = tetSurfaceTriIds.reshape((-1,3))

pos = ti.Vector.field(3, float, numParticles)
tet = ti.Vector.field(4, int, numTets)
edge = ti.Vector.field(2, int, numEdges)
surf = ti.Vector.field(3, int, numSurfs)

pos.from_numpy(verts)
tet.from_numpy(tetIds)
edge.from_numpy(tetEdgeIds)
surf.from_numpy(tetSurfaceTriIds)
