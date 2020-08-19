import turtle
import time,random

def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(1)
def textdown():
    turtle.right(90)
    turtle.fd(10)
    turtle.left(90)
def textup():
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)

def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(10)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,1,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(15)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            textdown()
            turtle.write('年',align="center",font=("Yahei", 18, "normal"))
            turtle.pencolor("green")
            textup()
            turtle.fd(40)
        elif i == '=':
            textdown()
            turtle.write('月',align="center",font=("Yahei", 18, "normal"))
            turtle.pencolor("blue")
            textup()
            turtle.fd(40)
        elif i == '+':
            textdown()
            turtle.write('日',align="center",font=("Yahei", 18, "normal"))
            textup()
            turtle.fd(40)
        else:
            drawDigit(eval(i))
def all(day):
    turtle.goto(-400,-60)
    turtle.pencolor("blue")
    turtle.write('总共：',align="left",font=("Yahei", 18, "normal"))
    textup()
    turtle.fd(60)
    for j in day:
        drawDigit(eval(j))
    textdown()
    turtle.write('天',align="left",font=("Yahei", 18, "normal"))
    textup()
    hour=eval(day)*24
    min=hour*60
    sen=min*60
    turtle.goto(-360, -100)
    for i in str(hour):
        drawDigit(eval(i))
    textdown()
    turtle.write('小时',align="left",font=("Yahei", 18, "normal"))
    turtle.goto(-360, -140)
    for i in str(min):
        drawDigit(eval(i))
    textdown()
    turtle.write('分钟', align="left", font=("Yahei", 18, "normal"))
    turtle.goto(-360, -180)
    for i in str(sen):
        drawDigit(eval(i))
    textdown()
    turtle.write('秒', align="left", font=("Yahei", 18, "normal"))


def count(t1,t2,t3):
    t=t1*365
    if t2 in [1,2]:
        t+=t2*30
    if t2 in [3]:
        t=t+91
    if t2==4:
        t+=122
    if t2==5:
        t+=152
    if t2==6:
        t+=183
    if t2==7:
        t+=213
    if t2==8:
        t+=244
    if t2==9:
        t+=275
    if t2==10:
        t+=303
    if t2==11:
        t+=334
    t+=t3
    return(str(t))
def text():
    turtle.penup()
    turtle.goto(-400,240)
    turtle.pendown()
    turtle.write('你知道今天是什么日子吗？',font=("Yahei", 18, "normal"))
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-400,210)
    turtle.pendown()
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.penup()
    turtle.goto(-400,150)
    turtle.pensize(3)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.write('你还记得第一次遇见我的时间吗？',font=("Yahei", 18, "normal"))
    turtle.penup()
    turtle.goto(-400,120)
    turtle.pendown()
    turtle.pensize(3)
    drawDate('2011-09=12+')
    turtle.penup()
    turtle.goto(-400,30)
    turtle.pensize(3)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.write('哈哈！我们认识多久了？',font=("Yahei", 18, "normal"))
    turtle.penup()
    turtle.goto(0,0)
    turtle.pensize(3)
    turtle.pendown()


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def tree(length, angel, k):
    if length > 10:
        if length < 40:
            turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if 0 < length <= 30:
            turtle.pensize(2)
        elif 30 < length <= 90:
            turtle.pensize(4)
        elif 90 < length <= 160:
            turtle.pensize(8)
        else:
            turtle.pensize(16)
        turtle.fd(length)
        turtle.right(angel)
        tree(length * k, angel, k)
        turtle.left(angel * 2)
        tree(length * k, angel, k)
        if length < 40:
            turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.right(angel)
        turtle.backward(length)


def snowflake():
    turtle.begin_fill()
    turtle.colormode(255)
    turtle.color((210, random.randint(0, 255), 255), (220, 240, random.randint(0, 255)))
    for i in range(3):
        koch(20, 3)
        turtle.right(120)
    turtle.end_fill()
    turtle.up()


def main():
    turtle.setup(960, 640, 0, 0)
    turtle.speed(0)
    text()
    turtle.penup()
    turtle.fd(-240)
    turtle.pensize(3)
    t1 = time.gmtime()
    t2 = t1.tm_year - 2011
    t3 = t1.tm_mon - 5
    if t3 < 0:
        t2 -= 1
        t3 += 12
    t4 = t1.tm_mday - 10
    if t4 < 0:
        t3 -= 1
        if t1.tm_mon - 1 in [1, 3, 5, 7, 8, 10, 12]:
            t4 += 31
        else:
            t4 += 30
    tatol = count(t2, t3, t4)
    drawDate(str(t2) + '-' + str(t3) + '=' + str(t4) + '+')
    all(tatol)

    turtle.pensize(1)
    for i in range(5):
        turtle.up()
        turtle.goto(random.randint(-200, 200), random.randint(20, 220))
        turtle.down()
        snowflake()
        turtle.up()
    turtle.goto(240, -240)
    turtle.left(90)
    turtle.down()
    turtle.pensize(5)
    length = 200
    angel = 36
    k = 0.60
    tree(length, angel, k)
    turtle.hideturtle()
    turtle.done()
if __name__ == '__main__':
    main()