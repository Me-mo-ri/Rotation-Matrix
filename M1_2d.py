from M1_plt_2d import vis2d_1, vis2d_2, vis2d_3, vis2d_4
from rich.console import Console
from rich.rule import Rule
import numpy as np

r = Console()

def roMa1():
    orderedPairA = r.input("[bold green]🔢 | A")
    try:
      xA, yA = map(float, orderedPairA.split('(')[1].strip(')').split(', '))
    except Exception as e:
      r.print(Rule("[bold red] ❌ | Error in calculating coordinates: A", style="red"))

    theta = r.input("[bold green]📐 | Rotation Degree: ")
    theta_rad = np.radians(int(theta))

    cos_t = np.cos(theta_rad)
    sin_t = np.sin(theta_rad)

    nxA = round(xA * cos_t - yA * sin_t, 3)
    nyA = round(xA * sin_t + yA * cos_t, 3)

    return nxA, nyA

def roMa2():
    orderedPairA = r.input("[bold green]🔢 | A")
    try:
      xA, yA = map(float, orderedPairA.split('(')[1].strip(')').split(', '))
    except Exception as e:
      r.print(Rule("[bold red] ❌ | Error in calculating coordinates: A", style="red"))

    theta = r.input("[bold green]📐 | Rotation Degree: ")
    theta_rad = np.radians(int(theta))

    cos_t = np.cos(theta_rad)
    sin_t = np.sin(theta_rad)

    nxA = xA * cos_t - yA * sin_t
    nyA = xA * sin_t + yA * cos_t

    return [nxA, nyA]
    
def roMa3():
    orderedPairA = r.input("[bold green]🔢 | A")
    try:
      xA, yA = map(float, orderedPairA.split('(')[1].strip(')').split(', '))
    except Exception as e:
      r.print(Rule("[bold red] ❌ | Error in calculating coordinates: A", style="red"))

    theta = r.input("[bold green]📐 | Rotation Degree: ")
    theta_rad = np.radians(int(theta))

    cos_t = np.cos(theta_rad)
    sin_t = np.sin(theta_rad)

    nxA = xA * cos_t - yA * sin_t
    nyA = xA * sin_t + yA * cos_t

    return nxA, nyA
    
def roMa4():
    orderedPairA = r.input("[bold green]🔢 | A")
    try:
      xA, yA = map(float, orderedPairA.split('(')[1].strip(')').split(', '))
    except Exception as e:
      r.print(Rule("[bold red] ❌ | Error in calculating coordinates: A", style="red"))

    theta = r.input("[bold green]📐 | Rotation Degree: ")
    theta_rad = np.radians(int(theta))

    cos_t = np.cos(theta_rad)
    sin_t = np.sin(theta_rad)

    nxA = xA * cos_t - yA * sin_t
    nyA = xA * sin_t + yA * cos_t

    return nxA, nyA

def C2D():
    r.print(Rule("[bold green] 📏 [/bold green]"))
    print()

    calType = int(r.input("[bold green]📏 | Numbers: "))

    if calType == 1:
        print()
        r.print(Rule("[bold yellow] One point in 2nd Dimension ", style="yellow"))
        print()
        print(roMa1())

    elif calType == 2:
        print()
        r.print(Rule("[bold yellow] Two points in 2nd Dimension ", style="yellow"))
        print()
        print(roMa2())

    elif calType == 3:
        print()
        r.print(Rule("[bold yellow] Three points in 2nd Dimension ", style="yellow"))
        print()
        print(roMa3())

    elif calType == 4:
        print()
        r.print(Rule("[bold yellow] Four points in 2nd Dimension ", style="yellow"))
        print()
        print(roMa4())

    else:
       r.print(Rule("[bold red] ❌ | invalidValue", style="red"))