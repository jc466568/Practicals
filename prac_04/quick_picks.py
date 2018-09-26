
import random
picks = int(input("How many quick picks? "))
for pick in range(picks):
    print("{} {} {} {} {} {}".format(random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45), random.
                                     randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45)))
