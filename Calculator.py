class Calculator:
    def sum(self, string):
        if string == "":
            return 0
        else:
            numbers = string.split(",")
            total = 0
            for number in numbers:
                total += int(number)
            return total