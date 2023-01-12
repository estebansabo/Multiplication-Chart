user_number = int(input("What number would you like to multiply? "))

if user_number < 1:
    user_number = 1

print(f"!!!! Multiplication chart of the number {user_number} !!!!")

for table_number in range(1, 11):

    if user_number == 12:
        print("I can't show this!")
        break

    print(f"{user_number} x {table_number} = {user_number*table_number}")
else: 
    print("Finish")