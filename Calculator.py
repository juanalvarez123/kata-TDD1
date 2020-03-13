class Calculator:
    def sum(self, string):
        if string == "":
            return 0
        elif not(',' in string):
            return int(string)
        else:
            numbers = string.split(",")
            total = 0
            for number in numbers:
                total += int(number)
            return total