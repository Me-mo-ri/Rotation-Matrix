from rich.console import Console
from rich.rule import Rule
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()

plt.rc('font', family=font_name)

r = Console()

def calPointRotation(x: float, y: float, theta: float):
    theta_rad = np.radians(theta)

    cosTheta = np.cos(theta_rad)
    sinTheta = np.sin(theta_rad)

    X = round(x * cosTheta - y * sinTheta, 3)
    Y = round(x * sinTheta + y * cosTheta, 3)

    return X, Y

def getOrderedPair(prompt_text: str):
    while True:
        ordered_pair_str = r.input(f"[bold green]🔢 | {prompt_text}[/bold green]")
        print()
        try:
            parts = ordered_pair_str.strip().replace('(', '').replace(')', '').split(',')

            if len(parts) != 2:
                raise ValueError("Input must contain two values separated by a comma")
            
            x_val = float(parts[0].strip())
            y_val = float(parts[1].strip())
            
            return x_val, y_val
        
        except Exception as e:
            r.print(Rule(f"[bold red] ❌ | Error: {e} [/bold red]", style="red"))
            print()

def C2D():
    while True:
        try:
            calType = int(r.input("[bold green]📏 | Numbers: [/bold green]"))
            print()
            if calType >= 1:
                break
        except Exception as e:
            r.print(Rule(f"[bold red] ❌ | Error: {e} [/bold red]", style="red"))
            print()

    messages = {
        1: "One point in 2nd Dimension",
        2: "Two points in 2nd Dimension",
        3: "Three points in 2nd Dimension",
        4: "Four points in 2nd Dimension",
    }

    r.print(Rule(f"[bold yellow] {messages[calType]} [/bold yellow]", style="yellow"))
    r.print()
 
    while True:
        theta_str = r.input("[bold green]📐 | Rotation : [/bold green]")
        print()
        try:
            inputTheta = float(theta_str)
            break
        except Exception as e:
            r.print(Rule(f"[bold red] ❌ | Error: {e} [/bold red]", style="red"))
            print()

    originalPoints = []
    rotatedPoints = []

    for i in range(calType):
        r.print(Rule(f"\n[cyan] {i+1}번째 점 좌표 [/cyan]", style="cyan"))
        print()
        
        originalX, originalY = getOrderedPair(f"점 {chr(65+i)}") 
        
        X, Y = calPointRotation(
            originalX, originalY, inputTheta
        )
        
        originalPoints.append((originalX, originalY))
        rotatedPoints.append((X, Y))

        r.print(f"[green]원본 점 {chr(65+i)}: ([bold]{originalX:.2f}[/bold], [bold]{originalY:.2f}[/bold])[/green]")
        r.print(f"[green]회전된 점 {chr(65+i)}: ([bold]{X:.2f}[/bold], [bold]{Y:.2f}[/bold])[/green]")

    plt.figure()
    maxVal = 0

    orig_xs_for_polygon = []
    orig_ys_for_polygon = []
    rot_xs_for_polygon = []
    rot_ys_for_polygon = []

    for i in range(calType):
        origX, origY = originalPoints[i]
        rotX, rotY = rotatedPoints[i]
        
        colors = ['red', 'blue', 'green', 'purple']
        pointColor = colors[i % len(colors)]

        plt.plot(origX, origY, 'o', color=pointColor, markersize=8, label=f'원본 {chr(65+i)}')
        plt.plot(rotX, rotY, 'X', color=pointColor, markersize=8, label=f'회전 {chr(65+i)}')
        
        plt.plot([0, origX], [0, origY], ':', color=pointColor, alpha=0.6)
        plt.plot([0, rotX], [0, rotY], ':', color=pointColor, alpha=0.8)

        maxVal = max(maxVal, abs(origX), abs(origY), abs(rotX), abs(rotY))

        orig_xs_for_polygon.append(origX)
        orig_ys_for_polygon.append(origY)
        rot_xs_for_polygon.append(rotX)
        rot_ys_for_polygon.append(rotY)

    if calType >= 3:
        orig_xs_for_polygon.append(orig_xs_for_polygon[0])
        orig_ys_for_polygon.append(orig_ys_for_polygon[0])
        plt.plot(orig_xs_for_polygon, orig_ys_for_polygon, 'k-', linewidth=1.5, label='원본 도형')

        rot_xs_for_polygon.append(rot_xs_for_polygon[0])
        rot_ys_for_polygon.append(rot_ys_for_polygon[0])
        plt.plot(rot_xs_for_polygon, rot_ys_for_polygon, 'k-', linewidth=1.5, label='회전된 도형')

    elif calType == 2:
        plt.plot([originalPoints[0][0], originalPoints[1][0]], [originalPoints[0][1], originalPoints[1][1]], 'k-', label='원본 선분')
        plt.plot([rotatedPoints[0][0], rotatedPoints[1][0]], [rotatedPoints[0][1], rotatedPoints[1][1]], 'k-', label='회전된 선분')

    padding = maxVal * 0.2
    plt.xlim(-maxVal - padding, maxVal + padding)
    plt.ylim(-maxVal - padding, maxVal + padding)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.title(f"2차원 {calType}개 점 회전: {inputTheta}°")
    plt.xlabel("x축")
    plt.ylabel("y축")
    plt.show()