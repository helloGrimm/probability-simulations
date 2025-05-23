import random
from collections import Counter
import matplotlib.pyplot as plt

def generate_deck() -> list:
    # Create a standard deck of cards with 4 suits and 13 values each
    colors = ['♣', '♠', '♥', '♦']  # Suits: Clubs, Spades, Hearts, Diamonds
    values = list(range(1, 14))  # Card values range from 1 (Ace) to 13 (King)

    deck = []  # Initialize an empty list to store the complete deck of cards
    
    # Generate all possible combinations of values and suits
    for value in values:
        for color in colors:
            deck.append([value, color])  # Add each card as a list [value, suit]
    
    return deck  # Return the complete deck of cards

def is_sucess(hand: list) -> bool:
    # Check if the given hand meets the success condition
    # Success condition: The hand contains exactly 2 cards of one suit 
    # and 1 card each of two other suits.
    color = [card[1] for card in hand]  # Extract the suits of the cards in the hand
    count = Counter(color)  # Count the occurrences of each suit in the hand

    # Return True if the counts match the success condition [1, 1, 2]
    # This means there are two cards of one suit and one card each of two other suits
    return sorted(list(count.values())) == [1, 1, 2]

def simulate(n: int) -> list:
    # Simulate the card drawing process `n` times and calculate the success rate
    deck = generate_deck()  # Generate a standard deck of cards
    sucess_count = 0  # Counter for the number of successful outcomes
    sucess_rates = []  # List to store the success rate after each trial

    # Perform `n` trials
    for trial in range(1, n + 1):  # Use range(1, n+1) because range is exclusive of the upper bound
        hand = random.sample(deck, 4)  # Draw 4 random cards from the deck without replacement
    
        if is_sucess(hand):  # Check if the drawn hand meets the success condition
            sucess_count += 1  # Increment the success counter if the condition is met
        
        # Calculate the success rate (successes so far divided by the number of trials)
        sucess_rates.append(sucess_count / trial)
    
    print(sucess_rates)  # Print the success rates for debugging or analysis
    return sucess_rates  # Return the list of success rates

def draw_plot(sucess_rates: list):
    # Plot the success rates to visualize the Law of Large Numbers
    plt.figure(figsize=(16, 9))  # Set the figure size for the plot

    # Add a title and labels to the plot
    plt.title('Law of Large Numbers - Success in Card Draws', fontsize=14)
    plt.xlabel('Number of Trials', fontsize=12)
    plt.ylabel('Success Frequency k/n', fontsize=12)

    # Add a horizontal line representing the theoretical success rate
    plt.axhline(y=0.584, color='#3E8E9B', linestyle='--', label='Theoretical Value y = 0.584')
    # Plot the simulated success rates
    plt.plot(sucess_rates, color='#A9557E', linewidth=2, label='Simulated Success Frequency')

    plt.legend()  # Add a legend to the plot
    plt.show()  # Display the plot

n = 10000  # Number of simulations to perform
draw_plot(simulate(n))  # Run the simulation and plot the results

# Comments in this code were generated by AI to help better understand the code.
