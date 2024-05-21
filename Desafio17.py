from math import sqrt
catetooposto = float(input("Informe o valor do cateto oposto em centimetros(0.10m) ou metros(ex: 1.0m) >>> "))
catetoadjacente = float(input("Informe o valor do cateto adjacente em centimetros(0.10cm) ou metros(ex: 1.0m) >>> "))
print(f"Informe o valor do carteto oposto em centimetros(0.10m) ou metros(ex: 1.0m) >>> é {sqrt((catetooposto * catetooposto) + (catetoadjacente * catetoadjacente)):.2}")
