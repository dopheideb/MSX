import disasm
import logging
import sys
import z80

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    dasm = disasm.Disasm(sys.argv[1])
    #dasm.add_routine(0x0056, 'FILVRM')
    dasm.add_routine(0x403B, 'HL+=a')
    dasm.add_routine(0x4685, 'GEENIDEE')
    
    output = dasm.run()
    for PC in sorted(output.keys()):
        try:
            routine_name = dasm.get_routine(PC)
            logging.info(f"; Start of routine {routine_name}.")
        except KeyError:
            pass
        
        logging.info(f"{PC:04X} : {output[PC]}")
