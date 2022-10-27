from bisect import insort_right
from subprocess import call

clear = lambda: call("clear")

tok_c = -1
def tok() -> int:
    global tok_c
    cur = tok_c
    tok_c += 1
    return cur

NOOP = tok()
HALT = tok()
ADDA = tok()
ADDB = tok()
ADDC = tok()
PUSH = tok()
POPA = tok()


class Instruction:
    def __init__(self, id: int = NOOP) -> None:
        self.id = id
        
    def __repr__(self):
        if   self.id == NOOP:    name = "NOOP"
        elif self.id == HALT:    name = "HALT"
        elif self.id == ADDA:    name = "ADDA"
        elif self.id == ADDB:    name = "ADDB"
        elif self.id == ADDC:    name = "ADDC"
        elif self.id == PUSH:    name = "PUSH"
        elif self.id == POPA:    name = "POPS"

        return f"{name}"

class Memory:
    def __init__(self, size: int = 1024) -> None:
        self.stack: list[int] = []
        self.ram: list[int|None] = [None for i in range(size)]
        self.rom: list[Instruction|int|None] = [None for i in range(size)]

    def writeROM(self, *args) -> None:
        for arg in args:
            for pos, i in enumerate(self.rom):
                if i is None:
                    self.rom[pos] = arg
                    break

    def debugROM(self) -> None:
        print("ROM:", end="")
        for pos, i in enumerate(self.rom):
            if isinstance(i, Instruction):
                print(f"\n{pos} | {i}", end=" ")
            elif i is not None:
                print(i, end=" ")
        print()
    
    def debug(self, rom: bool = False) -> None:
        print("--- Memory ---")
        print("Stack:", self.stack)
        print("RAM:", [i for i in self.ram if i is not None])
        if rom is True: self.debugROM()

class CPU:
    def __init__(self) -> None:
        self.mem = Memory(1024)
        self.pc = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.running = True
        
    def debug(self) -> None:
        self.mem.debug()
        print("A:", self.A)
        print("B:", self.B)
        print("C:", self.C)
        
    def fetchInst(self) -> Instruction:
        if not isinstance(self.mem.rom[self.pc], Instruction):
            print("expected instruction")
            exit(1)
        ret = self.mem.rom[self.pc].id
        self.pc += 1
        return ret
    
    def fetchValue(self):
        if isinstance(self.mem.rom[self.pc], Instruction):
            print("expected value")
            exit(1)
        ret = self.mem.rom[self.pc]
        self.pc += 1
        return ret
    
    def eval(self, id: int):
        if   id == NOOP:    pass
        elif id == HALT:    self.running = False
        elif id == ADDA:    self.A += self.fetchValue()
        elif id == ADDB:    self.B += self.fetchValue()
        elif id == ADDC:    self.C += self.fetchValue()
        elif id == PUSH:    self.mem.stack.append(self.fetchValue())
        elif id == POPA:    self.A = self.mem.stack.pop()
            
    
    def run(self) -> None:
        while self.running is True:
            self.eval(self.fetchInst())  
        print("cpu halted")          
            
def main():
    clear()
    cpu = CPU()
    cpu.mem.writeROM(
        Instruction(PUSH), 1, 
        Instruction(PUSH), 2, 
        Instruction(POPA), 
        Instruction(ADDA), 2,
        Instruction(HALT))
    cpu.mem.debugROM()
    cpu.run()
    cpu.debug()
    
    
if __name__ == "__main__":
    main()