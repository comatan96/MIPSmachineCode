import commands_and_regs as data

def bin_sized(dec_num,type_):
    bits_size = data.size[type_]
    num_bin = bin(dec_num)[2:]
    if len(num_bin) < bits_size:
        missing_zeros = bits_size - len(num_bin)
        return ('0'*missing_zeros+num_bin)
    return num_bin

class InstructionIdentifier:

    # constructor
    def __init__(self, instruction):
        #splitting the MIPS instruction into registers and command
        #saving the data into the instance variables
        self.instruction = str(instruction).split()
        try:
            self.command_format = data.instructions_list[str(self.instruction[0])]['format']
            self.opcode = data.instructions_list[str(self.instruction[0])]['opcode']
            self.command_order = data.instructions_list[str(self.instruction[0])]['order']
        except KeyError:
            print("command not recognized")
            return
        #depending on the command format , initializing  the registers
        if self.command_format == 'R':
            self.r_registers()
            self.funct = data.instructions_list[str(self.instruction[0])]['fun']
        if self.command_format == 'I':
            self.i_registers()

    # to string
    def __str__(self):
        command = ' '.join(self.instruction)
        try:
            foramt = "    format: " + str(self.command_format)
        except AttributeError:
            return "ERROR OCCURRED"
        if (self.command_format == 'R') and (self.instruction[0] != 'jr'):
            opcode = "\n\nopcode -> in DEC: " + str(self.opcode) + " in HEX: " +str(hex(self.opcode))
            rd = "    \n\nrd -> in DEC: " + str(self.rd) + " in HEX: " +str(hex(self.rd))
            rt = "    \n\nrt -> in DEC:  " + str(self.rt) + " in HEX: " +str(hex(self.rt))
            rs = "    \n\nrs -> in DEC: " + str(self.rs) + " in HEX: " +str(hex(self.rs))
            funct = "    \n\nfunct -> in DEC: " + str(self.funct) + " in HEX: " +str(hex(self.funct))
            if (self.funct == 0) or (self.funct == 2):
                self.shamt = int(self.instruction[2])
            else:
                self.shamt = 0
            shamt = "    \n\nshamt -> " +bin_sized(self.shamt,'shamt')
            regs = rd + rt + rs + funct + shamt
            #m_code = machine_code('R')
        elif self.command_format == 'I':
            rt = "    rt: " + str(self.rt)
            rs = "    rs: " + str(self.rs)
            imm = "    imm: " + str(self.imm)
            regs = rt + rs + imm
            #m_code = machine_code('I')
        else:
            regs = "    target    " + self.instruction[1] if self.command_format == 'J' else "    rs : " + self.instruction[1]

        return command + ("  -->") + foramt + opcode + regs

    def machine_code_detailed(self):

        if (self.command_format == 'R') and (self.instruction[0] != 'jr'):
            opcode = "\n\nopcode ->  " +bin_sized(self.opcode,'opcode')
            rd = "    \n\nrd -> " +bin_sized(self.rd,'rd')
            rt = "    \n\nrt -> " +bin_sized(self.rt,'rt')
            rs = "    \n\nrs -> " +bin_sized(self.rs,'rs')
            funct = "    \n\nfunct -> " +bin_sized(self.funct,'funct')
            #TODO move shamt to init
            if (self.funct == 0) or (self.funct == 2):
                self.shamt = int(self.instruction[2])
            else:
                self.shamt = 0
            shamt = "    \n\nshamt -> " +bin_sized(self.shamt,'shamt')
            regs = rd + rt + rs + shamt + funct 
            #m_code = machine_code('R')
        elif self.command_format == 'I':
            rt = "    rt: " + bin_sized(self.rt,'rt')
            rs = "    rs: " + bin_sized(self.rs,'rs')
            imm = "    imm: " + bin_sized(self.imm,'imm')
            
            regs = rt + rs + imm
            #m_code = machine_code('I')
        else:
            regs = "    target    " + self.instruction[1] if self.command_format == 'J' else "    rs : " + self.instruction[1]

        return (opcode + regs)

    def machine_code(self):
        if (self.command_format == 'R') and (self.instruction[0] != 'jr'):
            opcode =bin_sized(self.opcode,'opcode')
            rd =bin_sized(self.rd,'rd')
            rt =bin_sized(self.rt,'rt')
            rs =bin_sized(self.rs,'rs')
            funct =bin_sized(self.funct,'funct')
            #TODO move shamt to init
            if (self.funct == 0) or (self.funct == 2):
                self.shamt = int(self.instruction[2])
            else:
                self.shamt = 0
            
            shamt =bin_sized(self.shamt,'shamt')
            regs = rd + rt + rs + shamt + funct 
            #m_code = machine_code('R')
        elif self.command_format == 'I':
            opcode =bin_sized(self.opcode,'opcode')
            rt =bin_sized(self.rt,'rt')
            rs =bin_sized(self.rs,'rs')
            imm =bin_sized(self.imm,'imm')
            
            regs = rt + rs + imm
            #m_code = machine_code('I')
        else:
            opcode = bin_sized(self.opcode,'opcode')
            regs = bin_sized(int(self.instruction[1]),data.size['addr'])

        return (opcode + regs)

    #TODO condsider rtype shift
    #initiallizing the registers for format R commands
    def r_registers(self):
        if self.command_order == 's':
            self.rs = data.registers.get(self.instruction[1], self.instruction[1])
        else:
            self.rd = data.registers.get(self.instruction[1], self.instruction[1])
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
            self.rt = data.registers.get(self.instruction[1], self.instruction[1])
            self.imm = data.registers.get(self.instruction[2], self.instruction[2])
            self.rs = data.registers.get(self.instruction[3], self.instruction[3])
        elif (self.command_order == 'branch') or (self.command_order == 'tsi'):
            self.rs = self.instruction[1] if self.command_order == 'branch' else self.instruction[2]
            self.rs = data.registers[self.rs] if self.rs in data.registers else self.rs
            self.rt = self.instruction[2] if self.command_order == 'branch' else self.instruction[1]
            self.rt = data.registers[self.rt] if self.rt in data.registers else self.rt
            self.imm = self.instruction[3]
