from inst import *
from memory import Memory
from error import *

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
        
    def getRegister(self, name: str) -> int:
        if   name == REG_A: return self.A
        elif name == REG_B: return self.B 
        elif name == REG_C: return self.C
    
    def setRegister(self, name: str, value: int) -> None:
        if   name == REG_A: self.A = value
        elif name == REG_B: self.B = value
        elif name == REG_C: self.C = value 
                
    def fetchInst(self) -> Instruction:
        if not isinstance(self.mem.rom[self.pc], Instruction):
            throw("expected instruction", self.pc)
        ret = self.mem.rom[self.pc].id
        self.pc += 1
        return ret
    
    def fetchValue(self) -> int:
        if not isinstance(self.mem.rom[self.pc], Value):
            throw("expected value", self.pc)
        ret = self.mem.rom[self.pc].value
        self.pc += 1
        return ret

    def fetchRegister(self) -> str:
        if not isinstance(self.mem.rom[self.pc], Register):
            throw("expected register", self.pc)
        ret = self.mem.rom[self.pc].name
        self.pc += 1
        return ret
    
    def eval(self, id: int) -> None:
        
        if   id == NOOP:    pass
        elif id == HALT:    self.running = False
        
        elif id == ADDS:    self.mem.stack.append(self.mem.stack.pop()+self.mem.stack.pop())
        elif id == SUBS:    
            a = self.mem.stack.pop()
            b = self.mem.stack.pop()
            self.mem.stack.append(b-a)
        
        elif id == ADDR: 
            reg = self.fetchRegister()
            val = self.fetchValue()
            self.setRegister(reg, self.getRegister(reg)+val)
        elif id == SUBR: 
            reg = self.fetchRegister()
            val = self.fetchValue()
            self.setRegister(reg, self.getRegister(reg)-val)
        
        elif id == PUSH:    self.mem.stack.append(self.fetchValue())
        elif id == POPR:    self.setRegister(self.fetchRegister(), self.mem.stack.pop())
        
        elif id == OUTS:    print(self.mem.stack.pop())
        elif id == OUTI:    print(self.fetchValue())
        elif id == OUTR:    print(self.getRegister(self.fetchRegister()))
        
        elif id == COPY:    self.setRegister(value=self.getRegister(self.fetchRegister()), name=self.fetchRegister())
                        
    
    def run(self) -> None:
        print("\n-- Output --")
        while self.running is True:
            self.eval(self.fetchInst())  
        print("-- Output --\n")