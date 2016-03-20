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
        self.xyz = np.asarray(xyz).squeeze()

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
        self.xyz += np.asarray(xyz).squeeze()
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
        self.xyz = np.asarray(xyz).squeeze()
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

    Methods
    -------
    shiftby(xyz=xyz)
        Shifts Vector by specified distances.
    shiftto(xyz=xyz)
        Shifts Vector to specified location.
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
        self.dir = np.asarray(dir).squeeze()
        super(Vector).__init__(xyz)


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

    Methods
    -------
    shiftby(xyz=xyz)
        Shifts Ray by specified distances.
    shiftto(xyz=xyz)
        Shifts Ray to specified location.
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
        self.value = np.asarray(value).squeeze()
        super(Ray).__init__(xyz, dir)


class Plane(object):
    """
    Plane defined by three or more Points.

    Attributes
    ----------
    points : iter[Point]
        Iterable of at least three Points.
    normal : Vector
        Unit normal Vector of plane.

    Methods
    -------
    get_coefficients()
        Returns coefficients of scalar plane equation.
    """

    def __init__(self, points):
        """Initializes Plane object."""
        self._points = list(points)
        self._normal = None

    @property
    def points(self):
        return self._points

    @property
    def normal(self):
        """Computes the normal unit Vector of Plane.
        
        Parameters
        ----------
        plane : Plane
            Plane object to compute normal Vector for. 
        Returns 
        --------
        Vector
            Normal unit Vector of parameter Plane.

        References 
        ----------
        .. [1] http://tutorial.math.lamar.edu/Classes/CalcIII/EqnsOfPlanes.aspx 
        """
        if self._normal is None:

            # Compute two in-plane vectors
            v1 = self.points[1].xyz - self.points[0].xyz
            v2 = self.points[2].xyz - self.points[0].xyz

            # Cross product of two in-plane vectors gives normal vector
            norm = np.cross(v1, v2)
            self._normal = Vector(norm / np.linalg.norm(norm))

        return self._normal


        def get_coefficients(self):
            """Computes coefficients of scalar plane equation. 

            Parameters
            ----------
            plane : Plane
                A Plane object. 

            Returns
            -------
            array
                Coefficients of scalar plane equation.

            References 
            ----------
            .. [1] http://tutorial.math.lamar.edu/Classes/CalcIII/EqnsOfPlanes.aspx 
            """
            d = self.normal.xyz.dot(self.points[0].xyz)
            return self.normal.xyz.append(d) 


class Triangle(Plane):
    """
    Triangular facet defined by three points.

    Attributes
    ----------
    points : iter[Point]
        Iterable of at least three Points.
    normal : Vector
        Unit normal Vector of plane.

    Methods
    -------
    get_coefficients()
        Returns coefficients of scalar plane equation for the Triangle's supporting
        plane.
    """
        
    def __init__(self, points):
        if len(points) != 3:
            raise ValueError("Triangle objects are defined by exactly 3 points.")

        super(Triangle).__init__(points)
