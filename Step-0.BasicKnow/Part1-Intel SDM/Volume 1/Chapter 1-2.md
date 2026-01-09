Date: 2026.01.05 14:24
Base: Chaoyang,Beijing
Theme: The note about Chapter 1 and 2
***
## 1x0 Foreword

Firstly, it introduces some processors which covered in this manual. It's number looks seem so many. So I ignore and look a second. 

Then, shows the overview of the volume 1. In the later of this volumn, I find it always call me to program with different processor architectures. But so clear that I don't have so many different processors and computer. So I will pay attention to the general-purpose things. 

And at least of chapter 1, we could learn some knowledges about the notational conventions which the Intel are using. After this, you can see some related literature are listed by this book. Go to website and enjoy the warm of knowledge.

Then at chapter 2, we will learn the history of Intel 64 and IA-32 Architectures. But I think it is unessional for student, none want to exam you the history of Intel.
## 2x0 Content

### 2x1 Bit and Byte Order
The main things what I think we should remember is the notational conventions. Look at the figure 1-1 below:
![Pasted image 20260105144109](D:\APT\Step-0\Intel64 SDM\photos\Pasted image 20260105144109.png)
This is bit and byte order, address raises from the bottom to the top. Bit raises from the right to the left. Intel 64 and IA-32 processors are "little endian" mechines, so the bytes of a word are numbered starting from the least significant byte.

### 2x2 Reserved Bits and software compatibility

To adapt the update of processor, it will always reserve some bits to adapt new capbility.
And also, compatibility is a essential reason. So while we developping the software, don't believe reserved bits and don't depend on its stores and states. If you want to operate the reserved bits, you should copy it and use register replace it. 

### 2x3 Instruction Operands

	label:mnemonic argument1,argument2,argument3

For that centence, I think we should only remember that mnemonic is a reserved name to operate the processor to process arguments that the number of argument have 3 the most.
And the number of argument depend on the mnemonic.
For example, `LOADREG:MOV EAX,SUBTOTAL`, In this case, we can find it only have two arguments. EAX is the destination operand and SUBTOTAL is the source operand.

### 2x4 Hexadecimal and Binary

We all know hexadecimal (16) contains 0~9,A~F. And use 'H' as the tail of number to present its number system.
Next, binary (2) have only 0 and 1，sometimes followed by 'B' .

### 2x5 Segmented Addressing
	Segment-register:Byte-address
For example, `DS:FF79H`, is data segment and adderess of that byte.
`CS:EIP`, is code segment and the EIP register contians the address of the instruction.

### 2x6 A Syntax for CPUID,CR,MSR Values

![Pasted image 20260105154102](D:\APT\Step-0\Intel64 SDM\photos\Pasted image 20260105154102.png)


## 3x0 The Last
However, this is only a head of study. There will have so many trobules and difficults are waitting for us, but don't need to worry. They will become the rocks to contined for your road.