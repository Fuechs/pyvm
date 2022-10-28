from subprocess import call
from cpu import *
from inst import *
from assembler import Assembler
# from memory import *

clear = lambda: call("clear") 
            
def main() -> None:
    clear()
    with open("src/prog/copy.pvm", 'r') as file:
        source = file.read()
    assembler = Assembler(source)
    del source
    cpu = CPU()
    cpu.mem.writeROM(assembler.read_prog())
    del assembler
    # cpu.mem.debugROM()
    cpu.run()
    # cpu.debug()
    
    
if __name__ == "__main__":
    main()