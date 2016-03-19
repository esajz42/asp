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

        Returns
        -------
        Point
            Instantiation of Point.
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


class Vector(Point):
    """
    Represents a vector in R3.

    A Vector is a Point with an associated direction.

    Attributes
    ----------
    xyz : array_like
        Three-element array_like specifying coordinates in R3.
    dir : array_like
        Three-element array_like specifying vector direction.
    """

    def __init__(self, xyz, dir):
        """Initializes a Vector object.

        Parameters
        ----------
        xyz : array_like
            Three-element array_like specifying coordinates in R3.
        dir : array_like
            Three-element array_like specifying vector direction.

        Returns
        -------
        Vector
            Instantiation of Vector.
        """
        self._dir = dir
        super(Vector).__init__(xyz)

    @property
    def dir(self):
        return self._dir


class Ray(Vector):
    """
    Represents a ray in R3.

    A Ray is a Vector with an associated value.

    Attributes
    ----------
    xyz : array_like
        Three-element array_like specifying coordinates in R3.
    dir : array_like
        Three-element array_like specifying vector direction.
    value : float
        Value or weight assigned to Ray.
    """

    def __init__(self, xyz, dir, value=0.):
        """Initializes a Ray object.

        Parameters
        ----------
        xyz : array_like
            Three-element array_like specifying coordinates in R3.
        dir : array_like
            Three-element array_like specifying vector direction.
        value : float, optional
            Value or weight assigned to Ray. Default is 0.

        Returns
        -------
        Ray
            Instantiation of Ray.
        """
        self._value = value
        super(Ray).__init__(xyz, dir)

    @property
    def value(self):
        return self._value
