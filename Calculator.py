class Calculator:
    def sum(self, string):
        if string == "":
            return 0
        elif not(',' in string):
            return int(string)
        else:
            return int(string[0]) + int(string[2])