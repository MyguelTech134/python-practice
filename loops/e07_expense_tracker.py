count = total  = highest = 0

while True:
    try:
        expenses = float(input("Type your Expensens to track (type 0 to leave): "))
        if expenses == 0 and count == 0:
            print("No expenses recorded")
            print(count)
            break
        if expenses < 0:
            print("ERROR! Invalid number, please type only positive numbers!")      
    except ValueError:
        print("ERROR! Value not valid, please try again!")
    else:
        if expenses > 0:
            print("Expens addet sucessfully!")
            count += 1
            total += expenses
            if expenses > highest:
                highest = expenses  
        if expenses == 0:
            print(f"count of valid expenses: {count}, total: {total:.2f}, average: {total / count:.2f}, highest: {highest:.2f}")
            print("Come back soon! :)")
            break 



    
    
        

