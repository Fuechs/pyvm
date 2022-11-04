from inst import *
# from memory import memoize

class Assembler:
    def __init__(self, source: str) -> None:
        self.source = source
        self.length = len(source)
        self.idx = 0        
    
    def check(self) -> bool:
        return self.idx < self.length
    
    def get_token(self):
                
        if not self.check(): return
        
        if self.source[self.idx].isalpha():
            value = self.source[self.idx]
            self.idx += 1
            while self.check() and self.source[self.idx].isalpha():
                value += self.source[self.idx]
                self.idx += 1
            return str_to_inst(value)
        
        elif self.source[self.idx] == '#':
            value = ""
            self.idx += 1
            while self.check() and self.source[self.idx].isdigit():
                value += self.source[self.idx]
                self.idx += 1
            return Value(int(value))

        elif self.source[self.idx] == '$':
            self.idx += 1
            value = '$'+self.source[self.idx]
            self.idx += 1
            return Register(value)

        elif self.source[self.idx].isspace(): 
            self.idx += 1
            return self.get_token()
        
            
    def read_prog(self) -> list:
        prog = []
        while self.check():
            prog.append(self.get_token())
        return prog