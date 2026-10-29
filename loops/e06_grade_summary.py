cont = 0
average = 0
total = 0

for i in range(5):
    num = float(input("Type your grade: "))
    if num >= 0 and num <= 10:
        if num >= 7:
            cont += 1
    total += num

average = total / 5
print(f"The average of the class was {average:.2f}, and over all, {cont} grades were atleast 7")
    
    