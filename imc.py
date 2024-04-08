nome = input("digite o nome do paciente:")
alturacm = float(input("digte a altura (em cm):"))
peso = float(input("digite o peso (em kg): "))
alturam = alturacm / 100
imc = peso / (alturam ** 2)

if imc <= 18.5:
    print(f"{nome} {imc:.2f}abaixo do peso(pegue suplemento com cariani)")
elif imc >= 18.6 and imc <= 24.9:
    print(f"{nome} {imc:.2f} peso ideal")
elif imc >= 25.0 and imc <= 29.9:
    print(f"{nome} {imc:.2f} sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
    print(f"{nome} {imc:.2f} obesidade grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print(f"{nome} {imc:.2f} obesidade grau 2 ")
else:
    print(f"{nome} {imc:.2f} obesidade grau 3 (Dr. nowzaradan te espera)")
