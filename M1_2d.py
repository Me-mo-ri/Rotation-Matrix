from rich.console import Console
from rich.rule import Rule
import numpy as np
import matplotlib.pyplot as plt
from sympy import E

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
        ordered_pair_str = r.input(f"[bold green]🔢 | {prompt_text}: [/bold green]")
        try:
            parts = ordered_pair_str.strip().replace('A(', '').replace(')', '').split(',')
            
            if len(parts) != 2:
              r.print(Rule(f"[bold red] ❌ | Error: {Exception}", style="red"))
            
            x_val = float(parts[0].strip())
            y_val = float(parts[1].strip())
            return x_val, y_val
        except Exception as e:
            r.print(Rule(f"[bold red] ❌ | Error: {e} [/bold red]", style="red"))

def C2D():
    r.print(Rule("[bold green] 📏 2차원 시뮬레이션 [/bold green]", style="green"))
    r.print()

    while True:
        try:
            cal_type = int(r.input("[bold green]📏 | Numbers: [/bold green]"))
            if cal_type >= 1:
                break
        except Exception as e:
            r.print(Rule(f"[bold red] ❌ | Error: {e}[/bold red]", style="red"))

    messages = {
        1: "One point in 2nd Dimension",
        2: "Two points in 2nd Dimension",
        3: "Three points in 2nd Dimension",
        4: "Four points in 2nd Dimension",
    }

    r.print(Rule(f"[bold yellow] {messages[cal_type]} [/bold yellow]", style="yellow"))
    r.print()
 
    while True:
        theta_str = r.input("[bold green]📐 | Rotation : [/bold green]")
        try:
            common_theta = float(theta_str)
            break
        except Exception as e:
            r.print(Rule(f"[bold red] ❌ | Error: {e} [/bold red]", style="red"))

    all_original_points = []
    all_rotated_points = []

    for i in range(cal_type):
        r.print(f"\n[cyan]----- {i+1}번째 점 입력 ----- [/cyan]")
        
        original_x, original_y = getOrderedPair(f"점 {chr(65+i)}") 
        
        X, Y = calPointRotation(
            original_x, original_y, common_theta
        )
        
        all_original_points.append((original_x, original_y))
        all_rotated_points.append((X, Y))

        r.print(f"[green]원본 점 {chr(65+i)}: ([bold]{original_x:.2f}[/bold], [bold]{original_y:.2f}[/bold])[/green]")
        r.print(f"[green]회전된 점 {chr(65+i)}: ([bold]{X:.2f}[/bold], [bold]{Y:.2f}[/bold])[/green]")

    plt.figure(figsize=(8, 8))
    max_val = 0

    for i in range(cal_type):
        orig_x, orig_y = all_original_points[i]
        rot_x, rot_y = all_rotated_points[i]
        
        colors = ['red', 'blue', 'green', 'purple']
        point_color = colors[i % len(colors)]

        plt.plot(orig_x, orig_y, 'o', color=point_color, markersize=8, label=f'원본 {chr(65+i)}')
        plt.plot(rot_x, rot_y, 'X', color=point_color, markersize=8, label=f'회전 {chr(65+i)}')
        
        plt.plot([0, orig_x], [0, orig_y], '--', color=point_color, alpha=0.6)
        plt.plot([0, rot_x], [0, rot_y], '-', color=point_color, alpha=0.8)

        max_val = max(max_val, abs(orig_x), abs(orig_y), abs(rot_x), abs(rot_y))

    padding = max_val * 0.2
    plt.xlim(-max_val - padding, max_val + padding)
    plt.ylim(-max_val - padding, max_val + padding)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.title(f"2차원 {cal_type}개 점 회전: {common_theta}°")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()