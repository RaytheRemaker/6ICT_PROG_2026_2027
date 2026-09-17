# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

#niveau 1 
# Print de dictionary-waarde gekoppeld aan onderstaande variabele
fruit = "banaan"
print( fruitmand[fruit] )
#niveau 2
nieuw_fruit  = "mango"
nieuw_aantal = 1
fruitmand["mango"]= 1

#niveau 3
fruit = "banaan"
nieuw_aantal = 8
fruitmand(fruit)= nieuw_aantal
print (fruitmand)
#niveau 4
fruit = "kers"
verlaag_met = 43
fruitmand[fruit]=fruitmand[fruit]-verlaag_met
print(fruitmand)
#niveau 5
erugleggen_fruit = "kers"
fruitmand.pop(fruit)