'''
this is the solutions for 'warmup-2' entry of codebat.com
'''

def first_last6(nums):
    '''
    Given an array of ints, return True if 6 appears as either the first or
     last element in the array.
    The array will be length 1 or more.
    '''
    # check if the first or last elemnt is 6
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    '''
    Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal
    '''
    # check if the array length is at least one and if the first
    # and last elemnts in the array are the same
    return (len(nums) >= 1) and (nums[0] == nums[-1])

def make_pi():
    '''
    Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
    '''
    return [3, 1, 4]

def common_end(nums_a, nums_b):
    '''
    Given 2 arrays of ints, nums_a and nums_b,
    return True if they have the same first element
    or they have the same last element.
    Both arrays will be length 1 or more.
    '''
    return nums_a[0] == nums_b[0] or nums_a[-1] == nums_b[-1]

def sum3(nums):
    '''
    Given an array of ints length 3, return the sum of all the elements.
    '''
    total = 0
    for number in nums:
        total += number
    return total
