import fractions


class Fractions():
    fraction1 = fractions.Fraction(numerator=1, denominator=2)
    fraction2 = fractions.Fraction(numerator=1, denominator=4)
    fract_add = fraction1 + fraction2
    print(fraction1)
    print(fraction2)
    print('Standart fract add')
    print(fract_add)
    print(float(fract_add))

    fraction4 = fractions.Fraction(numerator=-11, denominator=5)
    fraction5 = fractions.Fraction(numerator=12, denominator=8)
    fraction6 = fraction4 + fraction5
    print(('Fractions - add'))
    print(fraction6)
    print(float(fraction6))

    fraction7 = fractions.Fraction(numerator=1, denominator=4)
    fraction8 = fractions.Fraction(numerator=2, denominator=5)
    fraction_multiply = fraction7 * fraction8
    print('Fraction multiply')
    print(fraction_multiply)

    fraction9 = fractions.Fraction(numerator=12, denominator=33)
    fraction10 = fractions.Fraction(numerator=4, denominator=39)
    fraction_divide = fraction9 / fraction10
    print('Fraaction divide')
    print(fraction_divide)


Fractions()