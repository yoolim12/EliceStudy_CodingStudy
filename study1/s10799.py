import sys

stick = sys.stdin.readline()
stick = stick.replace("()", "l")

stick_num = 0
stick_part = 0

for e in stick:
    if e == '(':
        stick_num += 1
    elif e == 'l':
        stick_part += stick_num
    else: # e == ')'
        stick_part += 1
        stick_num -= 1

print(stick)
print(stick_part - 1)