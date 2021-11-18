#Kalkulačka těles 
#Autor: Štěpán Závacký, P1B
#Datum: 16.11.2021
####
###
##
#
import math

teleso = int(input("Vyber si těleso: čtverec[1] | obdélník[2] | kruh[3]: "))

if teleso is 1:
    rozmerA = int(input("Zadej rozměr strany A[cm]: "))
    print("Obvod čtverce o rozměrech ", rozmerA, "x", rozmerA, " je ", rozmerA*4, " cm")
    print("Obsah čtverce o rozměrech ", rozmerA, "x", rozmerA, " je ", rozmerA*rozmerA, " cm²")
elif teleso is 2:
    rozmerA = int(input("Zadej rozměr strany A[cm]: "))
    rozmerB = int(input("Zadej rozměr strany B[cm]: "))
    print("Obvod obedélníku o rozměrech ", rozmerA, "x", rozmerB, " je ", rozmerB*2 + rozmerA*2, " cm")
    print("Obsah obdélníku o rozměrech ", rozmerA, "x", rozmerB, " je ", rozmerB*rozmerA, " cm²")
elif teleso is 3:
    rozmerA = int(input("Zadej poloměr[r]=[cm]: "))
    print("Obvod kruhu o rozměrech [r]=", rozmerA,  " je", 2*math.pi*rozmerA, " cm")
    print("Obsah kruhu o rozměrech [r]=", rozmerA, " je", math.pi*rozmerA*rozmerA, " cm²")