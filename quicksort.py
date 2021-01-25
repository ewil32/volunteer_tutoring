"""
Recursive implementation of random quicksort

https://en.wikipedia.org/wiki/Quicksort
"""
import random


def quick_sort(nums):
    """
    Takes a list of numbers and sorts the list so the numbers are in ascending order
    Use quick sort with a random choice for the pivot
    :param nums: a list of real numbers.
    :return: nums_sorted
    """

    # base case nums is empty, so return an emtpy list also
    if len(nums) == 0:
        return []
    # or nums contains one element so return nums
    elif len(nums) == 1:
        return nums

    # choose the pivot index of nums randomly
    pivot_index = random.randint(0, len(nums) - 1)
    pivot_value = nums[pivot_index]

    # seperate the numbers in nums into those less than the pivot value and those greater than or equal to the pivot value
    less_than_pivot = []
    greater_than_pivot = []

    for i in range(len(nums)):
        if i != pivot_index:  # we don't want to include the pivot value
            num = nums[i]
            if num <= pivot_value:
                less_than_pivot.append(num)
            else:
                greater_than_pivot.append(num)

    # use quicksort on the two new lists of numbers
    nums_sorted = quick_sort(less_than_pivot) + [pivot_value] + quick_sort(greater_than_pivot)
    return nums_sorted


# Some testing with edge cases and random lists.
# Use python's built-in sorting function for comparison

if __name__ == "__main__":

    # empty list
    assert quick_sort([]) == []

    # one item
    l = [1]
    assert quick_sort(l) == l

    # 100 random lists of real numbers between -100 and 100 with length between 10 and 10000
    for i in range(100):
        length = random.randint(10, 10000)
        l = [random.randint(-100, 100) for i in range(length)]

        assert quick_sort(l) == sorted(l)

    print("All tests passed")

