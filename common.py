import matplotlib.pyplot as plt

def renderDots(dots):
    x_cords = []
    y_cords = []
    templ_str = "(%f, %f)"
    for dot in dots:
        x_cords.append(dot[0])
        y_cords.append(dot[1])
        plt.annotate(templ_str % (dot[0], dot[1]), (dot[0], dot[1]))

    plt.plot(x_cords, y_cords, 'ro')