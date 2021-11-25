class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.first_fix()


    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)


    def first_fix(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1

        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1


    def second_fix(self, other):
        if self.second < other.second:
            self.second += 60
            self.minute -= 1

        if self.minute < other.minute:
            self.minute += 60
            self.hour -= 1


    def add(self, other):
        result = Time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.second = self.second + other.second
        result.first_fix()
        return result


    def sub(self, other):
        result = Time()
        self.second_fix(other)
        result.second = self.second - other.second
        result.minute = self.minute - other.minute
        result.hour = self.hour - other.hour
        return result


    def convert_time_to_sec(self):
        result = self.hour * 3600 + self.minute * 60 + self.second
        return result



def menu():
    print("\n1. Addition of two times")
    print("2. Subtraction of two times")
    print("3. Convert second to time")
    print("4. Convert time to second")
    print("5. Exit")


def get_hour():
    input_hour = int(input("\nPlease enter the hour: "))
    return input_hour


def get_minute():
    input_minute = int(input("Please enter the minute: "))
    return input_minute


def get_second():
    input_second = int(input("Please enter the second: "))
    return input_second


while True:
    menu()
    choice = int(input("--> "))

    if choice == 1:
        first_obj = Time(get_hour(), get_minute(), get_second())
        second_obj = Time(get_hour(), get_minute(), get_second())
        result = first_obj.add(second_obj)
        result.show()

    elif choice == 2:
        first_obj = Time(get_hour(), get_minute(), get_second())
        second_obj = Time(get_hour(), get_minute(), get_second())
        result = first_obj.sub(second_obj)
        result.show()

    elif choice == 3:
        print()
        first_obj = Time(second = get_second())
        first_obj.show()

    elif choice == 4:
       first_obj = Time(get_hour(), get_minute(), get_second())
       print("Total seconds =", first_obj.convert_time_to_sec())

    elif choice == 5:
        break
    
    else:
        print("\nTry again!")