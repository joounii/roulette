import random

def roulette_spin():
    # European roulette has numbers from 0 to 36
    number = random.randint(0, 36)
    # Define the colors for the roulette numbers
    color = 'green' if number == 0 else 'red' if number in (
        1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
    ) else 'black'
    return number, color

def calculate_payout(bet_type, bet_value, spin_number, spin_color):
    # Determine win or loss based on bet type
    if bet_type == 'number':
        if bet_value == spin_number:
            return 35  # 35 to 1 payout
    elif bet_type == 'color':
        if bet_value == spin_color:
            return 1  # 1 to 1 payout
    elif bet_type == 'parity':
        if (bet_value == 'even' and spin_number % 2 == 0 and spin_number != 0) or \
           (bet_value == 'odd' and spin_number % 2 != 0):
            return 1  # 1 to 1 payout
    return -1  # Lost the bet

def main():
    print("Welcome to the Roulette Game!")
    print("You can bet on a 'number' (0-36), 'color' (red/black), or 'parity' (odd/even).")

    # Place bet type
    bet_type = input("Enter bet type (number/color/parity): ").strip().lower()

    # Get bet value based on bet type
    if bet_type == 'number':
        bet_value = int(input("Enter a number to bet on (0-36): "))
        if bet_value < 0 or bet_value > 36:
            print("Invalid number! Must be between 0 and 36.")
            return
    elif bet_type == 'color':
        bet_value = input("Enter a color to bet on (red/black): ").strip().lower()
        if bet_value not in ('red', 'black'):
            print("Invalid color! Must be 'red' or 'black'.")
            return
    elif bet_type == 'parity':
        bet_value = input("Enter parity to bet on (odd/even): ").strip().lower()
        if bet_value not in ('odd', 'even'):
            print("Invalid parity! Must be 'odd' or 'even'.")
            return
    else:
        print("Invalid bet type!")
        return

    # Place bet amount
    bet_amount = int(input("Enter your bet amount: "))

    # Spin the roulette wheel
    spin_number, spin_color = roulette_spin()
    print(f"\nThe roulette spins... and lands on {spin_number} ({spin_color})!")

    # Calculate payout
    payout_multiplier = calculate_payout(bet_type, bet_value, spin_number, spin_color)
    winnings = bet_amount * payout_multiplier

    # Display result
    if payout_multiplier > 0:
        print(f"Congratulations! You won {winnings} units.")
    else:
        print(f"Sorry, you lost your bet of {bet_amount} units.")

# Run the game
main()
