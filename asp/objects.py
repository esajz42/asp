import numpy as np

class point(object):
    """
    Representing a point in R3 space.

    Attributes
    ----------
    xyz : array_like
        Three-element array_like specifying coordinates in R3.
    """
    
    def __init__(self, xyz):
        """Initializes point object.

        Parameters
        ----------
        xyz : array_like
            Three-element array_like specifying coordinates in R3.
        """
        self.xyz = xyz
