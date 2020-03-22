import re
class NegativeNumber(Exception):
    pass

def Add(num):
    if num == "":
        return ""
    else:
        num, delimiter = get_delimiter(num)
        num_list = get_num_list(num, delimiter)
        check_negatives(num_list)
        return crosssum(num_list)

def get_delimiter(num):
    delimiter = ",|\n"
    if starts_with_new_delimiter(num):
        delimiter = num.splitlines()[0][-1]
        return num.splitlines()[1], delimiter
    return num, delimiter

def starts_with_new_delimiter(num):
    return num[:2] == "//"

def check_negatives(num_list):
    negatives = [n for n in num_list if n < 0]
    if len(negatives) > 0:
        raise NegativeNumber("Negatives not allowed:", repr([n for n in negatives]))

def get_num_list(num, delimiter):
    return [int(n) for n in re.split(delimiter, num)]

def crosssum(num_list):
    crosssum = 0
    for n in num_list:
        crosssum += n if n < 1001 else 0
    return crosssum

print(Add(""))
print(Add("//p\n1p2"))
print(Add("1"))
print(Add("10,2,5,22,1,1"))
print(Add("1\n 2"))
print(Add("-1,2"))

