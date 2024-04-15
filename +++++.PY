A=int (input("donner valeur a;"))

print("adem",c)

C = (A<B) and (3>B)
print(C)
D = (A == 5 ) or (B>10)
print (D)
A= 2 != 4
print(A)

import math
r=float(input("donne la rayon: "))
c=(4* math.pi*(r**3))/3
print("sphere",format(c,".3f"))
E=not C
print(E)
A =(50 % 3) == 2
print(A)

v=x**y
print("le puissance",v)   
##########################
a = int (input ("  entrer a : " ) )
b = int (input ("  entrer b : " ) )
#################################
###########if elif else##########
#################################
if a>0:
    print ("postif",a)
elif a<0 :
    print ("nigatif",a)
else:
    print ("nul",a)
############################
# varible 1 if condition else varible 2
max=a if a>b else b
print("adem",max)
############################
age = int (input ("  entrer age : " ) )
print("vote"if age >= 18 else "no vote")
#################################
#########les Bocale##############
#################################
# n bdya   n=0
# m la fin  m=16
# p 3dad 5twat 1.3.6.9.12.15  p=3
for i in range(n,m,p)
   print("hello")
############################
for i in range(0,11):
    f=7*i
    print("7 *",i,"=",f)   
############################
n=input("entre valer n:")
for i in range(0,n+1):
    f=7*i
    print("7 *",i,"=",f) 
############################
for i in range(1,11):
    for j in range(1,11):
        f=i*j
        print(i," * ",j,"=",f,end=" ") 
    print()       
##############################
for i in range(1,20,3):
    print(i) 
##############################********
a = int(input("  entrer a :"))
b = int(input("  entrer b :"))

for i in range(a):
    for j in range(b):
        print(" * ",end=" ") 
    print()
# ******
# ******
# ******
#################################
a = int(input("  entrer a :"))

while a <1 or a>10:
    a = int(input("  entrer a :"))

i=0    
while i <=10:
    f=a*i
    print(a,"*",i,"=",f)
    i=i+1
#################################
a = int(input("  entrer a :"))

while a <=1:
    a = int(input("  entrer a :"))

s=0
i=1
while i <= a:
    s=s+i
    i=i+1
    print("la somme",s)
#################################
#break
s=0
for i in range (1,5):
    print("entre nomber",i,":",end="")
    a = int(input())
    if a < 0:
        break
#break
    s=s+a
print("la somme",s)
#################################
#continue
s=0
for i in range (1,5):
    print("entre nomber",i,":",end="")
    a = int(input())
    if a < 0:
        continue
#continue
    s=s+a
print("la somme",s)
#################################
##########Fonction###############
#################################
def nom-fonction (var1,var2,var3):
 #   instruction
 #    a+b  
 #   return resultat

nom-fonction (var1,var2)
#################################
def somme (x,y):
    c=x+y
    print("la somme",c)

a = int(input("  entrer a :"))
b = int(input("  entrer b :"))
somme (a,b)
#################################
def somme (x,y):
    c=x+y
    return c

a = int(input("  entrer a :"))
b = int(input("  entrer b :"))
f=somme (a,b)

print(f)
#################################
# varible  global 
def affiche ():
    global c
    c=5
    print("la nomber",c)
c=9
affiche ()

#################################
##########import Fonction####modules##package##
#################################
Google
modules python standard
modules python standard Library
#################################
from nom-package.(nom-file.py) import nome--fonction
from adem.fractionss import somme
from adem.fractionss import somme as f

__package__--> adem dosi fih les fils li fifom li fonction
#################################
from fractionss import*
# from fractionss import somme1
a=int(input("donner le nomber a: "))
b=int(input("donner le nomber b: "))

s=somme1(a,b)
somme2(a,b)

print(s)
#################################
import fractionss as f
# from fractionss import somme1 as f
a=int(input("donner le nomber a: "))
b=int(input("donner le nomber b: "))

s=f.somme1(a,b)
f.somme2(a,b)

print(s)
#################################
# fractionss.py
def somme1 (x,y):
    c=x+y
    return c

def somme2 (x,y):
    c=x+y
    print("la somme",c)
#################################
from datetime import datetime
y=datetime.today()

print(y)
#################################
import webbrowser

webbrowser.open("https://google.com")
webbrowser.open("https://fiverr.com")
#####12#####12###########12############

#################################

#################################

#################################

#################################

#################################

#################################

#################################






# exercic

############################

############################

############################
a = int(input("  entrer a :"))

while a <=1:
    a = int(input("  entrer a :"))

s=0
i=1
while i <= a:
    s=s+i
    i=i+1
    print("la somme",s)

############################
a = int(input("  entrer a :"))

while a <10 or a >20:
    if a <10:
        print("ptit")
    else:
        print("grand")
    a = int(input("  entrer a :"))

print("bien")
############################
# 24*****
# cc = (input ("  entrer a : " ) )
# # b = int  (input("  entrer age :"))

# if ("a"< cc and "z"> cc ):
#     print ("alfbit")
# elif ("0"< cc and "9"> cc ):  
#       print("nomber") 
# else:
#         print ("ini")
############################
# 23
# a = int (input ("  entrer a : " ) )
# # b = int  (input("  entrer age :"))

# if (a%4 == 0 and a%100 != 100)or (a%400 == 0):
#     print ("pair")
# else:
#         print ("inper")
############################
# 22
# a = int (input ("  entrer a : " ) )
# # b = int  (input("  entrer age :"))

# if (a % 2 == 0 ):
#     print ("pair")
# else:
#         print ("inper")
############################
# 18
# a = str (input ("  entrer sex f/h : " ) )
# b = int  (input("  entrer age :"))
# if (a == "h" and b>=20)or(a == "f" and b>18 and b<35):
#     print ("paient")
# else:
#         print ("nop")
#################################
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#12
# A = float (input (" Veuillez entrer le dividende : " ) )
# B = float (input (" Veuillez entrer le diviseur : " ) )
# if A>B :
#     print ("Le MAX: ",A)
# else:
#     print ("Le MAX: ",B)

# a = float (input (" Veuillez entrer le dividende : " ) )

# if a > 0:
#     print("le nomber positif")
# elif a == 0:
#     print("le nomber errer")
# else:
#     print("le nomber négatif")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 1 nom=str(input( "donner voter nom; "))
# age=int(input("donner voter age; "))

# print ("bonjour " , nom , ",tu as ",age, " ans et bienvenue a luniversite")
# ********************************************************************************

# 2 date_naissance = int (input ("Quelle  est votre année de naissance ? "))
# age = 2021 - date_naissance
# print("Vous aurez alors : ", age ," ans cette année")
# *********************************************************
# 3 la=float(input("largeur"))
# lo=float(input("lorngreur"))
# s=(la*2)+(lo*2)
# p=la*lo
# print("perimater" ,format(p,".2f"))
# print("surface" ,format(s,".2f"))
# ****************************************
# 4
# x=int(input("done x"))
# y=int(input("done y"))
# v=x**y
# print("le puissance",v)
# **************************************
# 5
# x=float(input("donnee x: "))
# y=float(input("donnee y: "))
# a=x+y
# b=x*y
# c=x-y
# d=x/y
# print("la somme",a)
# print("la produit",b)
# print("la difference",c)
# print("la dividion",format(d,".3f"))
# ************************************************
# 6
# f = float(input("Donnez la première note: "))
# w = float(input("Donnez la deuxième note: "))
# e = float(input("Donnez la troisième note: "))
# r = float(input("Donnez la quatrième note: "))
# t = float(input("Donnez la cinquième note: "))

# # Calcul de la somme des notes
# s =  f+ w + e + r + t

# # Calcul de la moyenne des notes
# m = s / 5

# # Affichage des résultats
# print("La somme des notes est :", format(s, ".3f"))
# print("La moyenne des notes est :", format(m, ".3f"))
# **********************************************************
# 7
# import math
# r=float(input("donne la rayon: "))
# c=(4* math.pi*(r**3))/3
# print("sphere",format(c,".3f"))
# *****************************************
# 8
# a=int(input("entre a: "))
# b=int(input("entre b: "))
# c=b
# b=a
# a=c
# print("le a est",a,"le b est",b)
# **********************************
# 9
# t=int(input("enter le temps: "))

# h=t//3600
# a=t%3600
# m=a//60
# s=a%60

# print("le temp: ",h,"H",m,"M",s,"S")
# ******************************************
# 10
# import math
# ax=float(input("entre point ax: "))
# bx=float(input("entre point bx: "))
# by=float(input("entre point by: "))
# ay=float(input("entre point ay: "))

# ab=(bx-ax)**2+(by-ay)**2
# f=math.sqrt(ab)

# print("la distance enter les pints",format(f,".3f"))
# *******************************************************
# 11
# r1=float(input("entre r1: "))
# r2=float(input("entre r2: "))
# r3=float(input("entre r3: "))
# rser=r1+r2+r3
# rpar=(r1*r2*r3)/(r1*r2+r1*r3+r2*r3)
# print("le rser",rser)
# print("le rpar",rpar)
# ******************************************