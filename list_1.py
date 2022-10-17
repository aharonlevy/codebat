'''
this is the solutions for 'warmup-2' entry of codebat.com
'''

def first_last6(nums):
    '''
    Given an array of ints, return True if 6 appears as either the first or last element in the array.
    The array will be length 1 or more.
    '''
    # check if the first or last elemnt is 6
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    '''
    Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal
    '''
    # check if the array length is at least one and if the first and last elemnts in the array are the same
    return (len(nums) >= 1) and (nums[0] == nums[-1])