import numpy as np
import matplotlib.pyplot as plt

# TODO readme
# Set initial values
np.random.seed(123)
step = 50
dice = np.random.randint(1, 7)
all_walks = []

for x in range(500):
    random_walk = [0]

    for y in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

np_aw = np.transpose(np.array(all_walks))
finishes = np_aw[-1, :]

ranges = [x * 10 for x in range(0, 12)]

# TODO style the plot
# plt.hist(finishes, bins=10, edgecolor='black', align='left')
# plt.xticks(ranges)
# #plt.hist(finishes)
# plt.show()

plt.hist(finishes)
plt.show()


# TODO style the response
succ_fin = finishes[finishes > 60]
possibility = (np.count_nonzero(finishes >= 60) / 500) * 100
print(str(possibility) + '%')
