tok_c = -1
def tok() -> int:
    global tok_c
    cur = tok_c
    tok_c += 1
    return cur

NOOP = tok()
HALT = tok()
ADDS = tok()
SUBS = tok()
ADDR = tok()
SUBR = tok()
PUSH = tok()
POPR = tok()
OUTS = tok()
OUTI = tok()
OUTR = tok()
COPY = tok()

def inst_to_str(inst: int) -> str:
    if   inst == NOOP:  return "NOOP"
    elif inst == HALT:  return "HALT"
    elif inst == ADDS:  return "ADDS"
    elif inst == SUBS:  return "SUBS"
    elif inst == ADDR:  return "ADDR"
    elif inst == SUBR:  return "SUBR"
    elif inst == PUSH:  return "PUSH"
    elif inst == POPR:  return "POPR"
    elif inst == OUTS:  return "OUTS"
    elif inst == OUTI:  return "OUTI"
    elif inst == OUTR:  return "OUTR"
    elif inst == COPY:  return "COPY"


REG_A = "$A"
REG_B = "$B"
REG_C = "$C"


class Instruction:
    def __init__(self, id: int = NOOP) -> None:
        self.id = id
        
    def __repr__(self) -> str:
        return inst_to_str(self.id)

def str_to_inst(inst: str) -> Instruction:
    if   inst == "NOOP": return Instruction(NOOP)
    elif inst == "HALT": return Instruction(HALT)
    elif inst == "ADDS": return Instruction(ADDS)
    elif inst == "SUBS": return Instruction(SUBS)
    elif inst == "ADDR": return Instruction(ADDR)
    elif inst == "SUBR": return Instruction(SUBR)
    elif inst == "PUSH": return Instruction(PUSH)
    elif inst == "POPR": return Instruction(POPR)
    elif inst == "OUTS": return Instruction(OUTS)
    elif inst == "OUTI": return Instruction(OUTI)
    elif inst == "OUTR": return Instruction(OUTR)
    elif inst == "COPY": return Instruction(COPY)
    
class Value:
    def __init__(self, value: int = 0) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f"#{self.value}"
        
class Register:
    def __init__(self, name: str = REG_A) -> None:
        self.name = name
        
    def __repr__(self) -> str:
        return self.name