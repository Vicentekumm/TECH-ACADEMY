from msilib.schema import Media


a = int(input("DIGITE A: "))
b = int(input("DIGITE B: "))
c = int(input("DIGITE C: "))

Media = ((a*2)+(b)+(c*2)) / 5

if Media >5 :
    print("aprovado")
else Media <=3 :
    print("recuperacao")
elif Media <5 :
    print("reprovado")