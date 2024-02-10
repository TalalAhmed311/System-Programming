Segmentation Fault Issue
If you encounter a "Segmentation fault (core dumped)" error while running the program, it indicates that the program is attempting to access restricted or invalid memory. This error often occurs when dereferencing null pointers, accessing unallocated memory, or trying to modify protected memory regions.

Possible Reasons:
Invalid Memory Access:

The specified memory address might not be accessible or may not belong to your program.
Memory Protection:

Certain memory regions are protected by the operating system, and attempting to modify them can result in a segmentation fault.
Address Alignment Issues:

The address you're trying to access might not be aligned correctly for the type of data you're trying to modify.
