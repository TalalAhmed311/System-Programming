# Silly Attempt to modify memory of another program

```
gcc -g -o program program.c
gdb ./program
```
It will run your program in debugger mode.

When you enter the gdb terminal attach breakpoint on line 8
```
break program.c:8

run
```

To check local variables info 
```
info locals
```
To check the memory address of a variable
```
p &myNymber
```
Copy the address and paste it into modify.c and run the program
```
gcc -o modify modify.c
./modify
```


## Segmentation Fault Issue
If you encounter a "Segmentation fault (core dumped)" error while running the program, it indicates that the program is attempting to access restricted or invalid memory. This error often occurs when dereferencing null pointers, accessing unallocated memory, or trying to modify protected memory regions.

### Possible Reasons:

1. Invalid Memory Access:
   
   The specified memory address might not be accessible or may not belong to your program.

3. Memory Protection:

   Certain memory regions are protected by the operating system, and attempting to modify them can result in a segmentation fault.

3. Address Alignment Issues:

   The address you're trying to access might not be aligned correctly for the type of data you're trying to modify.


#### Resouce:

https://en.wikipedia.org/wiki/Segmentation_fault
