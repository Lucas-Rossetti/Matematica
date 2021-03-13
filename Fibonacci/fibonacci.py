# Imports
import turtle, time

# Número de iterações
tn = int(input("Número: "))

s = turtle.getscreen()
t = turtle.Turtle()

# Velocidade
t.speed(50)

# Valores iniciais dos números
n1 = 0
n2 = 1
n = n1 + n2

# Primeiro quadrado
t.fd(n2)
t.lt(90)
t.fd(n2)
t.lt(90)
t.fd(n2)
t.lt(90)
t.fd(n2)

# Valores se somam e alteram
n1 = n2
n2 = n
n = n1 + n2

for i in range(tn):
    # Quadrado de n2 de lado
    t.bk(n1)
    t.rt(90)
    t.fd(n2)
    t.lt(90)
    t.fd(n2)
    t.lt(90)
    t.fd(n2)

    # Valores se somam e alteram
    n1 = n2
    n2 = n
    n = n1 + n2

# Ponta vai para o centro para desenhar espiral
t.penup()
t.goto(1, 0)
time.sleep(1)
t.pendown()

# Descobre quantos graus a ponta precisa girar baseado onde ficou o último quadrado desenhado
d = tn/4
d = str(d).split(".")

if d[1] == "0":
    t.rt(180)   
elif d[1] == "25":
    t.rt(270)
elif d[1] == "50":
    t.rt(360)
elif d[1] == "75":
    t.rt(90)

# Valores iniciais
n1 = 0
n2 = 1
n = n1 + n2

# Primeiro círculo
t.circle(n2, 90)

# Valores se somam e alteram
n1 = n2
n2 = n
n = n1 + n2

for i in range(tn):
    # Círculo com n2 de diâmetro
    t.circle(n2, 90)
    
    # Valores se somam e alteram
    n1 = n2
    n2 = n
    n = n1 + n2

# Fica com a tela aberta por mais um tempo
time.sleep(5)
