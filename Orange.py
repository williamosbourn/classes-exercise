import random
import math

def random_number_gen():
  return math.floor(random.random() * (300 - 100) + 200) / 100


class Orange:
    def __init__(self):
      self.diameter = random_number_gen()

