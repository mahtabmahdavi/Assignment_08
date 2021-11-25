class Complex_Numbers:
    def __init__(self, real = 0, imaginary = 0):
        self.real = real
        self.imaginary = imaginary


    def show(self):
        print(self.real, '+', self.imaginary, 'i')


    def add(self, other):
        result = Complex_Numbers()
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result


    def mul(self, other):
        result = Complex_Numbers()
        result.real = self.real * other.real - self.imaginary * other.imaginary
        result.imaginary = self.real * other.imaginary + self.imaginary * other.real
        return result


    def sub(self, other):
        result = Complex_Numbers()
        result.real = self.real - other.real
        result.imaginary = self.imaginary - other.imaginary
        return result



def menu():
    print("\n1. Addition of two complex numbers")
    print("2. Multiply two complex numbers")
    print("3. Subtraction of two complex numbers")
    print("4. Exit")


def get_real():
    input_real = int(input("\nEnter the real part of your complex number: "))
    return input_real


def get_imaginary():
   input_imaginary = int(input("Enter the imaginary part of your complex number: "))
   return input_imaginary


while True:
    menu()
    choice = int(input("--> "))

    if choice == 1:
        first_obj = Complex_Numbers(get_real(), get_imaginary())
        second_obj = Complex_Numbers(get_real(), get_imaginary())
        result = first_obj.add(second_obj)
        result.show()
    
    elif choice == 2:
        first_obj = Complex_Numbers(get_real(), get_imaginary())
        second_obj = Complex_Numbers(get_real(), get_imaginary())
        result = first_obj.mul(second_obj)
        result.show()

    elif choice == 3:
        first_obj = Complex_Numbers(get_real(), get_imaginary())
        second_obj = Complex_Numbers(get_real(), get_imaginary())
        result = first_obj.sub(second_obj)
        result.show()

    elif choice == 4:
        break
    
    else:
        print("\nTry again!")
