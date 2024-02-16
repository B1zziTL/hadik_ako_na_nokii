#naimportovanie modulu tkinter
import tkinter

#vytvorenie platna
canvas = tkinter.Canvas(width=300, height=300, background="white")
canvas.pack()

#vytvorenie prazdnych zoznamov
suradnice_x = []
suradnice_y = []
zhody = []

#zadefinovanie povodnych suradnic
x = 150
y = 150

#vlozenie zmenenych suradnic do zoznamov
suradnice_x.append(x)
suradnice_y.append(y)

#vykreslenie hada
canvas.create_line(x,y,x,y-1)

#zmena suradnice y
y -= 1

#vlozenie zmenenych suradnic do zoznamov
suradnice_x.append(x)
suradnice_y.append(y)

#zadefinovanie povodnej funkcie
funkcia = "hore"

def hore(event): #funkcia na pohnutie hore
    #zadefinovanie globalnej premennej
    global funkcia

    #zmena funkcie
    funkcia = "hore"

def dolava(event): #funkcia na pohnutie dolava
    #zadefinovanie globalnej premennej
    global funkcia

    #zmena funkcie
    funkcia = "dolava"

def doprava(event): #funkcia na pohnutie doprava
    #zadefinovanie globalnej premennej
    global funkcia

    #zmena funkcie
    funkcia = "doprava"

def dole(event): #funkcia na pohnutie dole
    #zadefinovanie globalnej premennej
    global funkcia

    #zmena funkcie
    funkcia = "dole"

def zisti_zhodu(x, y, suradnice_x, suradnice_y): #funkcia na zistenie zhody v suradniciach
    for index_x, value_x in enumerate(suradnice_x): #cyklus na prechadzanie indexu a hodnoty v zozname pre x suradnicu
        for index_y, value_y in enumerate(suradnice_y): #cyklus na prechadzanie indexu a hodnoty v zozname pre y suradnicu
            #podmienka na najdenie zhody
            if value_x == x and value_y == y:
                if index_x == index_y:
                    zhody.append((index_x, index_y))

    #vratenie zhody
    return zhody

def kresli(): #funkcia na vykreslenie hada
    #zadefinovanie globalnych premennych
    global x,y,funkcia

    #podmienka na vykreslenie ciary podla funkcie
    if funkcia == "hore":
        canvas.create_line(x,y,x,y-1)
        y -= 1

    elif funkcia == "dolava":
        canvas.create_line(x,y,x-1,y)
        x -= 1

    elif funkcia == "dole":
        canvas.create_line(x,y,x,y+1)
        y += 1

    elif funkcia == "doprava":
        canvas.create_line(x,y,x+1,y)
        x += 1

    #zadefinovanie zhody
    zhody = zisti_zhodu(x, y, suradnice_x, suradnice_y)

    #podmienka na ukoncenie programu
    if zhody:
        for index_x, index_y in zhody:
            return
                
    
    #vlozenie zmenenych suradnic do zoznamov
    suradnice_x.append(x)
    suradnice_y.append(y)

    #opakovanie funkcie po 200 ms
    canvas.after(200,kresli)

#zavolanie funkcie
kresli()

#nabindovanie klavesov k funkciam
canvas.bind_all("w",hore)
canvas.bind_all("a",dolava)
canvas.bind_all("s",dole)
canvas.bind_all("d",doprava)


