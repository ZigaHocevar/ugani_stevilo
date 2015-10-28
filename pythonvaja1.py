ime = "Ziga"
priimek = "Hocevar"

print (ime)

print ime

print "hello world"

print ("Moje ime je %s %s" % (ime,priimek))
# %s naj sprinta nek spring, v tem springu naj bo sintaksa

print ime + " " + priimek

ime = raw_input("Vpisi svoje ime: ")

print "Zivjo " + ime

print "Zivjo %s" %ime

if ime == "Ziga" or ime == "ziga":
    print "Zivjo Ziga"
elif ime == "Marko":
    print "Zivjo Marko"
else:
    print "Zivjo neznanec"

x = 0

while x < 10:
    if x == 5:
        print "Huhu"
    else:
        print x
    x = x + 1

print "koncal"

odgovor = "ja"

while odgovor == "ja":
    odgovor = raw_input("hoces nadaljevati?: (ja/ne) ")


while True:
    odgovor = raw_input("hoces nadaljevati?: (ja/ne) ")
    if odgovor == "ne":
        break

print "koncal"

geslo = "mojegeslo"
x = 4
while x > 0:
    vpisano_geslo = raw_input("Vpisi geslo?")
    if vpisano_geslo == geslo:
        print "Bravo"
        break
    else:
        print "Napacno"
        x = x - 1