import numpy as np


class camera(object):
    """
    Camera used to image a scene. 

    Attributes
    ----------
    orient : Vector
        Defines camera orientation: location and pointing direction
    focal : float, [meters]
        Camera system focal length. 
    array_size : tuple, (2,), [pixels]
        Number of pixels along x and y dimensions of detector.
    pixel_size : tuple, (2,), [meters]
        Size of each pixel along x and y dimensions.
    """

    def __init__(self, orient, focal, array_size, pixel_size):
        self.focal = focal
        self.array_size = array_size
        self.pixel_size = pixel_size
