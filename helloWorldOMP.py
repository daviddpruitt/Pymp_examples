#!/usr/bin/env python3

# import the PyMP library
import pymp

# simple PyMP hello world program
# you can run this with varying numbers of threads
# with the command:
# OMP_NUM_THREADS=<number of threads> python3 ./helloWorldOMP.py
def main():

    # start a parallel section
    with pymp.Parallel() as p:
        
        # print the thread number and number of threads
        # p.thread_num is the current thread number
        # p.num_threads is the total number of threads in the set
        print(f'Hello from thread {p.thread_num} of {p.num_threads}')

if __name__ == '__main__':
        # execute only if run as a script
        main()
