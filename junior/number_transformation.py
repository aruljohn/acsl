#
# ACSL Junior Division - Number Transformation - 2019-2020
# Solution by Arul John
# Created: 2020-11-11
# Updated: 2020-12-06

'''
Function to do the number transformations
'''
def number_transformation(n, p, d): # we are passing in N, P, D as arguments/input parameters
    str_n = n       # we will store N as a string
    n = int(n)      # converting n from string to int
    p = int(p)      # converting p from string to int
    d = int(d)      # converting d from string to int
    
    # If the Pth digit position is larger than the number itself, it's a fake number, so quit
    if len(str_n) < p:
        return
    # We will store the final answer in this variable
    str_n_ans = '' # answer

    # i is the index of the Pth digit. We will iterate from left to right
    i = len(str_n) - p

    # pth_digit is the Pth digit. Starting position is the rightmost digit.
    pth_digit = int(str_n[i:i+1])

    ''' Condition (i) which states:
    If the Pth digit of N from the right is from 0 to 4, add D to it. 
    Replace the Pth digit by the units digit of the sum. 
    Then, replace all digits to the right of the Pth digit by 0.
    '''
    if 0 <= pth_digit <= 4:
        pth_new = (pth_digit + d) % 10  # add d to the pth digit and replace with units digit
        str_n_right = str_n[i+1:]       # slice the right side of n and dump into str_n_right
        str_n_ans = str_n[:i] + str(pth_new) + ('0' * len(str_n_right)) # replace all digits on right with 0
    elif 5 <= pth_digit <= 9:
        ''' Condition (ii) which states:
        If the Pth digit of N from the right is from 5 to 9, subtract D from it. 
        Replace the Pth digit by the leftmost digit of the absolute value of the difference.
        Then, replace all digits to the right of the Pth digit by 0.
        '''
        pth_new = int(str(abs(pth_digit - d))[0])  # subtract d from the pth digit
        str_n_right = str_n[i+1:]                  # slice the right side of n and dump into str_n_right
        str_n_ans = str_n[:i] + str(pth_new) + ('0' * len(str_n_right)) # replace all digits on right with 0

    return int(str_n_ans)

# Main
if __name__ == "__main__":
    n, p, d = input().split()
    print(number_transformation(n, p, d))
