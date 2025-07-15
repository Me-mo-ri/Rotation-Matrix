from rich.console import Console
from rich.rule import Rule
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()

plt.rc('font', family=font_name)

r = Console()

def getLength():
    lengths = {}
    axes = ['x', 'y', 'z']

    for axis in axes:
        while True:
            length = r.input(f"[bold green]🔢 | {axis}축 길이: [/bold green]")
            try:
                length = float(length)
                lengths[axis] = length
                break
            except Exception as e:
                r.print(Rule(f"[bold red] ❌ | Error: {e} [/bold red]", style="red"))
    
    return lengths['x'], lengths['y'], lengths['z']

def roMa3D():
    orderedPairA = r.input("[bold green]🔢 | A")
    r.print()

    try:
        xA, yA = map(float, orderedPairA.split('(')[1].strip(')').split(', '))
    except Exception as e:
        r.print(Rule(f"[bold red] ❌ | Error: {e}", style="red"))
        r.print()

    theta = r.input("[bold green]📐 | Rotation Degree: ")
    theta_rad = np.radians(int(theta))

    cos_t = np.cos(theta_rad)
    sin_t = np.sin(theta_rad)

    nxA = round(xA * cos_t - yA * sin_t, 3)
    nyA = round(xA * sin_t + yA * cos_t, 3)

    return nxA, nyA

def C3D():
    lengthX, lengthY, lengthZ = getLength()

    r.print(f"[green] Input: X={lengthX:.2f}, Y={lengthY:.2f}, Z={lengthZ:.2f}[/green]")
    r.print()

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    vertices = [
        (0, 0, 0), (lengthX, 0, 0), (0, lengthY, 0), (0, 0, lengthZ),
        (lengthX, lengthY, 0), (lengthX, 0, lengthZ), (0, lengthY, lengthZ),
        (lengthX, lengthY, lengthZ)
    ]

    edges = [
        (0, 1), (0, 2), (0, 3),
        (1, 4), (1, 5),
        (2, 4), (2, 6),
        (3, 5), (3, 6),
        (4, 7), (5, 7), (6, 7)
    ]

    for edge in edges:
        coordX = [vertices[edge[0]][0], vertices[edge[1]][0]]
        coordY = [vertices[edge[0]][1], vertices[edge[1]][1]]
        coordZ = [vertices[edge[0]][2], vertices[edge[1]][2]]
        ax.plot(coordX, coordY, coordZ, color='blue')

    ax.set_xlabel('x축')
    ax.set_ylabel('y축')
    ax.set_zlabel('z축')

    max_dim = max(abs(lengthX), abs(lengthY), abs(lengthZ))
    padding = max_dim * 0.2
    
    ax.set_xlim([0 - padding, max_dim + padding])
    ax.set_ylim([0 - padding, max_dim + padding])
    ax.set_zlim([0 - padding, max_dim + padding])

    ax.scatter([0], [0], [0], color='red', s=50, label='원점')

    ax.set_title(f"3차원 8개 점 (X:{lengthX:.1f}, Y:{lengthY:.1f}, Z:{lengthZ:.1f})")
    plt.show()