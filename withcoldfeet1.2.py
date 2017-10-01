#-*- coding: utf-8 -*-

import os
import winsound
import msvcrt
from msvcrt import getch
import time
from random import randint, choice

os.system('color 06')
os.system('mode con:cols=25 lines=31')


alp = 'abcdefghijklmnopqrstuvwxyz '
az = 0
kbcount = 0

x = chr(219)
o = chr(0)
p = alp[az]
f = '^'
e = '_'
w = '~'
a = '@'
hot = '>'
dry = '#'
wet = '$'
cold = '<'
h = '/'
i = '\\'
j = '1'
k = '2'
l = '3'
m = '4'
d = '5'
inv = ' '
obstacles = []
craftitems = []
assembly = []

window = [o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,'\n',
          o,o,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,' ']

lab =    [o,o,x,x,x,x,d,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,'\n',
          o,o,x,o,o,o,o,o,o,o,x,h,x,i,x,o,o,o,o,o,o,o,x,'\n',
          o,o,x,x,x,o,o,o,o,o,x,x,x,x,x,o,o,o,o,o,x,x,x,'\n',
          o,o,x,f,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,j,x,'\n',
          o,o,x,x,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,'\n',
          o,o,x,w,x,o,o,o,o,o,p,o,o,o,o,o,o,o,o,o,x,k,x,'\n',
          o,o,x,x,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,'\n',
          o,o,x,a,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,l,x,'\n',
          o,o,x,x,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,'\n',
          o,o,x,e,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,m,x,'\n',
          o,o,x,x,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,x,x,'\n',
          o,o,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,'\n',
          o,o,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,' ']

dream =  [o,o,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,'\n',
          o,o,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,x,x,x,x,x,x,x,x,x,x,x,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,x,hot,x,x,x,f,x,x,x,dry,x,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,x,x,x,x,x,x,x,x,x,x,x,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,x,a,x,x,x,o,x,x,x,e,x,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,x,x,x,x,x,x,x,x,x,x,x,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,x,wet,x,x,x,w,x,x,x,cold,x,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,x,x,x,x,x,x,x,x,x,x,x,o,o,o,o,x,'\n',
          o,o,x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,'\n',
          o,o,x,o,o,o,p,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,'\n',
          o,o,x,x,x,x,o,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,' ']

vtab = len(lab)/13

answer1 = [a,e,f,w]
answer2 = [w,w,w,w]
answer3 = [hot,e,dry,w]
answer4 = [cold,hot,a,f]
answer5 = [e,e,e,e]
answer6 = [' ',' ',' ',a]
answer7 = [o,o,o,o]

def titlex():
    window[50:71]   = '* * * * * * * * * * *'
    window[74:95]   = ' * * * * * * * * * * '
    window[98:119]  = '* * * * * * * * * * *'
    window[122:143] = ' * * * * * * * * * * '
    window[146:167] = '* * * * * * * * * * *'
    window[170:191] = ' * * * * * * * * * * '
    window[194:215] = '* * * * * * * * * * *'
    window[218:239] = ' * * * * * * * * * * '
    window[242:263] = '* * * * * * * * * * *'
    window[266:287] = ' * * * * * * * * * * '
    window[290:311] = '* * * * * * * * * * *'
    print ''.join(window)

def titlexx():
    window[50:71]   = ' * * * * * * * * * * '
    window[74:95]   = '* * * * * * * * * * *'
    window[98:119]  = ' * * * * * * * * * * '
    window[122:143] = '* * * * * * * * * * *'
    window[146:167] = ' * * * * * * * * * * '
    window[170:191] = '* * * * * * * * * * *'
    window[194:215] = ' * * * * * * * * * * '
    window[218:239] = '* * * * * * * * * * *'
    window[242:263] = ' * * * * * * * * * * '
    window[266:287] = '* * * * * * * * * * *'
    window[290:311] = ' * * * * * * * * * * '
    print ''.join(window)

def title0():
    window[50:71]   = '                     '
    window[74:95]   = '                     '
    window[98:119]  = '                     '
    window[122:143] = '                     '
    window[146:167] = 'k u c y k - k u c y k'
    window[170:191] = '                     '
    window[194:215] = '      presents       '
    window[218:239] = '                     '
    window[242:263] = '                     '
    window[266:287] = '                     '
    window[290:311] = '                     '
    print ''.join(window)

def title1():
    window[50:71]   = '                     '
    window[74:95]   = '                     '
    window[98:119]  = '                     '
    window[122:143] = '       W I T H       '
    window[146:167] = '       C O L D       '
    window[170:191] = '       F E E T       '
    window[194:215] = '                     '
    window[218:239] = '                     '
    window[242:263] = '                     '
    window[266:287] = '                     '
    window[290:311] = '                     '
    print ''.join(window)

def title2():
    window[50:71]   = '                     '
    window[74:95]   = '                     '
    window[98:119]  = '                     '
    window[122:143] = '       W I T H       '
    window[146:167] = '       C O L D       '
    window[170:191] = '       F E E T       '
    window[194:215] = '                     '
    window[218:239] = '                     '
    window[242:263] = '< press up to start >'
    window[266:287] = '                     '
    window[290:311] = '                     '
    print ''.join(window)

def title3():
    window[50:71]   = '                     '
    window[74:95]   = '                     '
    window[98:119]  = '                     '
    window[122:143] = '       W I T H       '
    window[146:167] = '       C O L D       '
    window[170:191] = '       F E E T       '
    window[194:215] = '                     '
    window[218:239] = '                     '
    window[242:263] = '  press up to start  '
    window[266:287] = '                     '
    window[290:311] = '                     '
    print ''.join(window)

t1 = list('Fed by the wind along')
t2 = list('my dark skin         ')
t3 = list('the hungry orange    ')
t4 = list('eats its way         ')
t5 = list('down                 ')
t6 = list('at last ending my    ')
t7 = list('misery               ')
t8 = list('diving into marine   ')
t9 = list('hues.                ')
t10 = list('                     ')
t11 = list('                     ')
text1 = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11]


t12 = list('Down there where     ')
t13 = list('all is blue and blur ')
t14 = list('the mumbling sounds  ')
t15 = list('around               ')
t16 = list('act like gentle pats ')
t17 = list('a comforting place   ')
t18 = list('my home is           ')
t19 = list('a simple life        ')
t20 = list('I follow             ')
t21 = list('undulating currents  ')
t22 = list('worried about nothing')
text2 = [t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22]


t23 = list('It is unbearable     ')
t24 = list('suffocating          ')
t25 = list('the yellow land      ')
t26 = list('splits               ')
t27 = list('lightnings of darker ')
t28 = list('crevasses watch over ')
t29 = list('the bones of the     ')
t30 = list('last dog             ')
t31 = list('loyal companion      ')
t32 = list('ultimate sacrifice to')
t33 = list('the lords of rain    ')
text3 = [t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33]


t34 = list('No please            ')
t35 = list('keep them I          ')
t36 = list('insist               ')
t37 = list('I still have some on ')
t38 = list('the other hand       ')
t39 = list('for now              ')
t40 = list('as long as           ')
t41 = list('my inner breath      ')
t42 = list('is here to           ')
t43 = list('remind them of       ')
t44 = list('unextinguished coals ')
text4 = [t34,t35,t36,t37,t38,t39,t40,t41,t42,t43,t44]

t45 = list('Distant rumors of    ')
t46 = list('a river              ')
t47 = list('trap for             ')
t48 = list('the dying man lost in')
t49 = list('labyrinthic valleys  ')
t50 = list('of clay              ')
t51 = list('solid element of     ')
t52 = list('many shades          ')
t53 = list('still theater of     ')
t54 = list('light for here stands')
t55 = list('four characters      ')
text5 = [t45,t46,t47,t48,t49,t50,t51,t52,t53,t54,t55]

t56 = list('There is nothing     ')
t57 = list('nothing at all       ')
t58 = list('in the act of the    ')
t59 = list('search               ')
t60 = list('a vacuum of hope     ')
t61 = list('and despair          ')
t62 = list('nothing here         ')
t63 = list('or there             ')
t64 = list('besides the name     ')
t65 = list('one was given        ')
t66 = list('as the search began  ')
text6 = [t56,t57,t58,t59,t60,t61,t62,t63,t64,t65,t66]

t67 = list('Aether               ')
t68 = list('light mysterious     ')
t69 = list('thing                ')
t70 = list('why can no soul      ')
t71 = list('have you             ')
t72 = list('is there no answer   ')
t73 = list('for there is no      ')
t74 = list('question             ')
t75 = list('no purpose nor quest ')
t76 = list('the room is yellow   ')
t77 = list('to my eyes only      ')
text7 = [t67,t68,t69,t70,t71,t72,t73,t74,t75,t76,t77]

def riddle1():
    window[50:71]   = t1
    window[74:95]   = t2
    window[98:119]  = t3
    window[122:143] = t4
    window[146:167] = t5
    window[170:191] = t6
    window[194:215] = t7
    window[218:239] = t8
    window[242:263] = t9
    window[266:287] = t10
    window[290:311] = t11
    print ''.join(window)

def riddle2():
    window[50:71]   = t12
    window[74:95]   = t13
    window[98:119]  = t14
    window[122:143] = t15
    window[146:167] = t16
    window[170:191] = t17
    window[194:215] = t18
    window[218:239] = t19
    window[242:263] = t20
    window[266:287] = t21
    window[290:311] = t22
    print ''.join(window)

def riddle3():
    window[50:71]   = t23
    window[74:95]   = t24
    window[98:119]  = t25
    window[122:143] = t26
    window[146:167] = t27
    window[170:191] = t28
    window[194:215] = t29
    window[218:239] = t30
    window[242:263] = t31
    window[266:287] = t32
    window[290:311] = t33
    print ''.join(window)

def riddle4():
    window[50:71]   = t34
    window[74:95]   = t35
    window[98:119]  = t36
    window[122:143] = t37
    window[146:167] = t38
    window[170:191] = t39
    window[194:215] = t40
    window[218:239] = t41
    window[242:263] = t42
    window[266:287] = t43
    window[290:311] = t44
    print ''.join(window)

def riddle5():
    window[50:71]   = t45
    window[74:95]   = t46
    window[98:119]  = t47
    window[122:143] = t48
    window[146:167] = t49
    window[170:191] = t50
    window[194:215] = t51
    window[218:239] = t52
    window[242:263] = t53
    window[266:287] = t54
    window[290:311] = t55
    print ''.join(window)

def riddle6():
    window[50:71]   = t56
    window[74:95]   = t57
    window[98:119]  = t58
    window[122:143] = t59
    window[146:167] = t60
    window[170:191] = t61
    window[194:215] = t62
    window[218:239] = t63
    window[242:263] = t64
    window[266:287] = t65
    window[290:311] = t66
    print ''.join(window)

def riddle7():
    window[50:71]   = t67
    window[74:95]   = t68
    window[98:119]  = t69
    window[122:143] = t70
    window[146:167] = t71
    window[170:191] = t72
    window[194:215] = t73
    window[218:239] = t74
    window[242:263] = t75
    window[266:287] = t76
    window[290:311] = t77
    print ''.join(window)

dreampos = dream.index(p)
playerpos = lab.index(p)
earthpos = lab.index(e)
waterpos = lab.index(w)
firepos = lab.index(f)
airpos = lab.index(a)
hpos = lab.index(h)
ipos = lab.index(i)
jpos = lab.index(j)
kpos = lab.index(k)
lpos = lab.index(l)
mpos = lab.index(m)
doorpos = lab.index(d)

h = ' '
i = ' '
j = ' '
k = ' '
l = ' '
m = ' '
d = chr(219)
lab[hpos] = h
lab[ipos] = i
lab[jpos] = j
lab[kpos] = k
lab[lpos] = l
lab[mpos] = m
lab[doorpos] = d

for y, z in enumerate(lab):
    if z == x:
        obstacles.append(y)
        
winsound.PlaySound("introsong.wav", winsound.SND_ASYNC)

def anim():
   os.system('cls')
   titlexx()
   os.system('cls')
   titlex()
   time.sleep(0.3)
   os.system('cls')
   titlexx()
   time.sleep(0.3)
   os.system('cls')
   titlex()
   time.sleep(0.3)
   os.system('cls')
   titlexx()
   time.sleep(0.3)
   os.system('cls')
   titlex()
   time.sleep(0.3)
   os.system('cls')
   titlexx()
   time.sleep(0.3)
   os.system('cls')
   titlex()
   os.system('cls')

print
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
print '      D I S P L A Y\n     S E T T I N G S\n'
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
print
print '- right click at the top   of this window on the\n  "Whith Cold Feet"\n  title.'
print
print '- click on Properties.'
print
print '- click on the Font tab.'
print
print '- in the Font section\n  select\n  "Raster Fonts".'
print
print '- in the size section\n  select 8 x 12.'
print
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
raw_input('Press Enter to continue')

os.system('cls')
print
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
print '     C O N T R O L S\n'
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
print
print '- arrow keys to move.'
print
print '- stand next to an\n  element to take it.'
print
print '- stand next to a\n  container to drop\n  the element.'
print
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
raw_input('press Enter to continue')

os.system('cls')
print
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
print '       S T O R Y\n'
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
print
print "- you're an Alchemist in\n  your lab."
print
print '- decypher the riddles\n  before time eats\n  though them.'
print
print '- find the missing\n  elements at the\n  mixing table.'
print
print "- enter the right\n  combinations at\n  the assembling table."
print
print '- try to crack all\n  the riddles before\n  you become an old Z.'
print
print '~~~~~~~~~~~~~~~~~~~~~~~~~'
raw_input('press Enter to start.')

anim()
title0()
time.sleep(2.5)
anim()
title1()
time.sleep(3)


while msvcrt.kbhit() == False:
    os.system('cls')
    title2()
    time.sleep(1)
    os.system('cls')
    title3()
    time.sleep(1)
    os.system('cls')

winsound.PlaySound(None, winsound.SND_ASYNC)

riddle = riddle1

answer = answer1

text = text1

comment = ''

def mainsong():
    winsound.PlaySound("mainsong.wav", winsound.SND_ASYNC)

def musicstop():
    musicstop = winsound.PlaySound(None, winsound.SND_ASYNC)

mainsong()

while True :

    craftitems = [h,i]

    assembly = [j,k,l,m]
    
    p = alp[az]

    if msvcrt.kbhit():

        key = ord(getch())

        if assembly == answer1:
            inv = ' '
            j = ' '
            lab[jpos] = j
            k = ' '
            lab[kpos] = k
            l = ' '
            lab[lpos] = l
            m = ' '
            lab[mpos] = m
            h = ' '
            lab[hpos] = h
            i = ' '
            lab[ipos] = i
            riddle = riddle2
            answer = answer2
            text = text2
        elif assembly == answer2:
            inv = ' '
            j = ' '
            lab[jpos] = j
            k = ' '
            lab[kpos] = k
            l = ' '
            lab[lpos] = l
            m = ' '
            lab[mpos] = m
            h = ' '
            lab[hpos] = h
            i = ' '
            lab[ipos] = i
            riddle = riddle3
            answer = answer3
            text = text3
        elif assembly == answer3:
            inv = ' '
            j = ' '
            lab[jpos] = j
            k = ' '
            lab[kpos] = k
            l = ' '
            lab[lpos] = l
            m = ' '
            lab[mpos] = m
            h = ' '
            lab[hpos] = h
            i = ' '
            lab[ipos] = i
            riddle = riddle4
            answer = answer4
            text = text4
        elif assembly == answer4:
            inv = ' '
            j = ' '
            lab[jpos] = j
            k = ' '
            lab[kpos] = k
            l = ' '
            lab[lpos] = l
            m = ' '
            lab[mpos] = m
            h = ' '
            lab[hpos] = h
            i = ' '
            lab[ipos] = i
            riddle = riddle5
            answer = answer5
            text = text5
        elif assembly == answer5:
            inv = ' '
            j = ' '
            lab[jpos] = j
            k = ' '
            lab[kpos] = k
            l = ' '
            lab[lpos] = l
            m = ' '
            lab[mpos] = m
            h = ' '
            lab[hpos] = h
            i = ' '
            lab[ipos] = i
            riddle = riddle6
            answer = answer6
            text = text6
        elif assembly == answer6:
            inv = ' '
            j = ' '
            lab[jpos] = j
            k = ' '
            lab[kpos] = k
            l = ' '
            lab[lpos] = l
            m = ' '
            lab[mpos] = m
            h = ' '
            lab[hpos] = h
            i = ' '
            lab[ipos] = i
            riddle = riddle7
            answer = answer7
            text = text7
            

        if f in craftitems:
            if a in craftitems:
                os.system('color 47')
                inv = hot
                h = ' '
                i = ' '
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Quality HOT created.'
                time.sleep(1)
                os.system('color 06')
            elif e in craftitems:
                os.system('color 67')
                inv = dry
                h = ' '
                i = ' '
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Quality DRY created.'
                time.sleep(1)
                os.system('color 06')
        elif w in craftitems:
            if a in craftitems:
                os.system('color 97')
                inv = wet
                h = ' '
                i = ' '
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Quality WET created.'
                time.sleep(1)
                os.system('color 06')
            elif e in craftitems:
                os.system('color 17')
                inv = cold
                h = ' '
                i = ' '
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Quality COLD created.'
                time.sleep(1)
                os.system('color 06')

        kbcount = kbcount + 1
        if kbcount == 60:
            az = az + 1
            kbcount = 0
            if az > 25:
                az = 0
        elif kbcount % 3 == 0:
            choice(text)[randint(0,20)] = ' '
        elif az == 2 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Time is the key..'
                time.sleep(2)
        elif az == 5 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  The answer.. Yes..'
                time.sleep(2.2)
        elif az == 7 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  This must be it.'
                time.sleep(2)
        elif az == 10 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Symbols.. Mysteries'
                time.sleep(2)
        elif az == 15 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Fire, ITS FIRE!'
                time.sleep(2)
        elif az == 18 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  My brains, lying ?'
                time.sleep(2)
        elif az == 20 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  John 5:0 says aliens.'
                time.sleep(2)
        elif az == 23 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  My clinging bones !'
                time.sleep(2)
        elif az == 25 :
            if kbcount == 2:
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Wait..'
                time.sleep(2)
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Could it be ?'
                time.sleep(2)
                os.system('cls')
                d = ' '
                lab[doorpos] = d
                riddle()
                print
                print ''.join(lab)
                print '  A door..'
                time.sleep(2)

            
        if key == 77:
            lab[playerpos] = o
            playerpos = playerpos + 1
            if playerpos in obstacles:
                playerpos = playerpos - 1
                lab[playerpos] = p
            elif playerpos == hpos + (vtab * 2):
                h = inv
                inv = ' '
                lab[playerpos] = p
                lab[hpos] = h
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Mixing Table'
            elif playerpos == ipos + (vtab * 2):
                i = inv
                inv = ' '
                lab[playerpos] = p
                lab[ipos] = i
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Mixing Table'
            elif playerpos == jpos - 2:
                j = inv
                inv = ' '
                lab[playerpos] = p
                lab[jpos] = j
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == kpos - 2:
                k = inv
                inv = ' '
                lab[playerpos] = p
                lab[kpos] = k
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == lpos - 2:
                l = inv
                inv = ' '
                lab[playerpos] = p
                lab[lpos] = l
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == mpos - 2:
                m = inv
                inv = ' '
                lab[playerpos] = p
                lab[mpos] = m
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            else:
                lab[playerpos] = p
                lab[hpos] = h
                lab[ipos] = i
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  [%s]' % inv
        
        elif key == 75:
            lab[playerpos] = o
            playerpos = playerpos - 1
            if playerpos in obstacles:
                playerpos = playerpos + 1
                lab[playerpos] = p
            elif playerpos == earthpos + 2:
                inv = e
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Earth Element'
            elif playerpos == waterpos + 2:
                inv = w
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Water Element'
            elif playerpos == firepos + 2:
                inv = f
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Fire Element'
            elif playerpos == airpos + 2:
                inv = a
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Air Element'
            elif playerpos == hpos + (vtab * 2):
                h = inv
                inv = ' '
                lab[playerpos] = p
                lab[hpos] = h
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Mixing Table'
            elif playerpos == ipos + (vtab * 2):
                i = inv
                inv = ' '
                lab[playerpos] = p
                lab[ipos] = i
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Mixing Table'
            else:
                lab[playerpos] = p
                lab[hpos] = h
                lab[ipos] = i
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  [%s]' % inv
    
        elif key == 72:
            lab[playerpos] = o
            playerpos = playerpos - vtab
            if playerpos in obstacles:
                playerpos = playerpos + vtab
                lab[playerpos] = p
            elif playerpos == earthpos + 2:
                inv = e
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Earth Element'
            elif playerpos == waterpos + 2:
                inv = w
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Water Element'
            elif playerpos == firepos + 2:
                inv = f
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Fire Element'
            elif playerpos == airpos + 2:
                inv = a
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Air Element'
            elif playerpos == hpos + (vtab * 2):
                h = inv
                inv = ' '
                lab[playerpos] = p
                lab[hpos] = h
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Mixing Table'
            elif playerpos == ipos + (vtab * 2):
                i = inv
                inv = ' '
                lab[playerpos] = p
                lab[ipos] = i
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Mixing Table'
            elif playerpos == jpos - 2:
                j = inv
                inv = ' '
                lab[playerpos] = p
                lab[jpos] = j
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == kpos - 2:
                k = inv
                inv = ' '
                lab[playerpos] = p
                lab[kpos] = k
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == lpos - 2:
                l = inv
                inv = ' '
                lab[playerpos] = p
                lab[lpos] = l
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == mpos - 2:
                m = inv
                inv = ' '
                lab[playerpos] = p
                lab[mpos] = m
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == doorpos + vtab:
                if az == 25:
                    lab[playerpos] = p
                    os.system('cls')
                    riddle()
                    print
                    print ''.join(lab)
                    print '  Secrets..'
                    time.sleep(2)
                    os.system('cls')
                    p = o
                    lab[playerpos] = p
                    riddle()
                    print
                    print ''.join(lab)
                    print '  Buried secrets..'
                    time.sleep(2)
                    p = 'z'
                    dream[dreampos] = p
                    os.system('cls')
                    musicstop()
                    winsound.PlaySound("dreamsong.wav", winsound.SND_ASYNC)
                    print
                    print ''.join(dream)
                    print
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  All elements,'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  at last united..'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  But one is missing !'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  Unless..'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  The key ! Of course !'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  All these years,'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  it was just here.. '
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  Mankind,'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  mind and body,'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  the last element..'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  Now the puzzle,'
                    time.sleep(2)
                    os.system('cls')
                    print
                    print ''.join(dream)
                    print '  is complete.'
                    time.sleep(2)
                    dream[dreampos] = o
                    dreampos = 156
                    dream[dreampos] = 'z'
                    os.system('cls')
                    print
                    print ''.join(dream)
                    os.system('color 60')
                    time.sleep(0.5)
                    os.system('color 5A')
                    time.sleep(0.5)
                    os.system('color 3F')
                    time.sleep(0.5)
                    os.system('color E9')
                    time.sleep(0.5)
                    os.system('color D5')
                    time.sleep(0.5)
                    os.system('color 4B')
                    time.sleep(0.5)
                    os.system('color 8C')
                    time.sleep(0.5)
                    os.system('cls')
                    os.system('color 06')
                    time.sleep(2)
                    print 'Is this the end ?'
                    time.sleep(2)
                    os.system('cls')
                    print 'Is the search over ?'
                    time.sleep(2)
                    os.system('cls')
                    print 'Am I one ?'
                    time.sleep(2)
                    os.system('cls')
                    print 'Am I nothing ?'
                    time.sleep(2)
                    os.system('cls')
                    print 'This is the end..'
                    time.sleep(2)
                    os.system('cls')
                    print 'The universe has me now.'
                    time.sleep(2)
                    os.system('cls')
                    time.sleep(3)
                    break
                else:
                    lab[playerpos] = p
                    os.system('cls')
                    riddle()
                    print
                    print ''.join(lab)
                    print '  [%s]' % inv
                    
            else:
                lab[playerpos] = p
                lab[hpos] = h
                lab[ipos] = i
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  [%s]' % inv

        elif key == 80:
            lab[playerpos] = o
            playerpos = playerpos + vtab
            if playerpos in obstacles:
                playerpos = playerpos - vtab
                lab[playerpos] = p
            elif playerpos == earthpos + 2:
                inv = e
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Earth Element'
            elif playerpos == waterpos + 2:
                inv = w
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Water Element'
            elif playerpos == firepos + 2:
                inv = f
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Fire Element'
            elif playerpos == airpos + 2:
                inv = a
                lab[playerpos] = p
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Air Element'
            elif playerpos == jpos - 2:
                j = inv
                inv = ' '
                lab[playerpos] = p
                lab[jpos] = j
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == kpos - 2:
                k = inv
                inv = ' '
                lab[playerpos] = p
                lab[kpos] = k
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == lpos - 2:
                l = inv
                inv = ' '
                lab[playerpos] = p
                lab[lpos] = l
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            elif playerpos == mpos - 2:
                m = inv
                inv = ' '
                lab[playerpos] = p
                lab[mpos] = m
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  Assembling Table'
            else:
                lab[playerpos] = p
                lab[hpos] = h
                lab[ipos] = i
                os.system('cls')
                riddle()
                print
                print ''.join(lab)
                print '  [%s]' % inv











