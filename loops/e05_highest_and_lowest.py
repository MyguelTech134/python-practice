highest = 0
lowest = 0

for i in range(1, 6):
    num = int(input("Type in a number: "))
    if i == 1:
        highest = num
        lowest = num 
    else:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

print(f"The highest number typed where {highest}, while the lowest number typed where {lowest}")