

def sleep_in(weekday, vacation):
    '''
    the function determane if we should sleep in or not.
    we sleep in if it's not a weekday or when we are on a vacation
    args:
    weekday- a boolean will be set as true if it's a weekday
    vacation- a boolean will be set as true if we are in a vacation
    return:
    true if we should sleep in false if we should'nt
    '''
    return (not weekday) or vacation
def monkey_trouble(a_smile, b_smile):
    '''
    the function determane if we are in truble,
     we are in trouble if both monkeys are smiling or not smiling
    args:
    a_smile- a bool indicate if 'monkey a' is smiling 
    b_smile- a bool indicate if 'monkey b' is smiling
    return:
    the function return true if we are in trouble
    '''
    return (a_smile and b_smile) or (not a_smile and not b_smile)

def sum_double(num_a, num_b):
    '''
    the function will return the sum of 'a' and 'b' unless a and b are the same
    then the function will double the sum
    '''
    if num_a == num_b:
        return 2*(num_a+num_b)
    return num_a+num_b

def diff21(num):
    '''
    the function returns the absolute difference between n and 21
    if 'num' is bigger then 21 it will return double the difference 
    '''
    if num < 21:
        return abs(21-num)
    return  2*abs(21-num)

def parrot_trouble(talking, hour):
    '''
    We have a loud talking parrot. The "hour" parameter is the
    current hour time in the range 0..23.
        We are in trouble if the parrot is talking and the hour
    is before 7 or after 20.
        Return True if we are in trouble.
    '''
    return talking and (hour<7 or hour>20)

def makes10(num_a, num_b):
    '''
    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
    '''
    return num_a==10 or num_b==10 or num_a+num_b==10

def near_hundred(num):
    '''
    Given an int num, return True if it is within 10 of 100 or 200.
     Note: abs(num) computes the absolute value of a number.
    '''
    return abs(num-100)<=10 or abs(num-200)<=10

def pos_neg(a, b, negative):
    '''
    Given 2 int values, return True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only if both are negative.
    '''
    if negative:
        return a<0 and b<0
    else:
        return (a<0 and b>0) or (a>0 and b<0)

def not_string(sentence):
    '''
    Given a string, return a new string 
    where "not " has been added to the front.
    However, if the string already begins with "not",
    return the string unchanged.
    '''
    mask_check="not"
    if sentence[0: len(mask_check)]==mask_check:
        return sentence
    return mask_check + " " + sentence
    