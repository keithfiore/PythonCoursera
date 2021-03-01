hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
overtime = r * 0.5
norm = 40
if h > 40:
    regpay = (h * r)
    overtime = float((h - norm) * overtime)
    grosspay = regpay + overtime
else:
    grosspay = float(h * r)
print(grosspay)
