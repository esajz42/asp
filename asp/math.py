import numpy as np
from asp.objects import Point, Vector


def add(points):
    """Sequentially adds iterable of Points.
    
    Parameters
    ----------
    points : iter[Points]
        Iterable of Point objects.

    added : Point
        Point with added xyz coordinates of all Points in input.
    """
    sum = points[0].xyz
    for point in Points[1:]:
        sum += point.xyz
    return Point(sum)


def mul(points):
    """Sequentially multiplies iterable of Points.
    
    Parameters
    ----------
    points : iter[Points]
        Iterable of Point objects.

    Point
        Point with multiplied xyz coordinates of all Points in input.
    """
    prod = points[0].xyz
    for point in Points[1:]:
        prod *= point.xyz
    return Point(prod)


def sub(points):
    """Sequentially subtracts iterable of Points.
    
    Parameters
    ----------
    points : iter[Points]
        Iterable of Point objects.

    Point
        Point with subtracted xyz coordinates of all Points in input.
    """
    diff = points[0].xyz
    for point in Points[1:]:
        diff -= point.xyz
    return Point(diff)   


def div(points):
    """Sequentially subtracts iterable of Points.
    
    Parameters
    ----------
    points : iter[Points]
        Iterable of Point objects.

    Point
        Point with subtracted xyz coordinates of all Points in input.
    """
    quo = points[0].xyz
    for point in Points[1:]:
        quo /= point.xyz
    return Point(quo)  


def normal(plane):
    """Computes the normal unit Vector of a Plane.
    
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

    # Compute two in-plane vectors
    v1 = plane.points[1].xyz - plane.points[0].xyz
    v2 = plane.points[2].xyz - plane.points[0].xyz

    # Cross product of two in-plane vectors gives normal vector
    norm_vec = np.cross(v1, v2)
    return Vector(norm_vec / np.linalg.norm(norm_vec))


def plane_coefficients(plane):
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
    abc = normal(plane)
    d = np.dot(-plane.points[0].xyz, abc.xyz)
    return abc.xyz.append(d) 


def intersection(vector, plane):
    """Computes the intersection Point of a Vector and Plane

    Parameters 
    ----------
    vector : Vector
        Vector to intersect with plane.
    plane : Plane
        Plane for Vector to intersect.

    Returns
    -------
    Point
        Intersection Point of ray and vector.

    References 
    -----------
    .. [1] https://www.khanacademy.org/partner-content/pixar/rendering/rendering-2/v/rendering-9
    """
    plane_coeffs = plane_coefficients(plane)
