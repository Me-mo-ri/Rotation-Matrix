from M1_2d import C2D
from M1_3d import C3D
from rich.console import Console
from rich.rule import Rule
import os

r = Console()

def setup():
    os.system('cls' if os.name == 'nt' else 'clear')
setup()

r.print(Rule("[bold green] 📏 [/bold green]"))
print()
Dim = r.input("[bold green]📏 | Dimension: ")
print()

if Dim in ('2', '2차원', '2D', '2d'):
    r.print(Rule("[bold yellow] in 2nd Dimension ", style="yellow"))
    print()
    C2D()

elif Dim in ('3', '3차원', '3D', '3d'):
    r.print(Rule("[bold yellow] in 3rd Dimension ", style="yellow"))
    print()
    C3D()

else:
    r.print(Rule("[bold red] ❌ | Error: invalidInput - Input must be 2 or 3", style="red"))