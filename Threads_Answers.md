NAME: AZHARUDDIN HUSSSAINI MOHAMMAD <br />
DATE: 04/08/16 <br />
M20222811 <br />


## 1. Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.
Answer: In thread 1, two threads threadA and thread B are created and are run independently with the processor. Thread2 introduced shared counter which is defined globally and is incremented in both the loops. This helps in understanding the order of execution of both the threads.

## 2. After running Thread3.py does it fix the problems that occurred in Threads2.py? What's the down-side?
Answer: The usage of Locks in ‘Thread3.py’ helps in resolving the issue of waiting time between threads in ‘thread2.py’. The methods Lock.Acquire and Lock.Release helps in locking and unblocking of threads. The down-side of Thread3.py is it takes larger execution time to previous threads.

## 3. Comment out the join statements at the bottom of the program and describe what happens.
The join statements here is wait until both the threads have finished execution as we know that there is switch between threads while execution. Once these join statements are commented,  The execution of main program is finished way before the threads have completed the execution.

## 4. What happens if you try to Ctrl-C out of the program before it terminates?
Answer: It only terminates the main program but threads continue to execute.

## 5. Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.
Answer: ThreadA and ThreadB continue to execute the same ‘that was wierd’. Both the threads are interrupted.

## 6. Does uncommenting the lock operations clear up the problem in question 5?
Answer:  Yes, it avoids thread interrupts.
