def test(a_list):
    temp = a_list[1:].copy()
    for i in range(len(temp)):
        temp[i] = ord(temp[i])
    print(temp)
    return a_list


a_list = ['a', 'b', 'c']

print("str")
test(a_list)
print()
print("int")
print(a_list)
