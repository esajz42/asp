import numpy as np


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
    for ray in camera.rays:
        pass
