from matplotlib.pyplot import show, plot, scatter
from math import pi, sin, cos, fabs

def better_frange(start, final, step=1.0):
    result = []
    if start < final:
        while start < final:
            result.append(start)
            start = start + step
    else:
        while final < start:
            result.append(start)
            start = start - step
        
    return result


def draw_circle(a, b, r, col = 'black'):
    ts = better_frange(0, 2*pi, 0.01)
    xs = [a + (r * cos(t)) for t in ts]
    ys = [b + (r * sin(t)) for t in ts]

    plot(xs, ys, color = col)


def draw_rectangle(a, b, c, d, col = 'black'):
    xs = [a, c, c, a, a]
    ys = [b, b, d, d, b]
    
    plot(xs, ys, color = col)

def draw_point(a, b, col = 'black'):
    scatter(a, b, color = col)


def draw_shapes(file):
    xs, ys = [], []
    with open(file) as f:
        for line in f:
            shape = line.strip().split(';')
            if shape[0] == 'point':
                if len(shape) == 4:
                    draw_point(int(shape[1]), int(shape[2]), shape[3])
                else:
                    draw_point(int(shape[1]), int(shape[2]))
            elif shape[0] == 'circle':
                if len(shape) == 5:
                    draw_circle(int(shape[1]), int(shape[2]), int(shape[3]), shape[4])
                else:
                    draw_circle(int(shape[1]), int(shape[2]), int(shape[3]))
            else:
                if len(shape) == 6:
                    draw_rectangle(int(shape[1]), int(shape[2]), int(shape[3]), 
                                   int(shape[4]), shape[5])
                else:
                    draw_rectangle(int(shape[1]), int(shape[2]), int(shape[3]), 
                                   int(shape[4]))



if __name__ == "__main__":
    draw_shapes('shapes_with_colors.csv')
    show()
