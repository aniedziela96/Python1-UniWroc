from math import sin, cos, acos, pi


def radian(alpha):
    return (alpha * pi)/180


def great_circle_distance(phi1, lambda1, phi2, lambda2):
    phi1 = radian(phi1)
    phi2 = radian(phi2)
    lambda1 = radian(lambda1)
    lambda2 = radian(lambda2)
    return 6371.01 * acos(sin(phi1) + cos(phi1) * cos(phi2) * cos(lambda1 - lambda2))
