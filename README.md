###Features

- Support MIPS assembly

# OTTER MIPS

![otter](https://github.com/comatan96/OTTERmips/blob/master/otter%20mips.png)



**Table of Contents**

###FlowChart

```flow
st=>start: Enter MIPS instruction
op=>operation: breaking the instruction into pieces
cond=>condition: valid instruction?
e=>end: returns the machine code of the instruction

st->op->cond
cond(yes)->e
cond(no)->st
```
