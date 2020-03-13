class Calculator:
    def sum(self, string):
        if string == "":
            return 0
        else:
            string = string.replace("&", ",")
            string = string.replace(":", ",")
            numbers = string.split(",")
            total = 0
            for number in numbers:
                total += int(number)
            return total