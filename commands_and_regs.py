
"""
    offset = rt , offset(rs)
    branch = rs , rt , offset
    instructions mapping
    formats: R , I or J
    opcodes: R = 0 , I & J = documentation codes https://opencores.org/project/plasma/opcodes
    order:   The order of the registers of the instruction
    fun:     Only on R format (opcode 0)
"""
instructions_list = {}
instructions_list['add']   =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 32}
instructions_list['addu']  =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 33}
instructions_list['and']   =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 36}
instructions_list['jr']    =   {'format': 'R', 'opcode': 0,  'order': 's',   'fun': 8}
instructions_list['nor']   =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 39}
instructions_list['or']    =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 37}
instructions_list['slt']   =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 42}
instructions_list['sltu']  =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 43}
instructions_list['sll']   =   {'format': 'R', 'opcode': 0,  'order': 'dts', 'fun': 0}
instructions_list['srl']   =   {'format': 'R', 'opcode': 0,  'order': 'dts', 'fun': 2}
instructions_list['sub']   =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 34}
instructions_list['subu']  =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 35}
instructions_list['xor']   =   {'format': 'R', 'opcode': 0,  'order': 'dst', 'fun': 38}
instructions_list['addi']  =   {'format': 'I', 'opcode': 8,  'order': 'tsi'}
instructions_list['addiu'] =   {'format': 'I', 'opcode': 9,  'order': 'tsi'}
instructions_list['andi']  =   {'format': 'I', 'opcode': 12, 'order': 'tsi'}
instructions_list['beq']   =   {'format': 'I', 'opcode': 4,  'order': 'branch'}
instructions_list['bne']   =   {'format': 'I', 'opcode': 5,  'order': 'branch'}
instructions_list['lb']    =   {'format': 'I', 'opcode': 32, 'order': 'offset'}
instructions_list['lbu']   =   {'format': 'I', 'opcode': 36, 'order': 'offset'}
instructions_list['lhu']   =   {'format': 'I', 'opcode': 37, 'order': 'offset'}
instructions_list['ll']    =   {'format': 'I', 'opcode': 48, 'order': 'tsi'}
instructions_list['lui']   =   {'format': 'I', 'opcode': 15, 'order': 'tsi'}
instructions_list['lw']    =   {'format': 'I', 'opcode': 35, 'order': 'offset'}
instructions_list['ori']   =   {'format': 'I', 'opcode': 13, 'order': 'tsi'}
instructions_list['slti']  =   {'format': 'I', 'opcode': 10, 'order': 'tsi'}
instructions_list['sltiu'] =   {'format': 'I', 'opcode': 11, 'order:': 'tsi'}
instructions_list['sb']    =   {'format': 'I', 'opcode': 40, 'order': 'offset'}
instructions_list['sc']    =   {'format': 'I', 'opcode': 56, 'order': 'offset'}
instructions_list['sh']    =   {'format': 'I', 'opcode': 41, 'order': 'offset'}
instructions_list['sw']    =   {'format': 'I', 'opcode': 43, 'order': 'offset'}
instructions_list['j']     =   {'format': 'J', 'opcode': 2,  'order': 't'}
instructions_list['jal']   =   {'format': 'J', 'opcode': 3,  'order': 't'}


#registers mapper
registers = {
    'zero':0, 'at':1, 'v0':2,
    'v1':3, 'a0':4, 'a1':5,
    'a2':6, 'a3':7, 't0':8,
    't1':9, 't2':10, 't3':11,
    't4':12, 't5':13, 't6':14,
    't7':15, 's0':16, 's1':17,
    's2':18, 's3':19, 's4':20,
    's5':21, 's6':22, 's7':23,
    't8':24, 't9':25, 'k0':26,
    'k1':27, 'gp':28, 'sp':29,
    'fp':30, 'ra':31
}

size = {
    'opcode':6,
    'rt':5,
    'rs':5,
    'rd':5,
    'imm':16,
    'shamt':5,
    'funct':6,
}