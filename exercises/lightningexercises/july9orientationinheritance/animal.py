class Animal():
  def __init__(self, species, leg_num=0, domesticated=False):
    self.species = species
    self.leg_num = leg_num
    self.domesticated = domesticated

  def saySomething(self):
    if self.species == "dog":
      return "'woof woof!'"
    else:
      return "moosqueakrrrrrchirp"