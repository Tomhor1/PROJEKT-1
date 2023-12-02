"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomas Horniak
email: tomas.horniak27@gmail.com
discord: just#7854
"""

from task_template import TEXTS

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("Enter name:")
password = input("Enter passoword:")
for u in users:
    if username == u and password == users[u]:
        print("Welcome to app", username,
            "we have", (len(TEXTS)), "text to analyze")
      
        text_to_analyze = input(f"Enter a number between 1 and {len(TEXTS)} to select: ")
        if not text_to_analyze.isnumeric():
            print("Wrong input")
            break
        else:
            if 1 <= int(text_to_analyze) <=3:
                slova = (TEXTS[0].split())
                print("There are", len(slova), "words in the selected text.")

                slova_s_velkym_pismenom = 0
                slova_s_velkymi_pismenami = 0
                slova_s_malym_pismenom = 0
                pocet_cisiel = 0
                sucet_cisiel = 0

                for slovo in slova:
                    slovo = slovo.strip('.,!?()[]{}":;')

                    if slovo.istitle():
                        slova_s_velkym_pismenom += 1
                    elif all(pismeno.isupper() for pismeno in slovo):
                        slova_s_velkymi_pismenami += 1
                    elif slovo.islower():
                        slova_s_malym_pismenom += 1
                    elif slovo.isnumeric():
                        pocet_cisiel += 1
                        sucet_cisiel += int(slovo)
                    
                print("There are", slova_s_velkym_pismenom, "words in the selected text.")             
                print("There are", slova_s_velkymi_pismenami, "uppercase words.")
                print("There are", slova_s_malym_pismenom, "lowercase words.")
                print("There are", pocet_cisiel, "numeric strings.")
                print("The sum of all the numbers", sucet_cisiel,)
                break
            else:
                print("You didn't enter number btw. 1 and 3")
                break
else: 
    print("Unregistered user, terminating the program..")

if 1 <= int(text_to_analyze) <= 3:
    slova = TEXTS[int(text_to_analyze) - 1].split()

    pocetnost_dlzky_slov = {}

    for slovo in slova:

        dlzka_slova = len(slovo)

        if dlzka_slova in pocetnost_dlzky_slov:
            pocetnost_dlzky_slov[dlzka_slova] += 1
        else:
            pocetnost_dlzky_slov[dlzka_slova] = 1

    sorted_pocetnost_dlzky_slov = dict(sorted(pocetnost_dlzky_slov.items()))

    print("-" * 30)
    print("LEN | OCCURRENCES    | NR.")
    print("-" * 30)

    for dlzka, pocet in sorted_pocetnost_dlzky_slov.items():
        print(f"{dlzka:2}|{'*' * pocet:13}  |{pocet}")

    print("-" * 30)
    



