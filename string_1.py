'''
this is the solutions for 'string-1' entry of codebat.com
'''

def hello_name(name):
    '''
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
    '''
    return f"Hello {name}!"
    #this solution will not work on the site but f-string is a valid way

def make_abba(word_a, word_b):
    '''
    Given two strings, a and b, return the result
     of putting them together in the order abba,
      e.g. "Hi" and "Bye" returns "HiByeByeHi".
    '''
    return word_a + (word_b*2) + word_a

def make_tags(tag, word):
    '''
    The web is built with HTML strings like "<i>Yay</i>"
     which draws Yay as italic text. In this example, the "i" tag makes
    <i> and </i> which surround the word "Yay".
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
    '''
    start_tag = "<" + tag + ">"
    end_tag = "</" + tag + ">"
    return start_tag + word + end_tag

def make_out_word(out, word):
    '''
    Given an "out" string length 4, such as "<<>>",
    and a word, return a new string where the word is
    in the middle of the out string, e.g. "<<word>>".
    '''
    start_out = out[:len(out)/2]
    end_out = out[len(out)/2:]
    return start_out + word + end_out

def extra_end(string):
    '''
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
    The string length will be at least 2.
    '''
    return string[-2:]*3

def first_two(string):
    '''
    Given a string, return the string made of its first two chars,
     so the String "Hello" yields "He". If the string is shorter than length 2,
    return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
    '''
    if len(string)<2:
        return string
    return string[0:2]

def first_half(string):
    '''
    Given a string of even length, return the first half.
    So the string "WooHoo" yields "Woo".
    '''
    return string[0: len(string)/2]

def without_end(string):
    '''
    Given a string, return a version without the first and last char, so "Hello" yields "ell".
    The string length will be at least 2.
    '''
    #starting from index 1 will cut the first letter and until -1 will cut the last letter
    return string[1:-1]

def combo_string(string_a, string_b):
    '''
    Given 2 strings, string_a and string_b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).
    '''
    if len(string_a)< len(string_b): #checking if string_a is shorter
        return string_a + string_b + string_a
    #string_b is shorter
    return string_b + string_a + string_b