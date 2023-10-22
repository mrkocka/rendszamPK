import random 

latin_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'


def randomLetters():
    """ Három random latin betű kiválasztása """
    return ''.join(random.choice(latin_letters) for _ in range(3))

def randomNumber():
    """ Három random szám kiválasztása """
    return ''.join(random.choice(numbers) for _ in range(3))

def rendszamGen(quantity):
    """ Elkészíti a kívánt rendszámokat """
    for _ in range(quantity):
        random_letters = randomLetters()
        random_numbers = randomNumber()
        result = random_letters + '-' + random_numbers
        print(result)


# Felhasználótól bekérjük a rendszámok számát
try: 
   quantity = int(input("Hány rendszámra van szükséged? "))
   rendszamGen(quantity)
except ValueError: 
    print("Érvénytelen bemenet. Kérem adjon meg egy számot.")
