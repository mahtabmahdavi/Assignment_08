class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator

        if denominator != 0:
            self.denominator = denominator
        else:
            self.denominator = 1
        

    def show(self):
        print(self.numerator, '/', self.denominator)


    def add(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result


    def mul(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result


    def sub(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator - self.denominator * other.numerator
        result.denominator = self.denominator * other.denominator
        return result


    def div(self, other):
        result = Fraction()
        result.numerator = self.numerator * other.denominator
        result.denominator = self.denominator * other.numerator
        return result


    def simplify(self):
        common_factor = 1

        for i in range(min(abs(self.numerator), abs(self.denominator)), 1, -1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                common_factor = i
                break

        result = Fraction()
        result.numerator = int(self.numerator /common_factor)
        result.denominator = int(self.denominator /common_factor)
        return result



def menu():
    print("\n1. Addition of two fractions")
    print("2. Multiply two fractions")
    print("3. Subtraction of two fractions")
    print("4. Divide into two fractions")
    print("5. Fraction simplification")
    print("6. Exit")


def get_numerator():
    input_numerator = int(input("\nEnter the numerator of your fraction: "))
    return input_numerator


def get_denominator():
    input_denominator = int(input("Enter the denominator of your fraction: "))

    while input_denominator == 0:
        print("\nZero is invalid for the denominator.")
        input_denominator = int(input("Enter the denominator of your fraction: "))

    return input_denominator


while True:
    menu()
    choice = int(input("--> "))

    if choice == 1:
        first_obj = Fraction(get_numerator(), get_denominator())
        second_obj = Fraction(get_numerator(), get_denominator())
        result = first_obj.add(second_obj)
        result.show()
    
    elif choice == 2:
        first_obj = Fraction(get_numerator(), get_denominator())
        second_obj = Fraction(get_numerator(), get_denominator())
        result = first_obj.mul(second_obj)
        result.show()

    elif choice == 3:
        first_obj = Fraction(get_numerator(), get_denominator())
        second_obj = Fraction(get_numerator(), get_denominator())
        result = first_obj.sub(second_obj)
        result.show()

    elif choice == 4:
        first_obj = Fraction(get_numerator(), get_denominator())
        second_obj = Fraction(get_numerator(), get_denominator())
        result = first_obj.div(second_obj)
        result.show()

    elif choice == 5:
        first_obj = Fraction(get_numerator(), get_denominator())
        result = first_obj.simplify()
        result.show()

    elif choice == 6:
        break
    
    else:
        print("\nTry again!")