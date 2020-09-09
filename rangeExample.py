#!/usr/bin/env python3

# import PyMP library
import pymp

# this program demonstrates the use of parallel range
# using parallel range the numbers of the range are split across threads
# to more clearly demonstrate what's going on you can comment out the
# standard range and the p.range sections to see how they differ
def main():
    """
    main function for when running as a script
    """

    with pymp.Parallel() as p:
        listOfNumsRange = []

        # each thread gets the same range 0-16
        for number in range(0, 16):
            listOfNumsRange.append(number)
        print(f'List of numbers that thread {p.thread_num} got from range {listOfNumsRange}')

        listOfNumsParRange = []
        # each thread gets a seperate part of the range
        for number in p.range(0, 16):
            listOfNumsParRange.append(number)

        print(f'List of numbers that thread {p.thread_num} got from parallel range {listOfNumsParRange}')
    
if __name__ == '__main__':
    # execute only if run as a script
    main()
