import numpy as np

class Point(object):
    """
    Representing a point in R3 space.

    Attributes
    ----------
    xyz : array_like
        Three-element array_like specifying coordinates in R3.

    Methods
    -------
    shiftby(xyz=xyz)
        Shifts Point by specified distances.
    shiftto(xyz=xyz)
        Shifts Point to specified location.
    """
    
    def __init__(self, xyz):
        """Initializes Point object.

        Parameters
        ----------
        xyz : array_like
            Three-element array_like specifying coordinates in R3.
        """
        self._xyz = xyz

    @property
    def xyz(self):
        return self._xyz

    def shiftby(self, xyz):
        """Shifts Point object by specified distances.

        Parameters
        ----------
        xyz : array_like
            Distances to shift Point by along each axis.

        Returns
        -------
        self : Updated Point object.
        """
        self.xyz += xyz
        return self

    def shiftto(self, xyz):
        """Shifts Point object to specified position.

        Parameters
        ----------
        xyz : array_like
            New position xyz to set Point to.

        Returns
        -------
        self : Updated Point object.
        """
        self.xyz = xyz
        return self
