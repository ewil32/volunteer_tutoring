"""
--- SELECTION SORT --- 

The intuition for the algorithm is as follows.
We can divide the list of numbers into a sorted and unsorted part
The sorted part can be incrementally built by finding the smallest number in the unsorted part
and placing it at the tail of the sorted part

I think it is easiest though to build up intuition with an example... 
Let's imagine our list of numbers is L = [3, 4, 2, 1]
Note the list can be named anything but I chose L for List
We imagine the sorted portion of the list is S (S for sorted) which starts empty
and the unsorted part is the entire L
So our initial state is
L = [3, 4, 2, 1]
S = []
S will not actually be another list, but will denote the sorted part of L that we build
I think it's just useful to see to keep track of how much we've sorted

We go through L from position 1 to 4 and find the smallest number 1 at position 4
We swap this number 1 with the number at postion 1 of the list, 3, which gives us
L = [1, 4, 2, 3]
S = [1]
Now L is sorted from position 1 to 1
So we go from postion 2 to 4 and find the smallest number 2 and swap it with the number at position 2
This gives us
L = [1, 2, 4, 3]
S = [1, 2]
Now L is sorted from position 1 to 2
So we go from postion 3 to 4 and find the smallest number 3 and swap it with the number at position 3
This gives us
L = [1, 2, 3, 4]
S = [1, 2, 3]
Since L is sorted from position 1 to 3 and only one number remains, L must be sorted
as we can see above.
L = [1, 2, 3, 4]
S = [1, 2, 3, 4]

So the algorithm can be stated as 
Given a list of numbers L
1. If L is empty, return L immediately 
2. Otherwise set p = 1 (p for position) and set N = the length of L
3. If p = N, we are finished so return L
4. Otherwise find the smallest number in L from p to N
5. swap that number with the number at p
6. Set p = p + 1
7. Go back to step 3

Let's see what this looks like in python
Note that the first position of a list in python is given by 0 not 1
"""


def selection_sort(list_of_numbers):

    # Set N = length of list 
    N = len(list_of_numbers)
    if N == 0:
        return []

    # set p = 0
    p = 0
    
    # while we still have numbers in list_of_numbers
    # note we need -1 here because python starts at 0 not 1 so last position in the list is N-1
    while p < N - 1:

        # find the smallest number in the remaining unsorted part
        # start by assuming it's the number at position p
        smallest_number = list_of_numbers[p]
        smallest_position = p
        
        # then check the rest of the list
        for i in range(p+1, N):
            if list_of_numbers[i] < smallest_number:
                smallest_position = i
                smallest_number = list_of_numbers[i]

        # swap the number at position p with the smallest number
        # we use temp so we don't lose a number
        temp_number = list_of_numbers[smallest_position]
        list_of_numbers[smallest_position] = list_of_numbers[p]
        list_of_numbers[p] = temp_number

        # increase p by one 
        p = p+1

    # the loop has finished so we return list_of_numbers
    return list_of_numbers




"""
---- TEST OUR SORT FUNCTION ----
We will create a function that tries some simple test lists 
Note here that we use += 1 to increment by 1
"""

def selection_sort_test():
    
    print(" --- Testing selection sort --- ")

    # keep track of how many tests are successful and unssuccesful 
    num_tests_passed = 0
    num_tests_failed = 0

    # random order
    test_list = [6,1,8,2,9,4,3,0,5,7]  
    if selection_sort(test_list) == [0,1,2,3,4,5,6,7,8,9]:
        num_tests_passed = num_tests_passed + 1
    else:
        print("Test failed for:", test_list)
        num_tests_failed = num_tests_failed + 1

    # empty list
    test_list = [] 
    if selection_sort(test_list) == []:
        num_tests_passed = num_tests_passed + 1
    else:    
        print("Test failed for:", test_list)
        num_tests_failed = num_tests_failed + 1

    # positive sorted list
    test_list = [1,2,3,4] 
    if selection_sort(test_list) == [1,2,3,4]: 
        num_tests_passed = num_tests_passed + 1
    else:
        print("Test failed for:", test_list)
        num_tests_failed = num_tests_failed + 1

    # only negative
    test_list = [-1,-3,-2,-4] 
    if selection_sort(test_list) == [-4,-3,-2,-1]:
        num_tests_passed = num_tests_passed + 1
    else:
        print("Test failed for:", test_list)
        num_tests_failed = num_tests_failed + 1

    # positive and negative
    test_list = [-1, 1, -2, 2, -3, 3, -4, 4] 
    if selection_sort(test_list) == [-4,-3,-2,-1,1,2,3,4]:
        num_tests_passed = num_tests_passed + 1
    else:    
        print("Test failed for:", test_list) 
        num_tests_failed = num_tests_failed + 1

    # including decimal numbers
    test_list = [1, 0.1, -1] 
    if selection_sort(test_list) == [-1, 0.1, 1]:
        num_tests_passed = num_tests_passed + 1
    else:    
        print("Test failed for:", test_list)
        num_tests_failed = num_tests_failed + 1
    
    print("Number of tests passed:", num_tests_passed)
    print("Number of tests failed:", num_tests_failed)


# --- RUN THE TESTING CODE---
selection_sort_test()
    
