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


def divides(points):
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
    """Computes the normal Vector of a Plane.
    
    Parameters
    ----------
    plane : Plane
        Plane object to compute normal Vector for. 

    Returns 
    --------
    Vector
        Normal Vector of parameter Plane.
    """

    # Compute two in-plane vectors
    v1 = plane.points[0].xyz - plane.points[1].xyz
    v2 = plane.points[0].xyz - plane.points[2].xyz

    # Cross product of two in-plane vectors gives normal vector
    return Vector(np.cross(v1, v2))
