from math import sin, cos, pi
import matplotlib.pyplot as plt


def frange(start, final, step=1.0):
    result = []
    while start < final:
        result.append(start)
        start = start + step
    return result


if __name__ == "__main__":
    ts = frange(0, 2 * pi, 0.01) # frange(0, 2 * pi + 0.01, 0.01)
    xs = [sin(t) + (cos(2*t) / 9) for t in ts]
    ys = [sin(9 * t) + cos( (2**2) * t) for t in ts]
    plt.plot(xs, ys)
    plt.show()
