start: add $a0, $s0, $s1
       beq $s0, $s1, exit
       sll $s0, $s1, 2
       bgez $s0, start
       j start
exit: