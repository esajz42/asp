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


def intersect(vector, plane):
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
        Intersection Point of Plane and Vector.

    References 
    -----------
    .. [1] https://www.khanacademy.org/partner-content/pixar/rendering/rendering-2/v/rendering-9
    .. [2] Curless, B., Ray-triangle intersection, 2006
    """

    # Plane equation a, b, c (normal vector) and d coefficients
    plane_coeffs = plane.get_coefficients(plane)
    abc = plane_coeffs[:3]
    d = plane_coeffs[3]

    # Vector origin 
    p = vector.xyz

    # Compute distance along vector, t
    t = (d - np.dot(abc, p)) / (abc, d)

    # Compute intersection using t
    q = p + t * d

    return Point(q)


def inside(point, triangle):
    """Checks if a point lies within a triangle or not.

    Parameters
    ----------
    point : Point
        Point in same plane as triangle. 
    triangle : Triangle
        Triangle facet.

    Returns
    -------
    in : bool
        True of point is inside triangle, False otherwise.

    References
    ----------
    .. [1] https://www.khanacademy.org/partner-content/pixar/rendering/rendering-2/v/rendering-9
    .. [2] Curless, B., Ray-triangle intersection, 2006
    """
    n = triangle.normal
    c0 = np.cross(sub([triangle.points[1], triangle.points[0]]),
                  sub([triangle.points[2], triangle.points[0]]))
    c1 = np.cross(sub([triangle.points[0], triangle.points[1]]),
                  sub([triangle.points[2], triangle.points[1]]))
    c2 = np.cross(sub([triangle.points[0], triangle.points[2]]),
                  sub([triangle.points[1], triangle.points[2]]))
    return (c0.dot(n) >= 0) and (c1.dot(n) >= 0) and (c2.dot(n) >= 0)


def rotation_matrix(a, b):
    """Returns rotation matrix that will rotate vector a onto b.

    Parameters
    ----------
    a : Vector
        A vector in R3
    b : Vector
        Vector to rotate a onto. 
    Returns
    -------
    rot : array, (3, 3)
        Matrix that rotates a onto b.

    References
    ----------
    .. [1] http://math.stackexchange.com/questions/180418/calculate-rotation-matrix-to-align-vector-a-to-vector-b-in-3d 
    """
    # Make sure a and b vectors are unit
    a /= np.linalg.norm(a.xyz)
    b /= np.linalg.norm(b.xyz)

    # Find sin and cos of angle to rotate by
    v = np.cross(a, b) 
    s = np.linalg.norm(v)
    c = np.dot(a, b)

    # Define skew-symmetric cross product of v
    vx = [[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]]

    # Construct rotation matrix
    rot = np.eye(3) + vx + (vx ** 2 * ((1 - c) / s ** 2))
    return rot
