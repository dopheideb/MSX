#!/usr/bin/env python3

import disasm
import logging
import sys
import z80

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    show_callees = True
    show_routines = True
    dasm = disasm.Disasm(sys.argv[1])
    dasm.add_routine(0x4685, 'CLUELESS_FOR_NOW')
    
    output = dasm.run('branch all')
    #output = dasm.run('linear')
    for PC in sorted(output.keys()):
        try:
            routine_name = dasm.get_routine(PC)
            if show_routines:
                print(f"; Start of routine {routine_name}.")
        except KeyError:
            pass
        
        try:
            show_from = False
            
            num_froms = len(output[PC]['from'])
            if num_froms > 1:
                show_from = True
            elif num_froms == 1:
                only_key = next(iter(output[PC]['from']))
                if output[PC]['from'][only_key] != 'fall through':
                    show_from = True
            
            if show_from and show_callees:
                print(f";")
                print(f";")
                print(f";")
                print(f"; We can get here from:")
                for i in sorted(output[PC]['from'].keys()):
                    print(f";   0x{i:04X} {output[PC]['from'][i]}")
        except NotImplementedError:
            pass
        print(f"{output[PC]['disasm']}")
