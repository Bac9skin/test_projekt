actions = ["+", "-", "*", "/"]

arg1 = imput(One)
arg2 = imput(two)
action = imput(Deystvie)

try:
    if "." in arg1
        arg1 = float(arg1)
    else
        arg1 = int(arg1)
except ValueError:
    print("Vse ne to1")
    exit(1)

try:
    if "." in arg2
        arg2 = float(arg2)
    else
        arg2 = int(arg2)
except ValueError:
    print("Vse ne to2")
    exit(1)

    if action not in actions:
        print("Vse ne to2")
        exit()
