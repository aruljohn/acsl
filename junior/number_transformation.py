#!env python

#
# ACSL Junior Division - Number Transformation - 2019-2020
# Solution by Arul John
# 2020-11-11
#

# Function to do the number transformations
def number_transformation(n, p, d):
    str_n = n
    n = int(n)
    p = int(p)
    d = int(d)
    if len(str_n) < p:
        return
    str_n_ans = '' # answer

    # index of the Pth digit
    i = len(str_n) - p

    # Pth digit
    pth_digit = int(str_n[i:i+1])
    if 0 <= pth_digit <= 4:
        pth_new = (pth_digit + d) % 10
        str_n_right = str_n[i+1:]
        str_n_ans = str_n[:i] + str(pth_new) + ('0' * len(str_n_right))
    elif 5 <= pth_digit <= 9:
        pth_new = int(str(abs(pth_digit - d))[0])
        str_n_right = str_n[i+1:]
        str_n_ans = str_n[:i] + str(pth_new) + ('0' * len(str_n_right))

    return int(str_n_ans)

# Tests
def test_number_transformation():
    test_data = [('124987 2 3', 124950),
                 ('540670 3 9', 540300),
                 ('7145042 2 8', 7145020),
                 ('124987 2 523', 124950),
                 ('4386709 1 2', 4386707),
                 ('4318762 4 3', 4315000),
                 ('72431685 1 7', 72431682),
                 ('123456789 7 8', 121000000),
                 ('9876543210 10 25', 1000000000),
                 ('314159265358 8 428', 314140000000)
                ]
    for test_input, answer in test_data:
        testlist = test_input.split(' ')
        assert number_transformation(*testlist) == answer

# Main
if __name__ == "__main__":
    test_number_transformation()

    n, p, d = input().split()
    print(number_transformation(n, p, d))

