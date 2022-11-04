from colorama import Fore as c

colors = [
    "",         # 0
    c.WHITE,    # 1
    c.RED,      # 2
    c.BLUE,     # 3
    c.GREEN,    # 4
    c.YELLOW    # 5
]

class Screen:
    
    def __init__(self, title: str = "Screen", width: int = 20, height: int = 10) -> None:
        self.title = title
        self.width = width
        self.height = height
        self.content = [[0 for y in range(width)] for x in range(height)]
        self.color = colors[1]
    
    def draw(self):
        print("-- "+self.title+" --")
        for y in self.content:
            for x in y:
                if x == 0: print(" ", end="")
                elif x == 1: print(self.color+"▀"+c.RESET, end="")
            print()
        print("-"*(6+len(self.title)))