

Chapter 2 Review Questions
Name: Azharuddin Hussaini Mohammad
Course: 5143 Operating Systems
Date: 16 Feb 2016

## What are three objectives of an OS design?
*The three main objectives of an OS design are:
*Convenience: Operating System makes the system more convenient to use.
*Efficiency: Efficient in terms of utilizing the available computer system resources
*Ability to evolve: An OS should be constructed in such a way as to permit the effective development, testing, and introduction of new                     system functions without interfering with service.

## What is the kernel of an OS?
A kernel is the core component of an operating system. Using interprocess communication and system calls, it acts as a bridge between applications and the data processing performed at the hardware level.

When an operating system is loaded into memory, the kernel loads first and remains in memory until the operating system is shut down again. The kernel is responsible for low-level tasks such as disk management, task management and memory management.

## What is multiprogramming?
Multiprogramming in Operating system is a form of parallel processing in which two or more programs are run at the same time on a single processor.

It can also be referred as multitasking.
Memory is expanded to hold three, four or more programs and switch among all of them.

## What is a process?
•	A Process can be defined as a program in execution.
•	The entity that can be assigned to and executed on a processor.

##	How is the execution context of a process used by the OS?
Contains the process elements
Created and manage by the operating system
Allows support for multiple processes

## List and briefly explain five storage management responsibilities of a typical OS.
The five principal storage management responsibilities are:
Process Isolation: Should prevent independent processes from accessing with each other’s memory, both data and instructions.

Automatic allocation and management: This is the process whereby allocation should be transported to the programmer.
Support of Modular Programming: Supports the program to be able to define programs modules and to create, destroy and alter the size of modules dynamically
Protection and access control: This is the process of sharing memory this is desirable when sharing is needed by a particular application it also threatens the integrity of programs.
Long-term storage: Is a process whereby memory is stored for a long period of time even when the computer is switch off it is stored in the RAM.

## Explain the distinction between a real address and a virtual address.
Real Address/ Physical Address refer to hardware addresses of physical memory.
Physical addressing means that your program actually knows the real layout of RAM. When you access a variable at address 0x8746b3, that's where it's really stored in the physical RAM chips.
With virtual addressing, all application memory accesses go to a page table, which then maps from the virtual to the physical address. So every application has its own "private" address space, and no program can read or write to another program's memory. This is called segmentation.

## Describe the round-robin scheduling technique.
Round Robin scheduling technique is one of the oldest and widely used algorithm, in this technique processes are dispatched in a FIFO manner but are given a limited amount of CPU time called a time-slice or a quantum.
If a process does not complete before its CPU-time expires, the CPU is preempted and given to the next process waiting in a queue. The preempted process is then placed at the back of the ready list.
Round Robin Scheduling is preemptive (at the end of time-slice) therefore it is effective in time-sharing environments in which the system needs to guarantee reasonable response times for interactive users.
The only interesting issue with round robin scheme is the length of the quantum. Setting the quantum too short causes too many context switches and lower the CPU efficiency. On the other hand, setting the quantum too long may cause poor response time and appoximates FCFS.

## Explain the difference between a monolithic kernel and a microkernel.
Monolithic Kernel
Monolithic kernel is a single large process running entirely in a single address space.
It is a single static binary file. All kernel services execute in the same kernel address space. 
Examples of monolithic kernel based Oss are Unix, Linux.
Microkernel
In microkernel, the kernel is broken down into separate processes, known as servers. 
Some of the servers run in kernel space and some run in user-space. All servers are kept separate and run in different address spaces. Servers invoke "services" from each other by sending messages via IPC (Interprocess Communication). This separation has the advantage that if one server fails, other servers can still work efficiently. 
Examples of microkernel based OSs: Mac OS X and Windows NT.

## What is multithreading?
Multithreading is the ability of a program or an operating system process to manage its use by more than one user at a time and to even manage multiple requests by the same user without having to have multiple copies of the programming running in the computer.


##	List the key design issues for an SMP operating system.
Simultaneous concurrent processes or threads: Kernel routines need to be reentrant to allow several processors to execute the same kernel code simultaneously.
Scheduling: Scheduling may be performed by any processor, so conflicts must be avoided
Synchronization: With multiple active processes having potential access to shared address spaces or shared I/O resources, care must be taken to provide effective synchronization
Memory Management: Memory management on a multiprocessor must deal with all of the issues found on uniprocessor machines. There is a problem with the cache memories: Cache memories contain image of a portion of main memory. If a processor changes the contents of the main memory, these changes have to be recorded in the cache memories that contain an image of that portion of memory. This is known as cache coherence problem and is typically solved in hardware.
Reliability and fault tolerance: The operating system should provide graceful degradation in the face of processor failure
