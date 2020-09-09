#!/usr/bin/env python3

import pymp


def main():
    """
    main function for when running as a script
    """

    # two lists of numbers
    listOfNumsA = [num for num in range(0,10)]
    listOfNumsB = [num for num in range(0,10)]

    sums = [0 for i in range(len(listOfNumsA))]
    sharedSums = pymp.shared.list(sums) # sharedSums = [x for x in sums]

    # alternatively you could do this
    #
    # empty list
    # sharedSums = pymp.shared.list()
    # for i in range( len(listOfNumsA) ):
    #   sharedSums.append(0)

    
    with pymp.Parallel() as p:
        #split indices across threads
        for index in p.range( len(listOfNumsA) ):
            sharedSums[index] = listOfNumsA[index] + listOfNumsB[index]

        # uncomment to see the work the individual threads did
        # print(f'Summed list for thread {p.thread_num} {sharedSums}')
    print(f'Summed list {sharedSums}')
            
    
if __name__ == '__main__':
    # execute only if run as a script
    main()
