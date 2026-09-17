# nummers = ["+32 470 998301","+32 483 313220", "+32 453 231456"]


# namen = ["Jan,","Piet","Kapper korneel"]

# naam=input("zeg een naam")

# for index, naame in enumerate(naam)
#     if naame == naam:

#     print(nummers[index])

# else:
#     print("naam niet in lijst")


# telefoonboekje={
#     "jan":"+32 470 998301",
#     "piet":"+32 483 31220",
#     "kapper":"+32 453 231456"
# }

# print(telefoonboekje["jan"])

# telefoonboekje["joris"]= "+32 483 02023"
# telefoonboekje["piet"]= "+32 483 313244"
# telefoonboekje.pop("kapper")

# naam=input("Geef naam")


telefoonboekje={
     "jan":"+32 470 998301",
     "piet":"+32 483 31220",
    "kapper":"+32 453 231456"
 }
naam=input("geef naam")
if naam in telefoonboekje:
    print(telefoonboekje[naam])
else:
    print("deze bestaat niet")