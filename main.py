# This program calculates pay, and adjusts the pay rate for overtime hours.
def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay


sh = input('Hours Worked: ')
sr = input('Rate of Pay: ')
fh = float(sh)
fr = float(sr)
otp = (fh-40.0) * (fr * 0.5)
xp = computepay(fh, fr)
print("Pay: ", xp)
print("Overtime accounted for ",otp," of your pay")