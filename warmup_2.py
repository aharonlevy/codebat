
def string_times(words, num):
    ''''
    Given a string and a non-negative int n,
     return a larger string that is n copies of the original string.
    '''
    return words*num

def front_times(string, num):
    ''' 
Given a string and a non-negative int n, we'll say that the
front of the string is the first 3 chars, or whatever is there
 if the string is less than length 3. Return n copies of the front;
'''
    if len(string) < 3:
        return string*num
    return string[0:3]*num

def string_bits(string):
    '''
    Given a string, return a new string made of every other char
     starting with the first, so "Hello" yields "Hlo".
    '''
    return string[::2]

def string_splosion(string):
    '''
    Given a non-empty string like "Code" return a string like "CCoCodCode"
    '''
    counter = 0
    sopolation=""
    while counter<len(string)-1:    #we loop through every word bit exept the full word and add it everytime
        sopolation += string[0:counter+1]
        counter += 1
    return sopolation +string

def last2(string):
    '''    
    Given a string, return the count of the number of times that
    a substring length 2 appears in the string and also as the
    last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
    '''
    check_string = string[len(string)-2::]
    char_index=0
    target_string_counter=0
    while char_index < len(string)-2:
        quarry_string = string[char_index:char_index+2]
        if quarry_string == check_string:
            target_string_counter +=1
        char_index +=1
    return target_string_counter

def array_count9(nums):
    '''
    Given an array of ints, return the number of 9's in the array.
    '''
    nine = 9
    nines_counter = 0
    for number in nums:
        if number == nine:
            nines_counter +=1
    return nines_counter
    
def array_front9(nums):
    '''
    Given an array of ints, return True if one of
    the first 4 elements in the array is a 9.
     The array length may be less than 4.
    '''
    index_pointer = 0
    while index_pointer < 4 and index_pointer < len(nums):
        if nums[index_pointer] == 9:
            return True
        index_pointer += 1
    return False