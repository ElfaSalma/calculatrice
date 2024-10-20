#programme calculatrice
def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division par zéro impossible!"
    else:
        return a / b
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
operation = input("Entrez l'opération (+, -, *, /) : ")

if operation == "+":
    resultat = addition(a, b)
elif operation == "-":
    resultat = soustraction(a, b)
elif operation == "*":
    resultat = multiplication(a, b)
elif operation   == "/":
    resultat = division(a, b)
else:
    resultat = "Opération invalide !"
print(f"Le résultat est : {resultat}")


    

