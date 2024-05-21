from math import radians, sin, cos, tan
# Angulo captura/ Calculo randians
ang = float(input("Informe o angulo >>>"))
angrad = radians(ang)
# Printa o seno, cosseno e tangente.
print(f"Seno: {sin(angrad):.3}, Cosseno: {cos(angrad):.3}, Tangente: {tan(angrad):.3}")