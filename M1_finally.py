from M1_2d import C2D
from rich.console import Console
from rich.rule import Rule
import os

r = Console()

def setup():
    os.system('cls' if os.name == 'nt' else 'clear')
setup()

r.print(Rule("[bold green] 📏 in 2nd Dimension [/bold green]"))
print()
C2D()