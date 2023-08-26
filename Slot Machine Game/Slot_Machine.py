import random

# Constants for gameplay
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1 

ROWS = 3 
COLS = 3

# Define the counts and values of different symbols
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}

symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,
}

# Function to check winnings on each line
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines 

# Function to simulate a slot machine spin
def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
             
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]

        for _ in  range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns 

# Function to print the slot machine output
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(f" {column[row]} ", end=" | ")
            else:
                print(f" {column[row]} ", end="")
        print()

# Function to get the initial deposit amount
def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")

    return amount 

# Function to get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

# Function to get the bet amount
def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? ${MIN_BET} - ${MAX_BET}: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount 

# Function to simulate the spin of the slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"Insufficient balance to place a bet. Your current balance is ${balance}")
        else: 
            break

    print(f"You are betting ${bet} on {lines} line{'s' if lines > 1 else ''}. Your total bet is ${total_bet}.")

    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print("\nSpinning the slot machine...\n")
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    
    if winnings > 0:
        print(f"Congratulations! You won ${winnings}!")
        print(f"You won on line{'s' if len(winning_lines) > 1 else ''}: {', '.join(map(str, winning_lines))}")
    else:
        print("Sorry, you didn't win this time.")

    return winnings - total_bet

# Main game loop
def main():
    balance = deposit()

    while True:
        print(f"Your current balance is ${balance}")
        spin_status = input("Press Enter to spin or 'q' to quit: ").lower()
        if spin_status == "q":
            break
        balance += spin(balance)

        print(f"You have ${balance} remaining")

# Entry point of the program
if __name__ == "__main__":
    main()
