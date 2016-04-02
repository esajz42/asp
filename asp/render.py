import numpy as np
from asp.math import intersect, inside


def snapshot(camera, triangles):
    """Renders instaneous image of a scene. 

    Parameters
    ----------
    camera : Camera
        Camera to render scene with.
    triangles : iter[Triangles]
        Triangular facets making up scene content.

    Returns
    -------
    image : Image
        Spatial, spectral rendered image of scene. 
    """

    # Intersect camera rays with scene triangles 
    image = []
    for ray in camera.rays():
        for triangle in triangles:
            interection_point = intersect(ray, triangle)
            if inside(intersection_point, triangle):
                image.append(1)
            else:
                image.append(0)
    return np.asarray(image).reshape(camera.array_size)
