import random


class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return f"MSDie({self.num_sides}) : {self.current_value}"


my_die = MSDie(6)

for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)
