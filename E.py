a = float(input("Värde för a: "))
b = float(input("Värde för b: "))
c = float(input("Värde för c: "))

if c**2 == a**2 + b**2:
    print(f"Trianglen med sidorna {a}, {b} och {c} är en rätvinklig triangel")
else:
    print(f"Trianglen med sidorna {a}, {b} och {c} är inte en rätvinkli triagel")