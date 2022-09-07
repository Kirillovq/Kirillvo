num = int(input("введите число" ))
list_of_digits = [ ]
for b in str(num):
    list_of_digits.append(int(b))
print(max(list_of_digits))