def add(num):
    if num == "":
        return ""

    else:
        num_list = get_num_list(num)
        return crosssum(num_list)

def get_num_list(num):
    return [int(n) for n in num.split(",")]

def crosssum(num_list):
    crosssum = 0
    for n in range(len(num_list)):
        crosssum += num_list[n]
    return crosssum

print(add("1,2"))
print(add("1"))
print(add("10,2,5,22,1,1"))
