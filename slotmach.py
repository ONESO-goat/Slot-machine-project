
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
  while True: 
    #amount = int(input("What would you like to deposit? $ \n"))
    amount = input("What would you like to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please a number")
  return amount

def get_number_of_lines():
  while True:
    line= input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
    if line.isdigit():
      line = int(line)
      if 1 <= line <= MAX_LINES:
        break
      else:
        print("Enter valid number of lines")
    else:
      print("Please enter a number")
  return line

def get_bet():
  while True: 
    bet = input("How many bets from " + str(MIN_BET) + " to " + str(MAX_BET) + "? ")
    if bet.isdigit():
      bet = int(bet)
      if bet > 0 and bet < 100:
        break
      else:
        print("Amount must be between the required amount.")
    else:
      print("Please a number")
  return bet

def main():
  balance = deposit()
  line = get_number_of_lines()
  bet = get_bet()
  print(balance, line, bet)
  

main()













#def music():
