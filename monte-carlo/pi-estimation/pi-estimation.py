import matplotlib.pyplot as plt
import numpy as np

def MC_simulation (n: int):
    global inside, outside

    while outside < n:
        # generujemy losowe liczy z przedziału [0, 1)
        x = np.random.uniform(0.0, 1.0)
        y = np.random.uniform(0.0, 1.0)

        outside += 1 # Liczba współrzędnych w kwadracie

        # Sprawdzamy nasz warunek:
        # True: dodajemy współrzędne do naszego koła 
        # False: dodajemy współrzędne do naszego kwadratu
        if (x**2 + y**2 < 1):
            x_circle.append(x)
            y_circle.append(y)

            inside += 1 # Liczba współrzędnych w kółku
        else: 
            x_square.append(x)
            y_square.append(y)

def graph (xC, yC, xS, yS, n):
    plt.title(f'Wyznaczanie Pi metodą Monte Carlo, n = {n}')
    
    # Tworzenie koła o promieniu: r = 1
    ax = plt.subplot()

    # Ustawiamy graniczne wartości naszego wykresu
    ax.set_xlim((0, 1))
    ax.set_ylim((0, 1))
    
    # Tworzenie wykresu dla punktów znajdujących się w środku koła
    plt.scatter(xC, yC, color = '#3E8E9B')
    plt.scatter(xS, yS, color = '#A9557E')
    circle = plt.Circle((0, 0), 1, fill = False, linestyle='dashed', color = '#3D3939')

    ax.add_artist(circle)

    # Automatyczne zapisyawnie wykresu
    # plt.savefig('plot.png', dpi = 1000, bbox_inches = 'tight')

    # Wyświetlanie wykresu
    plt.show()
    

# Zmienne przechowujące ilość punktów w środku okręgu {inside} i poza nim {outside} 
inside = 0
outside = 0

# Zmienne odpowiedzialne za przechowywanie współrzędnych x i y, które spełniają warunek: x^2 + y^2 < 1
x_circle = []
y_circle = []

# Zmienne odpowiedzalne za przechowywanie współrzędnych x i y, które nie spełniają warunku: x^2 + y^2 < 1
x_square = []
y_square = []

# n = 0 # Wprowadzanie z góry wartości ~ pominięcie wprowadzenia przez konsolę 
n = int(input('Ilość losowanych par [n]: ')) # Ilość losowanych par ~ wprowadzane przez uytkowanika

MC_simulation (n)
graph(x_circle, y_circle, x_square, y_square, n)
print(f'\nPrzyblienie PI: {4 * (inside / n)}\n')
