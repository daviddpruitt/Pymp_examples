#!/usr/bin/env python3

import pymp


# Example of iterating over a list in parallel
# The parallel code will iterate over a list of letters and
# add the letters to a dictionary where the key is the thread
# number. One example output is
# 0 : []
# 3 : ['AAA', 'CCC', 'EEE', 'GGG']
# 2 : ['BB', 'DD', 'FF', 'HH']
# 1 : []
# The individual elements of the iteration
# are spread out across threads in a non-deterministic
# manner. Running this multiple times will give
# different results.
def dictOfItems(itemsToIterate=[]):

    # creates a shared dictionary where we store
    # the lists
    sharedDict = pymp.shared.dict()
    
    with pymp.Parallel() as p:
        # the strings for this thread
        listOfItems = []
 
        # iterate over the list of strings
        # using standard iteration (for item in itemsToIterate)
        # each thread would work the entire list resulting in duplicates
        # with parallel iterate they each get a portion of the list
        for item in p.iterate(itemsToIterate):
            # for each item take that item and
            # add thread_num of these to the dict
            listOfItems.append(item * (p.thread_num + 1))

        # add the list to the dict
        sharedDict[p.thread_num] = listOfItems

    return sharedDict
        
def main():
    """
    main function for when running as a script
    """

    itemsToIterate = ['A', 'B', 'C', 'D',
                      'E', 'F', 'G', 'H']
    lists = dictOfItems(itemsToIterate)

    for list in lists:
        print(f'{list} : {lists[list]}')
    
if __name__ == '__main__':
    # execute only if run as a script
    main()

