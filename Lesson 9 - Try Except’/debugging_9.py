


ATM_BALANCE=500
while True:
    user_input = input("Enter withdrawal amount (or 'exit' to quit): ")
    amount = int(user_input)
    if user_input.lower().strip() == "exit":
        continue
    if amount <= 0:
        print("Invalid amount. Try again.")
        break
    if amount > ATM_BALANCE:
        print("Insufficient funds!")
        continue
    ATM_BALANCE = ATM_BALANCE - amount
    print(f"Withdrawal successful. Remaining balance: {ATM_BALANCE}")
    if ATM_BALANCE == 0:
        print("ATM empty")
        break
   