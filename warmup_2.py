

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