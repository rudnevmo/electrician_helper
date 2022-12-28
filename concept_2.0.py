import dictionary as d


class CrossSectionalArea:
    def __init__(self, value):
        self.__value = value
        self.__copper_amperage_220 = d.COPPER_AMPERAGE_220
        self.__copper_capacity_220 = d.COPPER_CAPACITY_220

    def __get_value(self):
        return f"{self.__value} мм2"

    def __str__(self):
        return self.__get_value()


class AbstractVoltage:
    pass


class CopperAmperage220:
    def __init__(self):
        self.__amperage = d.COPPER_AMPERAGE_220

    def __str__(self):
        return

    def get_amperage(self, value):
        if value not in self.__amperage.keys():
            self.get_amperage_value(value)
        return self.__amperage.keys(value)

    def get_amperage_value(self, value):
        try:
            while value not in self.__amperage.keys() and value <= max(self.__amperage):
                value += 1
                round(value, 1)
                return value
        except IndexError:
            print(f"{value}: невідповідне значення")


class Electrician:
    def __init__(self):
        self.input_ = input("Введіть значення: ")

    def check_input(self):
        try:
            self.input_ = abs(float(self.input_))
        except ValueError:
            print(f'ValueError: {self.input_} невірне значення')
        else:
            return self.input_


v = CopperAmperage220()
electrician = Electrician()
print(v.get_amperage(electrician.check_input()))
'''
class CopperVoltage220:
    def __init__(self):
        self.__amperage = list(c.COPPER_AMPERAGE_220)
        self.__capacity = list(c.COPPER_CAPACITY_220)


class CopperVoltage380:
    def __init__(self):
        # self.__voltage = 380
        self.__amperage = list(c.COPPER_AMPERAGE_380)
        self.__capacity = list(c.COPPER_CAPACITY_380)


class AluminiumVoltage220:
    def __init__(self):
        # self.__voltage = 220
        self.__amperage = list(c.ALUMINIUM_AMPERAGE_220)
        self.__capacity = list(c.ALUMINIUM_CAPACITY_220)

    def __str__(self):
        return

    def get_amperage_index(self, value):
        if value not in self.__amperage:
            self.get_amperage_value(value)
        return self.__amperage.index(value)
    
    def get_amperage_value(self, value_):
        try:
            for item in range(len(self.__amperage)):
                if item < value_:
                    continue
                else:
                    return item
        except IndexError:
            print(f"{value_}: невідповідне значення")
            
    def get_amperage_value(self, value):
        try:
            while value not in self.__amperage and value <= max(self.__amperage):
                value += 1
                round(value, 1)
                return value
        except IndexError:
            print(f"{value}: невідповідне значення")

    def get_capacity_index(self, value):
        if value not in self.__capacity:
            return f"ValueError: {value} неправильне значення"
        return self.__capacity.index(value)


class AluminiumVoltage380:
    def __init__(self):
        # self.__voltage = 380
        self.__amperage = list(c.ALUMINIUM_AMPERAGE_380)
        self.__capacity = list(c.ALUMINIUM_CAPACITY_380)


class Electrician:
    def __init__(self):
        self.input_ = input("Введіть значення: ")

    def check_input(self):
        try:
            self.input_ = abs(float(self.input_))
        except ValueError:
            print(f'ValueError: {self.input_} невірне значення')
        else:
            return self.input_


v = AluminiumVoltage220()
electrician = Electrician()
print(v.get_amperage_index(electrician.check_input()))
'''