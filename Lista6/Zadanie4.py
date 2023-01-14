from math import sin, cos, tan, radians, fabs
import matplotlib.pyplot as plt


def frange_better(start, final, step=1.0):
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

def draw_turtle_path(commands):
    xs = []
    ys = []
    position = (0, 0)
    orientation = 0
    for command in commands:
        if command[0] == "forward":
            if sin(radians(orientation)) not in [-1, 0, 1]:
                x1 = frange_better(position[0], position[0] + cos(radians(orientation)) * command[1], 0.01)
                move = position[1] - tan(radians(orientation)) * position[0]
                y1 = [tan(radians(orientation)) * i + move for i in x1]
            elif sin(radians(orientation)) == 0:
                x1 = frange_better(position[0], position[0] + command[1], 0.01)
                y1 = [position[1]] * len(x1)
            else:
                y1 = frange_better(position[0], position[0] + command[1], 0.01)
                x1 = [position[0]] * len(y1)
                
            position = x1[-1], y1[-1]
            for i in range(0, len(x1)):
                xs.append(x1[i])
                ys.append(y1[i])

        elif command[0] == "left":
            orientation = orientation + command[1]
        else:
            orientation = orientation - command[1]

        
    return xs, ys

    
if __name__ == "__main__":
    xs, ys = draw_turtle_path([('forward', 15), ('left', 144), ('forward', 15), 
                               ('left', 144), ('forward', 15), ('left', 144), 
                               ('forward', 15), ('left', 144), ('forward', 15)])
    
    plt.plot(xs , ys, c = 'r')
    plt.show()
        
