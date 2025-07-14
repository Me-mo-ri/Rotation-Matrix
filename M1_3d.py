from rich.console import Console
from rich.rule import Rule
import numpy as np

r = Console()

def roMa3D():
    orderedPairA = r.input("[bold green]🔢 | A")
    try:
        xA, yA = map(float, orderedPairA.split('(')[1].strip(')').split(', '))
    except Exception as e:
        r.print(Rule(f"[bold red] ❌ | Error: {e}", style="red"))

    theta = r.input("[bold green]📐 | Rotation Degree: ")
    theta_rad = np.radians(int(theta))

    cos_t = np.cos(theta_rad)
    sin_t = np.sin(theta_rad)

    nxA = round(xA * cos_t - yA * sin_t, 3)
    nyA = round(xA * sin_t + yA * cos_t, 3)

    return nxA, nyA

def C3D():
    roMa3D()