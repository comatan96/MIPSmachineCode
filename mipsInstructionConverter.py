
import commands_and_regs as instructions

class InstructionIdentifier:

#constructor
    def __init__(self, instruction):
        self.instruction = str(instruction).split()
        self.command_format = instructions.instructions_list[str(self.instruction[0])]['format']
        self.opcode = instructions.instructions_list[str(self.instruction[0])]['opcode']
        self.command_order = instructions.instructions_list[str(self.instruction[0])]['order']
        if self.command_format == 'R' :
            self.r_registers()
            self.funct = instructions.instructions_list[str(self.instruction[0])]['fun']
        if self.command_format == 'I':
            self.i_registers()



    def __str__(self):
        command = ' '.join(self.instruction)
        foramt = "    format: " + str(self.command_format)
        opcode = "    opcode: " + str(self.opcode)
        command_order = str(self.command_order)
        if (self.command_format == 'R') and (self.instruction[0] != 'jr'):
            rd = "    rd: " + str(self.rd)
            rt = "    rt: " + str(self.rt)
            rs = "    rs: " + str(self.rs)
            funct = "    funct: " + str(self.funct)
            regs = rd + rt + rs + funct
        elif self.command_format == 'I':
            rt = "    rt: " + str(self.rt)
            rs = "    rs: " + str(self.rs)
            imm = "    imm: " + str(self.imm)
            regs = rt + rs + imm
        else:
            regs = "    target    " + self.instruction[1] if self.command_format == 'J' else "    rs : " + self.instruction[1]
            
        return command + ("    -->    ") + foramt + opcode + regs


    def r_registers(self):
        if self.command_order == 's':
            self.rs = instructions.registers[self.instruction[1]] if self.instruction[1] in instructions.registers else self.instruction[1] 
        else:
            self.rd = instructions.registers[self.instruction[1]] if self.instruction[1] in instructions.registers else self.instruction[1]
            self.rs = self.instruction[2] if self.command_order == 'dst' else self.instruction[3]
            self.rs = instructions.registers[self.rs] if self.rs in instructions.registers else self.rs
            self.rt = self.instruction[3] if self.command_order == 'dst' else self.instruction[2]
            self.rt = instructions.registers[self.rt] if self.rt in instructions.registers else self.rt

    def i_registers(self):
        if self.command_order == 'offset':
            self.instruction = ' '.join(self.instruction)
            self.instruction = self.instruction.replace('(', ' ')
            self.instruction = self.instruction.replace(')', '')
            print (self.instruction)
            self.instruction = self.instruction.split()
            self.rt = instructions.registers[self.instruction[1]] if self.instruction[1] in instructions.registers else self.instruction[1]
            self.imm = instructions.registers[self.instruction[2]] if self.instruction[2] in instructions.registers else self.instruction[2]
            self.rs = instructions.registers[self.instruction[3]] if self.instruction[3] in instructions.registers else self.instruction[3]
        elif (self.command_order == 'branch') or (self.command_order == 'tsi'):
            self.rs = self.instruction[1] if self.command_order == 'branch' else self.instruction[2]
            self.rs = instructions.registers[self.rs] if self.rs in instructions.registers else self.rs
            self.rt = self.instruction[2] if self.command_order == 'branch' else self.instruction[1]
            self.rt = instructions.registers[self.rt] if self.rt in instructions.registers else self.rt
            self.imm = self.instruction[3]

