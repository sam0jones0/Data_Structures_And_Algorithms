class Fraction:
    """Class modelling a fraction."""

    def __init__(self, top, bottom):
        """Constructor definition."""
        self.num = top
        self.den = bottom

    def __str__(self):
        """Builds fraction as a string."""
        return f"{self.num}/{self.den}"

    def __float__(self):
        """Returns fraction as float."""
        return float(self.num / self.den)

    def __eq__(self, other_fraction):
        """Returns True if the two fractions are equal."""
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __gt__(self, other_fraction):
        """Returns True if this fraction is greater than the other."""
        first_num = self.num / self.den
        second_num = other_fraction.num / other_fraction.den

        return first_num > second_num

    def __lt__(self, other_fraction):
        """Returns True if this fraction is less than the other."""
        first_num = self.num / self.den
        second_num = other_fraction.num / other_fraction.den

        return first_num < second_num

    def __add__(self, other_fraction):
        """Adds this fraction to another."""
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common_den = gcd(new_num, new_den)

        return Fraction(new_num // common_den, new_den // common_den)

    def __sub__(self, other_fraction):
        """Subtracts another fraction from this one."""
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common_den = gcd(new_num, new_den)

        return Fraction(new_num // common_den, new_den // common_den)

    def __mul__(self, other_fraction):
        """Multiplies this fraction to another."""
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common_den = gcd(new_num, new_den)

        return Fraction(new_num // common_den, new_den // common_den)

    def __truediv__(self, other_fraction):
        """Divides this fraction by another."""
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common_den = gcd(new_num, new_den)

        return Fraction(new_num // common_den, new_den // common_den)


def gcd(m, n):
    """Returns greatest common denominator between two integers."""
    while m % n != 0:
        m, n = n, m % n
    return n
