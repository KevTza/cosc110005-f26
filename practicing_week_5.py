'''
for count in range(1, 21):
    print(count)
for count in range(1, 21, 2):
    print(count)
x = True
while x:
    min_value = int(input("Enter the minimum value: "))
    if min_value in range(1, 21):
        print("Wonderhoy.")
    else:
        continue
    max_value = int(input("Enter the maximum value: "))
    if max_value in range(1, 21) and max_value >= min_value:
        print("Wonderhoy.")
        x = False
    else:
        continue
for count in range(min_value, max_value):
    print(count)
'''

''' 
for chr in ("Kevin"):
    print(chr)
for chr in ["F", "W", "O", "M", "P"]:
    print(chr)
'''

'''
Matrix:
'''
list1 = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
]

list1  ([2],[2])

# for innerlist in list1:
#     for num in innerlist:
#         print(num)
