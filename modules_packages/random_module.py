import random

# random.seed(0)

# for _ in range(5):
#     print(random.random(), end=' ')

# choice takes random values from the given choices
# It doesn't care if the value is already picked or not
print(random.choice([1, 2, 3, 4]))

# sample takes random values from the given choices without duplication
# It won't pick the same values twice
# You can't set the limit greater than or equal to the choices length
print(random.sample([1, 2, 3, 4], 2))