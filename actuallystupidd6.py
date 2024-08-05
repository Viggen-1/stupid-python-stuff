import random

def biased_d6():
    # 90% chance to land on 1
    if random.random() < 0.9:
        return 1
    else:
        # 10% chance to land on 2, 3, 4, 5, or 6
        return random.choice([2, 3, 4, 5, 6])

# Roll the biased die once and print the result
print("Biased d6 roll result:", biased_d6())
