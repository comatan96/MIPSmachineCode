import commands_and_regs as data


class InstructionIdentifier:

    # constructor
    def __init__(self, instruction):
        #splitting the MIPS instruction into registers and command
        #saving the data into the instance variables
        self.instruction = str(instruction).split()
        self.command_format = data.instructions_list[str(self.instruction[0])]['format']
        self.opcode = data.instructions_list[str(self.instruction[0])]['opcode']
        self.command_order = data.instructions_list[str(self.instruction[0])]['order']
        #depending on the command format , initializing  the registers
        if self.command_format == 'R':
            self.r_registers()
            self.funct = data.instructions_list[str(self.instruction[0])]['fun']
        if self.command_format == 'I':
            self.i_registers()

    # to string
    def __str__(self):
        command = ' '.join(self.instruction)
        foramt = "    format: " + str(self.command_format)
        opcode = "    opcode: " + str(self.opcode)
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


    #initiallizing the registers for format R commands
    def r_registers(self):
        if self.command_order == 's':
            self.rs = data.registers.get(data.instructions_list[1],self.instruction[1])
        else:
            self.rd = data.registers.get(data.instructions_list[1],self.instruction[1])
            self.rs = self.instruction[2] if self.command_order == 'dst' else self.instruction[3]
            self.rs = data.registers[self.rs] if self.rs in data.registers else self.rs
            self.rt = self.instruction[3] if self.command_order == 'dst' else self.instruction[2]
            self.rt = data.registers[self.rt] if self.rt in data.registers else self.rt

    #initiallizing the registers for format I commands depends on instruction order
    def i_registers(self):
        if self.command_order == 'offset':
            self.instruction = ' '.join(self.instruction)
            self.instruction = self.instruction.replace('(', ' ')
            self.instruction = self.instruction.replace(')', '')
            print (self.instruction)
            self.instruction = self.instruction.split()
            self.rt = data.registers.get(data.instructions_list[1],self.instruction[1])
            self.imm = data.registers.get(self.instruction[2],self.instruction[2])
            self.rs = data.registers.get(self.instruction[3],self.instruction[3])
        elif (self.command_order == 'branch') or (self.command_order == 'tsi'):
            self.rs = self.instruction[1] if self.command_order == 'branch' else self.instruction[2]
            self.rs = data.registers[self.rs] if self.rs in data.registers else self.rs
            self.rt = self.instruction[2] if self.command_order == 'branch' else self.instruction[1]
            self.rt = data.registers[self.rt] if self.rt in data.registers else self.rt
            self.imm = self.instruction[3]
