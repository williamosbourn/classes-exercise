class OrangeTree:
  # Trees should start at the age of 0. 
  # Trees should start at a height of 0.
  def __init__(self):
    self.age = 0
    self.height = 0


  # Each growing season.
  # A tree should age one year.
  # A tree should grow 2.5 feet taller until it reaches its maximum height, say 25 feet.
  # A tree should bear fruit if it is mature ( at least six years old )
  #     Between 100 and 300 oranges of fruit. 
  # All oranges from the previous year drop off the tree. 
  def pass_growing_season(self):
    self.age += 1
    self.height += 2.5
    if self.height > 25:
      self.height = 25


  # Checks if a tree is old enough to bear fruit ( at least 6 years )
  def is_mature(self):
    return self.age >= 6


  # Add instance method: has_oranges() which returns whether or not a tree has any oranges on it.
  def has_oranges(self):
    pass

  # Should pick an orange of a tree and return it.
  # Or throw an error if there are no oranges.
  def harvest_orange(self):
    pass

  def __str__(self):
    return 'OrangeTree age={0}, height={1}'.format(self.age, self.height)