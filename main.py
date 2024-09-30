#   Atrodi kļūdas kodā un izlabo tās
#         un optimizē kodu
#
#   Programma paprasa cilvēka vardu un cik gadi
#           un pārbauda vai ir pieaudzis
#
#
# Pieprasām lietotāja vārdu un vecumu
name = input("Kāds ir tavs vārds? ")
age = int(input("Cik tev gadu? "))

# Izvadām vārdu un vecumu
print(f"Tevi sauc {name}, un tev ir {age} gadi.")

if age >= 18:
    print("Tu esi pieaudzis!")
else:
    print("Tu neesi pieaudzis!")

# Veicam nelielu matemātiku - aprēķinām dzimšanas gadu
current_year = 2024
birth_year = current_year - age

# Izvadām aprēķināto dzimšanas gadu
print(f"Tavs dzimšanas gads ir aptuveni {birth_year}.")




