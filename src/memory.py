from inst import Instruction

class Memory:
    def __init__(self, size: int = 1024) -> None:
        self.stack: list[int] = []
        # unused for now
        # self.ram: list[int|None] = [None for i in range(size)]
        self.rom: list[Instruction|int|None] = [None for i in range(size)] 

    def writeROM(self, prog: list) -> None:
        for i, stmt in enumerate(prog):
            self.rom[i] = stmt

    def debugROM(self) -> None:
        print("ROM:", end="")
        for pos, i in enumerate(self.rom):
            if isinstance(i, Instruction):
                print(f"\n{pos:04d} | {i}", end=" ")
            elif i is not None:
                print(i, end=" ")
        print()
    
    def debug(self, rom: bool = False) -> None:
        print("--- Memory ---")
        print("Stack:", self.stack)
        # print("RAM:", [i for i in self.ram if i is not None])
        if rom is True: self.debugROM()     