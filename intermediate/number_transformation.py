#!env python

#
# ACSL Intermediate Division - Number Transformation - 2019-2020
# Solution by Arul John
# 2020-11-22
#

# Function to do the number transformations
def number_transformation(n, p):
    str_n = n
    n = int(n)
    p = int(p)
    if len(str_n) < p:
        return
    str_n_ans = '' # answer

    # index of the Pth digit
    i = len(str_n) - p

    # Pth digit
    pth_digit = int(str_n[i:i+1])
    str_n_right = str_n[i+1:]
    str_n_left = str_n[:i]
    for c in str_n_left:
        str_n_ans += str((int(c) + pth_digit) % 10)
    str_n_ans += str(pth_digit)
    for c in str_n_right:
        str_n_ans += str(abs(int(c) - pth_digit))
    return int(str_n_ans)

# Tests
def test_number_transformation():
    test_data = [('296351 5', 193648),
                 ('762184 3', 873173),
                 ('45873216 7', 95322341),
                 ('19750418 6', 86727361),
                 ('386257914 5', 831752441)
                ]
    for test_input, answer in test_data:
        testlist = test_input.split(' ')
        assert number_transformation(*testlist) == answer

# Main
if __name__ == "__main__":
    test_number_transformation()

    n, p = input().split()
    print(number_transformation(n, p))
