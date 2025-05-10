# Krsytian Pietrzyk
import random
from collections import Counter
import matplotlib.pyplot as plt

def generate_deck () -> list:
    # 4 kolory, 13 wartości każdy
    colors = ['♣', '♠', '♥', '♦']
    values = list(range(1, 14)) # losujemy liczby z zakresu od 1 do 13, jako wartości dla naszych ['♣', '♠', '♥', '♦']

    deck = [] # zmienna przechowująca naszą talię kart
    
    for value in values:
        for color in colors:
            deck.append((value, color)) # dodajemy do naszej tali wartości wraz z ich kolorami
    
    return deck

def is_sucess (hand: list):
    color = [card[1] for card in hand]
    count = Counter(color)

    # Jeżeli waruenk jest spełniony, zwracamy wartość True
    return sorted(list(count.values())) == [1, 1, 2]

def simulate (n: int) -> float:
    deck = generate_deck() # nasza talia
    sucess_count = 0 # ilość sukcesów
    sucess_rates = list()

    for _ in range(1, n+1): # musimy +1 ponieważ funkcja range() jest otwarta prawostronnie, czyli kiedy było by n, to by go nie uwzględniało 
        hand = random.sample(deck, 4)
    
        if is_sucess(hand): # if wykonan się jeżeli is_sucess() zwróci True, czyli kiedy waruenk zostanie spełniony
            sucess_count += 1
        
        sucess_rates.append(sucess_count / _)
    
    print(sucess_rates)
    return sucess_rates
    

def draw_plot (sucess_rates: float):
    plt.figure(figsize=(16, 9))

    plt.title('Prawo Wielkich Liczb - Sukces w losowaniu kart', fontsize=14)
    plt.xlabel('Liczba prób', fontsize=12)
    plt.ylabel('Częstość sukcesu k/n', fontsize=12)

    plt.axhline(y=0.584, color='#3E8E9B', linestyle='--', label='Wartość teoretyczna y = 0,584')
    plt.plot(sucess_rates, color='#A9557E', linewidth=2, label='Symulowana częstość sukcesu')

    plt.legend()    
    plt.show()

n = 10 # liczba wykonywanych symulacji 
draw_plot(simulate(n))