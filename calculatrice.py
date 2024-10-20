import math

# Fonctions mathématiques de base
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division par zéro impossible !"
    else:
        return a / b

# Fonctions trigonométriques
def sinus(a):
    return math.sin(math.radians(a))  # Conversion en radians

def cosinus(a):
    return math.cos(math.radians(a))  # Conversion en radians

def tangente(a):
    return math.tan(math.radians(a))  # Conversion en radians

# Interface utilisateur
a = float(input("Entrez le premier nombre (ou l'angle pour les fonctions trigonométriques) : "))

# Si l'utilisateur choisit une fonction non-trigonométrique, il peut entrer un deuxième nombre
operation = input("Entrez l'opération (+, -, *, /, sin, cos, tan) : ")

# Calculs selon l'opération
if operation in ["+", "-", "*", "/"]:
    b = float(input("Entrez le deuxième nombre : "))  # Deuxième nombre nécessaire pour ces opérations
    if operation == "+":
        resultat = addition(a, b)
    elif operation == "-":
        resultat = soustraction(a, b)
    elif operation == "*":
        resultat = multiplication(a, b)
    elif operation == "/":
        resultat = division(a, b)
elif operation == "sin":
    resultat = sinus(a)
elif operation == "cos":
    resultat = cosinus(a)
elif operation == "tan":
    resultat = tangente(a)
else:
    resultat = "Opération invalide !"

# Afficher le résultat
print(f"Le résultat est : {resultat}")
