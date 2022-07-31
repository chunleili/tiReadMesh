from mesh_data import bunnyMesh
import taichi as ti
import numpy as np
ti.init()

numParticles = len(bunnyMesh['verts']) // 3
numEdges = len(bunnyMesh['tetEdgeIds']) // 2
numTets = len(bunnyMesh['tetIds']) // 4
numSurfs = len(bunnyMesh['tetSurfaceTriIds']) // 3

pos_np = np.array(bunnyMesh['verts'], dtype=float)
tet_np = np.array(bunnyMesh['tetIds'], dtype=int)
edge_np = np.array(bunnyMesh['tetEdgeIds'], dtype=int)
surf_np = np.array(bunnyMesh['tetSurfaceTriIds'], dtype=int)

pos_np = pos_np.reshape((-1,3))
tet_np = tet_np.reshape((-1,4))
edge_np = edge_np.reshape((-1,2))
surf_np = surf_np.reshape((-1,3))

pos = ti.Vector.field(3, float, numParticles)
tet = ti.Vector.field(4, int, numTets)
edge = ti.Vector.field(2, int, numEdges)
surf = ti.Vector.field(3, int, numSurfs)

pos.from_numpy(pos_np)
tet.from_numpy(tet_np)
edge.from_numpy(edge_np)
surf.from_numpy(surf_np)
