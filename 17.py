num2words = {1:"One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", \
             6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", \
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", \
            19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", \
            50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", \
            90: "Ninety"}

def convert(n):
    if not n:
        return ""
    if n in num2words:
        return num2words[n]
    elif n < 100:
        return f"{num2words[n - n % 10]}-{num2words[n % 10]}"
    elif n < 1000:
     #    100: "hundred", 1000: "thousand"
        if n % 100:
            return f"{num2words[n // 100]} hundred and {convert(n % 100)}"
        else:
            return f"{num2words[n // 100]} hundred"

    else:
        return f"{num2words[n // 1000]} thousand {convert(n % 1000)}"


s = " ".join(map(convert, range(1, 1001)))
print(len(s.replace(" ","").replace("-", "")))