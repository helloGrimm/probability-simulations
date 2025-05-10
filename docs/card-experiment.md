# Law of Large Numbers

### Author: Krystian Pietrzyk  
### Date: 23.04.2025  

## 1. Objective

The goal of this experiment is to conduct a Monte Carlo simulation in the context of drawing cards from a 52-card deck. Success is defined as drawing two cards of the same color and the other two being of different colors. We will then compare the simulation results with theoretical probability to illustrate the Law of Large Numbers.

## 2. Theoretical Background

The Law of Large Numbers states that as the number of independent trials increases, the observed average value approaches the theoretical value. In this case, the experiment involves drawing four cards from a deck. Success is defined as:

1. Exactly two cards of the same color.
2. The remaining two cards must be of different colors and distinct from the color of the pair.

We do not group black suits (♣, ♠) or red suits (♥, ♦); instead, we treat each suit as a separate color.

### Examples of success:
- ♣♣♥♦
- ♥♥♠♣

### Examples of failure:
- ♦♦♦♠
- ♥♥♣♣

## 3. Analytical Calculations

### Number of possible arrangements:
Drawing 4 cards from a deck of 52 without replacement:



\[
|Ω| = \frac{52!}{4!(52-4)!} = 270725
\]



### Choosing colors:
Selecting one color for the pair (4 choices) and two other different colors from the remaining three (3 choices).



\[
\text{Number of color combinations} = 4 \times C(3,2) = 4 \times 3 = 12
\]



### Selecting cards:
- **Pair of one color:** \(C(13,2) = 78\)
- **Remaining two cards (one from each of the other colors):** \(C(13,1) = 13\)

Total number of successful outcomes:



\[
12 \times 78 \times 13 \times 13 = 158184
\]



### Probability of success:



\[
P(success) = \frac{158184}{270725} \approx 0.584
\]



## 4. Description of Functions Used

To draw cards, we used the `sample()` method from the `random` library. For analyzing color distribution, we used `Counter()` from `collections`, which helped classify each trial.

To visualize simulation results, we used `matplotlib.pyplot` to plot success frequencies stabilizing as the number of trials increased.

## 5. Simulation Results

### For n = 10:

| Trial Number | Success Rate |
|-------------|-------------|
| 1           | 1.00        |
| 2           | 0.50        |
| 3           | 0.33        |
| 4           | 0.25        |
| 5           | 0.40        |
| 6           | 0.50        |
| 7           | 0.43        |
| 8           | 0.50        |
| 9           | 0.56        |
| 10          | 0.60        |

For a small number of trials, the result is unstable and deviates from the theoretical value.

### For n = 1000:
The success frequencies stabilize and approach the theoretical 0.584.

### For n = 100000:
The result almost exactly matches the theoretical value, confirming the Law of Large Numbers.

## 6. Summary

The simulation demonstrated the Law of Large Numbers: the more trials conducted, the closer the observed result approaches the expected probability. With a high number of trials, the graph of success frequencies stabilizes and approaches the theoretical probability.

---

