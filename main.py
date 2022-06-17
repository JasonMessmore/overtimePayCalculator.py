# This program calculates pay, and adjusts the pay rate for overtime hours.
def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay


while True:
    try:
        sh = input('Hours Worked: ')
        sr = input('Rate of pay: ')
        fh = float(sh)
        fr = float(sr)
        break
    except:
        print('Error: Please enter numerals only')


otp = (fh - 40.0) * (fr * 0.5)
xp = computepay(fh, fr)
rp = round(xp, 2)
rotp = round(otp, 2)

print("Pay: $",rp)
print("Overtime accounted for $",rotp, " of your pay")
