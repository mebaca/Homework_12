d = float(input("Bitte geben Sie die zurückgelegte Strecke in Metern ein: "))
sl = float(input("Bitte geben Sie ihre Schrittlänge in Metern ein: "))

def steps(d,sl):
    x = float(d / sl)
    return x

print("Sie haben " + str(steps(d,sl)) + " Schritte gemacht!")