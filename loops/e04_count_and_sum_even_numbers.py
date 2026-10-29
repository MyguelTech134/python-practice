total = 0
count = 0
for i in range(1, 7):
    num = int(input("Type in a number: "))
    if num % 2 == 0:
        total += num
        count += 1
print(f"The sum of the even numbers is {total}, and you entered {count} even numbers.")
