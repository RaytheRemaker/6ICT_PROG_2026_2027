dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]
ray=int(input("welke rij wilde gij? "))
kolom=int(input("wulke kolom wilde gij? "))


if ray>len(dambord_2D) or kolom>len(dambord_2D):
    print("dat gaat niet")
else:
    print(dambord_2D[ray][kolom] )