import numpy as np
import matplotlib.pyplot as plt

# Set initial values (seed for random, empty list for all walks)
np.random.seed(123)
all_walks = []

# Trying to play 500 times
for x in range(500):
    random_walk = [0]

    # 100 die throws
    for y in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        # Point addition decision-making
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # Returning to 0 check
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Preparing data (transpose - switch rows with cols, selecting only last points)
np_aw = np.transpose(np.array(all_walks))
finishes = np_aw[-1, :]

# Probability calculation
possibility = round((np.count_nonzero(finishes >= 60) / 500) * 100, 2)

# Plotting the
font = {'size': 11}

plt.hist(finishes, bins=10, edgecolor='black')
plt.title('Final points and their occurrences', loc='left', fontdict=font)
plt.title('Probability of win: ' + str(possibility) + '%', loc='right', fontdict=font)
plt.xlabel("Count of final points")
plt.ylabel("Occurrences")
plt.show()
