skrito_stevilo = "14"

while True:
    skrito_stevilo = raw_input("Vnesi poljubno stevilo od 0 do 20:")
    if skrito_stevilo == "14":
        print "Cestitam, uganil si skrito stevilo in zadel 0 EUR!"
        break
    elif skrito_stevilo == "13" or skrito_stevilo == "15":
        print "Si zelo, zelo, zelo blizu :)"
    else:
        print "Vneseno stevilo zal ni pravilno"