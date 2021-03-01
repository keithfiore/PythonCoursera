hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
print(h, r)
overtime: float = r * 0.5
norm = 40
if h > 40:
    regpay = (h * r)
    overtime = float((h - norm) * overtime)
    grosspay = regpay + overtime
else:
    grosspay = float(h * r)
print("Pay:", grosspay)
