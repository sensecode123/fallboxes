import pygame
import pygame.freetype

pygame.init()
pygame.freetype.init()
pygame.mixer.init()

#window 
width, height = 600, 600
win = pygame.display.set_mode((width, height))
icon = pygame.image.load("ic.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Fall Box")

#rects
p1 = pygame.Rect(250, 20, 100, 50)
p11 = pygame.Rect(250, 20, 100, 50)
p2 = pygame.Rect(280, 500, 50, 50)
p3 = pygame.Rect(480, 500, 40, 40)
p4 = pygame.Rect(80, 500, 40, 40)
wins = pygame.Rect(0, 570, 600, 30)

bull = pygame.Rect(290, 470, 25, 25)
bull2 = pygame.Rect(486, 470, 20,20)
bull3 = pygame.Rect(86, 470, 20, 20)

#text
f1 = pygame.freetype.Font("font.ttf", 28)
w1 = pygame.freetype.Font("font.ttf", 80)
e1 = pygame.freetype.Font("font.ttf", 60)
e2 = pygame.freetype.Font("font.ttf", 40)

#Health and levels
levels = 1
levels2 = 2
levels3 = 3
levels4 = 4
levels5 = 5
levels6 = 6
levels7 = 7
levels8 = 8
levels9 = 9
levels10 = 10
back = pygame.Rect(10, 10, 200, 100)

#sound
s1 = pygame.mixer.Sound("lose.wav")
s2 = pygame.mixer.Sound("ball.wav")
music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

def draw1(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), p1)
    pygame.draw.rect(win, (150, 9, 9), p2)
    pygame.draw.rect(win, (150, 9, 9), p3)
    pygame.draw.rect(win, (150, 9, 9), p4)
    pygame.draw.rect(win, (150, 9, 9), bull)
    pygame.draw.rect(win, (150, 9, 9), bull2)
    pygame.draw.rect(win, (150, 9, 9), bull3)
    pygame.draw.rect(win, (217, 217, 217), wins)

    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40, 40))
    f1.render_to(win, (20, 50), "Hits: " + str(hit), (40, 40, 40))
    f1.render_to(win, (20, 80), "Level: " + str(levels), (40, 40, 40))
    pygame.display.update()

def move():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and p1.x > 7:
        p1.x -= 2

    if key[pygame.K_RIGHT] and p1.x + p1.width + 7 <  width:
        p1.x += 2

def draw_loser(text):
    draw_text = w1.render_to(win, (150, 200), text, (0,0, 0))
    pygame.display.update()
    pygame.time.delay(2000)

#level2
#rects
p12 = pygame.Rect(280, 20, 40, 40)
p22 = pygame.Rect(220, 500, 80, 20)
p32 = pygame.Rect(420, 500, 80, 20)
p42 = pygame.Rect(360, 500, 40, 20)
p52 = pygame.Rect(40, 500, 100, 20)

bulle = pygame.Rect(246, 460, 40, 20)
bulle2 = pygame.Rect(436, 460, 40, 20)
bulle3 = pygame.Rect(366, 460, 20, 10)
bulle4 = pygame.Rect(62, 460, 50, 20)

#draw
def draw2(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), p12)
    pygame.draw.rect(win, (150, 9, 9), p22)
    pygame.draw.rect(win, (150, 9, 9), p32)
    pygame.draw.rect(win, (150, 9, 9), p42)
    pygame.draw.rect(win, (150, 9, 9), p52)
    pygame.draw.rect(win, (217, 217, 217), wins)

    pygame.draw.rect(win, (150, 9, 9), bulle)
    pygame.draw.rect(win, (150, 9, 9), bulle2)
    pygame.draw.rect(win, (150, 9, 9), bulle3)
    pygame.draw.rect(win, (150, 9, 9), bulle4)

    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40,40))
    f1.render_to(win, (20, 50), "Hits: " + str(hit), (40, 40, 40))
    f1.render_to(win, (20, 80), "Level: " + str(levels2), (40, 40, 40))
    pygame.display.update()

def move2():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and p12.x > 7:
        p12.x -= 2.5

    if key[pygame.K_RIGHT] and p12.x + p12.width + 7 < width:
        p12.x += 2.5

#level3
#rect
pl1 = pygame.Rect(290, 20, 50, 50)
pl2 = pygame.Rect(0, 500, 90, 40)
pl3 = pygame.Rect(510, 500, 90, 40)
pl4 = pygame.Rect(150, 500, 64, 40)
pl5 = pygame.Rect(290, 500, 54, 40)
pl6 = pygame.Rect(400, 500, 64, 40)

bullf = pygame.Rect(20, 460, 40, 20)
bullf2 = pygame.Rect(536, 460, 40, 20)
bullf3 = pygame.Rect(166, 460, 30, 20)
bullf4 = pygame.Rect(306, 460, 25, 20)
bullf5 = pygame.Rect(416, 460, 30, 20)
#draw
def draw3(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), pl1)
    pygame.draw.rect(win, (150, 9, 9), pl2)
    pygame.draw.rect(win, (150, 9, 9), pl3)
    pygame.draw.rect(win, (150, 9, 9), pl4)
    pygame.draw.rect(win, (150, 9, 9), pl5)
    pygame.draw.rect(win, (150, 9, 9), pl6)

    pygame.draw.rect(win, (150, 9, 9), bullf)
    pygame.draw.rect(win, (150, 9, 9), bullf2)
    pygame.draw.rect(win, (150, 9, 9), bullf3)
    pygame.draw.rect(win, (150, 9, 9), bullf4)
    pygame.draw.rect(win, (150, 9, 9), bullf5)
    pygame.draw.rect(win, (217, 217, 217), wins)

    f1.render_to(win, (20, 20), "Health:" + str(health), (40, 40,40))
    f1.render_to(win, (20, 50), "Hits: " + str(hit), (40, 40, 40))
    f1.render_to(win, (20, 80), "Level: " + str(levels3), (40, 40, 40))
    pygame.display.update()

#move
def move3():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pl1.x > 7:
        pl1.x -= 3.2

    if key[pygame.K_RIGHT] and pl1.x + pl1.width + 7 <  width:
        pl1.x += 3.2

#level 4
#rects
pc1 = pygame.Rect(300, 20, 50, 60)
pc2 = pygame.Rect(510, 450, 90, 40)
pc3 = pygame.Rect(0, 450, 90, 40)
pc4 = pygame.Rect(150, 500, 300, 40)

bullg = pygame.Rect(100, 456, 35, 15)
bullg2 = pygame.Rect(470, 456, 35, 15)
bullg3 = pygame.Rect(200, 470, 40, 20)
bullg4 = pygame.Rect(280, 470, 40, 20)
bullg5 = pygame.Rect(360, 470, 40, 20)

#draw
def draw4(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (150, 9, 9), pc2)
    pygame.draw.rect(win, (9, 9, 43), pc1)
    pygame.draw.rect(win, (150, 9, 9), pc3)
    pygame.draw.rect(win, (150, 9, 9), pc4)
    pygame.draw.rect(win, (217, 217, 217), wins)

    pygame.draw.rect(win, (150, 9, 9), bullg)
    pygame.draw.rect(win, (150, 9, 9), bullg2)
    pygame.draw.rect(win, (150, 9, 9), bullg3)
    pygame.draw.rect(win, (150, 9, 9), bullg4)
    pygame.draw.rect(win, (150, 9, 9), bullg5)

    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40,40))
    f1.render_to(win, (20,50), "Hits: " + str(hit), (40, 40, 40))
    f1.render_to(win, (20, 80), "Level: " + str(levels4), (40, 40, 40))
    pygame.display.update()

#move
def move4():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pc1.x > 7:
        pc1.x -= 3.2

    if key[pygame.K_RIGHT] and pc1.x + pc1.width +7 < width:
        pc1.x += 3.2

def drawi():
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (9, 9, 43), p11)
    e1.render_to(win, (24, 200), "WELCOME TO FALL BOXES", (132, 132, 130))
    e2.render_to(win, (140, 250), "PRESS SPACE TO START",  (132, 132, 130))

    pygame.display.update()

#level5
#rects
pd1 = pygame.Rect(270, 20, 38, 50)
pd2 = pygame.Rect(266, 500, 70, 30)
pd3 = pygame.Rect(0, 430, 90, 40)
pd4 = pygame.Rect(510, 430, 90, 40)
pd5 = pygame.Rect(136, 500, 112, 40)
pd6 = pygame.Rect(355, 500, 112, 40)

bullh = pygame.Rect(100, 448, 35, 15)
bullh2 = pygame.Rect(470, 448, 35, 15)
bullh3 = pygame.Rect(360, 470, 30, 20)
bullh4 = pygame.Rect(400, 470, 30, 20)
bullh5 = pygame.Rect(180, 470, 30, 20)
bullh6 = pygame.Rect(220, 470, 30, 20)
#draw
def draw5(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), pd1)
    pygame.draw.rect(win, (150, 9, 9), pd2)
    pygame.draw.rect(win, (150, 9, 9), pd3)
    pygame.draw.rect(win, (150, 9, 9), pd4)
    pygame.draw.rect(win, (150, 9, 9), pd5)
    pygame.draw.rect(win, (150, 9, 9), pd6)

    pygame.draw.rect(win, (150, 9, 9), bullh)
    pygame.draw.rect(win, (150, 9, 9), bullh2)
    pygame.draw.rect(win, (150, 9, 9), bullh3)
    pygame.draw.rect(win, (150, 9, 9), bullh4)
    pygame.draw.rect(win, (150, 9, 9), bullh5)
    pygame.draw.rect(win, (150, 9, 9), bullh6)

    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40,40))
    f1.render_to(win, (20,50), "Hits: " + str(hit), (40, 40, 40))
    f1.render_to(win, (20, 80), "Level: " + str(levels5), (40, 40, 40))
    pygame.draw.rect(win, (217, 217, 217), wins)
    pygame.display.update()

#move
def move5():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pd1.x > 7:
        pd1.x -= 3.2

    if key[pygame.K_RIGHT] and pd1.x + pd1.width + 7 < width:
        pd1.x += 3.2

#level6
#rects
pe1 = pygame.Rect(280, 20, 50, 30)
pe2 = pygame.Rect(0, 430, 90, 40)
pe3 = pygame.Rect(510, 430, 90, 40)
pe4 = pygame.Rect(270, 320, 60, 40)
pe5 = pygame.Rect(100, 320, 260, 40)
pe6 = pygame.Rect(450, 320, 100, 40)
pe7 = pygame.Rect(490, 500, 100, 20)
pe8 = pygame.Rect(290, 500, 100, 20)

bulli = pygame.Rect(470, 438, 35, 15)
bulli2 = pygame.Rect(290, 310, 22, 10)
bulli3 = pygame.Rect(106, 290, 100, 20)
bulli4 = pygame.Rect(480, 340, 35, 15)
bulli5 = pygame.Rect(305, 500, 40,20)

#draw
def draw6(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), pe1)
    pygame.draw.rect(win, (150, 9, 9), pe2)
    pygame.draw.rect(win, (150, 9, 9), pe3)
    pygame.draw.rect(win, (150, 9, 9), pe4)
    pygame.draw.rect(win, (150, 9, 9), pe5)
    pygame.draw.rect(win, (150, 9, 9), pe6)
    pygame.draw.rect(win, (150, 9, 9), pe7)
    pygame.draw.rect(win, (150, 9, 9), pe8)
    pygame.draw.rect(win, (217, 217, 217), wins)

    pygame.draw.rect(win, (150, 9, 9), bulli2)
    pygame.draw.rect(win, (150, 9, 9), bulli)
    pygame.draw.rect(win, (150, 9, 9), bulli3)
    pygame.draw.rect(win, (150, 9, 9), bulli4)
    pygame.draw.rect(win, (150, 9, 9), bulli5)

    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40,40))
    f1.render_to(win, (20, 50), "Hits: " + str(hit), (40, 40,40))
    f1.render_to(win, (20, 80), "Level: " + str(levels6), (40, 40, 40))
    pygame.display.update()

#move
def move6():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pe1.x > 7:
        pe1.x -= 3.2

    if key[pygame.K_RIGHT] and pe1.x + pe1.width + 7 < width:
        pe1.x += 3.2

#level7
#rects
pf1 = pygame.Rect(280, 20, 50, 30)
pf2 = pygame.Rect(0, 430, 90, 40)
pf3 = pygame.Rect(510, 430, 90, 40)
pf4 = pygame.Rect(270, 320, 60, 40)
pf5 = pygame.Rect(100, 320, 260, 40)
pf6 = pygame.Rect(450, 320, 100, 40)
pf7 = pygame.Rect(500, 500, 100, 20)
pf8 = pygame.Rect(300, 500, 100, 20)

bullj1 = pygame.Rect(460, 500, 32, 20)
bullj2 = pygame.Rect(106, 290, 100, 20)
bullj3 = pygame.Rect(460, 440, 40,20)
bullj4 = pygame.Rect(400, 330, 30, 15)

#draw
def draw7(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), pf1)
    pygame.draw.rect(win, (150, 9, 9), pf2)
    pygame.draw.rect(win, (150, 9, 9), pf3)
    pygame.draw.rect(win, (150, 9, 9), pf4)
    pygame.draw.rect(win, (150, 9, 9), pf5)
    pygame.draw.rect(win, (150, 9, 9), pf6)
    pygame.draw.rect(win, (150, 9, 9), pf7)
    pygame.draw.rect(win, (150, 9, 9), pf8)
    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40,40))
    f1.render_to(win, (20, 50), "Hits: " + str(hit), (40, 40,40))
    f1.render_to(win, (20, 80), "Level: " + str(levels7), (40, 40, 40))
    pygame.draw.rect(win, (217, 217, 217), wins)

    pygame.draw.rect(win, (150, 9, 9), bullj3)
    pygame.draw.rect(win, (150, 9, 9), bullj4)
    pygame.draw.rect(win, (150, 9, 9), bullj2)
    pygame.draw.rect(win, (150, 9, 9), bullj1)
    pygame.display.update()


#move
def move7():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pf1.x > 7:
        pf1.x -= 3.2

    if key[pygame.K_RIGHT] and pf1.x + pf1.width + 7 < width:
        pf1.x += 3.2

#level8
#draw level
#rects
pg1 = pygame.Rect(280, 20, 30, 40)
pg2 = pygame.Rect(280, 500, 60, 40)
pg3 = pygame.Rect(170, 500, 60, 40)
pg4 = pygame.Rect(380, 500, 60, 40)
pg5 = pygame.Rect(530, 430, 70, 40)
pg6 = pygame.Rect(0, 430, 70, 40)

bullk1 = pygame.Rect(495, 440, 25,15)
bullk2 = pygame.Rect(80, 440, 25,15)

def draw8(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), pg1)
    pygame.draw.rect(win, (150, 9, 9), pg2)
    pygame.draw.rect(win, (150, 9, 9), pg3)
    pygame.draw.rect(win, (150, 9, 9), pg4)
    pygame.draw.rect(win, (150, 9, 9), pg5)
    pygame.draw.rect(win, (150, 9, 9), pg6)
    pygame.draw.rect(win, (150, 9, 9), bullk1)
    pygame.draw.rect(win, (150, 9, 9), bullk2)
    pygame.draw.rect(win, (217, 217, 217), wins)

    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40,40))
    f1.render_to(win, (20, 50), "Hits: " + str(hit), (40, 40,40))
    f1.render_to(win, (20, 80), "Level: " + str(levels8), (40, 40, 40))
    pygame.display.update()

#move
def move8():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pg1.x > 7:
        pg1.x -= 3.2

    if key[pygame.K_RIGHT] and pg1.x + pg1.width + 7 < width:
        pg1.x += 3.2

#level9
#rects
ph1 = pygame.Rect(280, 20, 36, 40)
ph2 = pygame.Rect(290, 500, 60, 40)
ph3 = pygame.Rect(180, 500, 70, 40)
ph4 = pygame.Rect(390, 500, 60, 40)

ph5 = pygame.Rect(530, 430, 70, 40)
ph6 = pygame.Rect(0, 430, 70, 40)
bullm1 = pygame.Rect(495, 440, 15,15)
bullm2 = pygame.Rect(80, 440, 15,15)

bullm3 = pygame.Rect(565, 390, 20,15)
bullm4 = pygame.Rect(20, 390, 20,15)
#draw
def draw9(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), ph1)
    pygame.draw.rect(win, (150, 9, 9), ph2)
    pygame.draw.rect(win, (150, 9, 9), ph3)
    pygame.draw.rect(win, (150, 9, 9), ph4)
    pygame.draw.rect(win, (150, 9, 9), ph5)
    pygame.draw.rect(win, (150, 9, 9), ph6)

    pygame.draw.rect(win, (150, 9, 9), bullm1)
    pygame.draw.rect(win, (150, 9, 9), bullm2)
    pygame.draw.rect(win, (150, 9, 9), bullm3)
    pygame.draw.rect(win, (150, 9, 9), bullm4)
    

    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40,40))
    f1.render_to(win, (20, 50), "Hits: " + str(hit), (40, 40,40))
    f1.render_to(win, (20, 80), "Level: " + str(levels9), (40, 40, 40))
    pygame.display.update()

#move
def move9():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and ph1.x > 7:
        ph1.x -= 3.2

    if key[pygame.K_RIGHT] and ph1.x + ph1.width + 7 < width:
        ph1.x += 3.2

#level10
#rects
pi1 = pygame.Rect(280, 20, 45, 40)
pi2 = pygame.Rect(280, 300, 60, 40)
pi3 = pygame.Rect(530, 430, 70, 40)
pi4 = pygame.Rect(0, 430, 70, 40)
pi5 = pygame.Rect(150, 500, 300, 40)

bulln = pygame.Rect(290, 270, 21, 20)
bulln2 = pygame.Rect(495, 440, 20,15)
bulln3 = pygame.Rect(80, 440, 20,15)

#draw
def draw10(health, hit):
    win.fill((217, 217, 217))
    pygame.draw.rect(win, (200, 200, 200), back)
    pygame.draw.rect(win, (9, 9, 43), pi1)
    pygame.draw.rect(win, (150, 9, 9), pi2)
    pygame.draw.rect(win, (150, 9, 9), pi3)
    pygame.draw.rect(win, (150, 9, 9), pi4)
    pygame.draw.rect(win, (150, 9, 9), pi5)
    pygame.draw.rect(win, (150, 9, 9), bulln)
    pygame.draw.rect(win, (150, 9, 9), bulln2)
    pygame.draw.rect(win, (150, 9, 9), bulln3)

    f1.render_to(win, (20, 20), "Health: " + str(health), (40, 40,40))
    f1.render_to(win, (20, 50), "Hits: " + str(hit), (40, 40,40))
    f1.render_to(win, (20, 80), "Level: " + str(levels10), (40, 40, 40))
    pygame.display.update()

#move
def move10():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and pi1.x > 7:
        pi1.x -= 3.2

    if key[pygame.K_RIGHT] and pi1.x + pi1.width + 7 < width:
        pi1.x +=3.2

#finished
t1 = pygame.freetype.Font("font.ttf", 50)
t2 = pygame.freetype.Font("font.ttf", 40)
t3 = pygame.freetype.Font("font.ttf", 35)

#level manager
class level():
    def entry():
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        level.level1()

            p11.y += 2
            if p11.y >= 600:
                p11.y = 20

            drawi()

        pygame.quit()

    def level1():
        run = True
        health = 10
        hit = 0
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            p1.y += 2
            if p1.y >= 600:
                level.level2()

            bull.y -= 1.5
            bull2.y -= 1.5
            bull3.y -= 1.5
            if bull.y == 0:
                bull.y = 470

            if bull2.y == 0:
                bull2.y = 470

            if bull3.y == 0:
                bull3.y = 470

            if p1.colliderect(p2):
                p1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p1.colliderect(p3):
                p1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p1.colliderect(p4):
                p1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p1.colliderect(bull):
                p1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p1.colliderect(bull2):
                p1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p1.colliderect(bull3):
                p1.y = 20
                health -= 1
                s2.play()
                hit += 1

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level1()


            draw1(health, hit)
            move()

        pygame.quit()

    def level2():
        run = True
        health = 10
        hit = 0
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            p12.y += 3
            if p12.y >= 600:
                level.level3()

            bulle.y -= 2.5
            bulle2.y -= 2.5
            bulle3.y -= 2.5
            bulle4.y -= 2.5

            if bulle.y <= 0:
                bulle.y = 460

            if bulle2.y <= 0:
                bulle2.y = 460

            if bulle3.y <= 0:
                bulle3.y = 460

            if bulle4.y <= 0:
                bulle4.y = 460

            if p12.colliderect(p22):
                p12.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p12.colliderect(p32):
                p12.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p12.colliderect(p42):
                p12.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p12.colliderect(p52):
                p12.y = 20
                health -= 1
                s2.play()
                hit += 1
        

            if p12.colliderect(bulle):
                p12.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p12.colliderect(bulle2):
                p12.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p12.colliderect(bulle3):
                p12.y = 20
                health -= 1
                s2.play()
                hit += 1

            if p12.colliderect(bulle4):
                p12.y = 20
                health -= 1
                s2.play()
                hit += 1

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level2()


            draw2(health, hit)
            move2()
                
        pygame.quit()


    def level3():
        run = True
        health = 10
        hit = 0
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pl1.y += 4
            if pl1.y >= 600:
                level.level4()

            bullf.y -= 3.8
            bullf2.y -= 3.8
            bullf3.y -= 3.8
            bullf4.y -= 3.8
            bullf5.y -= 3.8

            if bullf.y <= 0:
                bullf.y = 460

            if bullf2.y <= 0:
                bullf2.y = 460

            if bullf3.y <= 0:
                bullf3.y = 460

            if bullf4.y <= 0:
                bullf4.y = 460

            if bullf5.y <= 0:
                bullf5.y = 460

            if pl1.colliderect(pl2):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pl1.colliderect(pl3):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pl1.colliderect(pl4):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pl1.colliderect(pl5):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pl1.colliderect(pl6):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pl1.colliderect(bullf):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pl1.colliderect(bullf2):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pl1.colliderect(bullf3):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pl1.colliderect(bullf4):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1
             
            if pl1.colliderect(bullf5):
                pl1.y = 20
                health -= 1
                s2.play()
                hit += 1

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level3()

            draw3(health, hit)
            move3()

        pygame.quit()

    def level4():
        run = True
        health = 10
        hit = 0
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pc1.y = 2

            pc1.y += 4.2
            if pc1.y >= 600:
                level.level5()

            bullg.x += 3
            bullg2.x -= 3

            if bullg.x >= 600:
                bullg.x = 100

            if bullg2.x <= 0:
                bullg2.x = 470

            if pc1.colliderect(pc2):
                pc1.y = 20
                health -= 1
                s2.play()
                hit += 1
            
            
            if pc1.colliderect(pc3):
                pc1.y = 20
                health -= 1
                s2.play()
                hit += 1

            
            if pc1.colliderect(pc4):
                pc1.y = 20
                health -= 1
                s2.play()
                hit += 1

            bullg3.y -= 3.9
            bullg4.y -= 3.9
            bullg5.y -= 3.9

            if bullg3.y <= 0:
                bullg3.y = 470

            if bullg4.y <= 0:
                bullg4.y = 470

            if bullg5.y <= 0:
                bullg5.y = 470

            
            if pc1.colliderect(bullg):
                pc1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if pc1.colliderect(bullg2):
                pc1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if pc1.colliderect(bullg3):
                pc1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if pc1.colliderect(bullg4):
                pc1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if pc1.colliderect(bullg5):
                pc1.y = 20
                s2.play()
                health -= 1
                hit += 1

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level4()

            draw4(health, hit)
            move4()

        pygame.quit()

    def level5():
        run = True
        health = 10
        hit = 0
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pd1.y = 2
            
            pd1.y += 4.2
            if pd1.y >= 600:
                level.level6()

            pd2.height += 1.4
            pd2.y -= 0.9

            if pd2.y == 20:
                pd2.y = 500
            pd2.y + pd2.height + 60 < height


            bullh.x += 3.5
            bullh2.x -= 3.5
            bullh3.y -= 4.1
            bullh4.y -= 4.1
            bullh5.y -= 4.1
            bullh6.y -= 4.1

            if bullh3.y <= 0 and bullh4.y <= 0:
                bullh3.y = 470
                bullh4.y = 470

            if bullh5.y <= 0 and bullh6.y <= 0:
                bullh5.y = 470
                bullh6.y = 470

            
            if bullh.x > 600:
                bullh.x = 100

            if bullh2.x <= 0:
                bullh2.x = 470

            if pd1.colliderect(pd2):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(pd3):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(pd4):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(pd5):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(pd6):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(bullh):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(bullh2):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(bullh3):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(bullh4):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(bullh5):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pd1.colliderect(bullh6):
                pd1.y = 20
                health -= 1
                s2.play()
                hit += 1

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level5()

            draw5(health, hit)
            move5()

        pygame.quit()

    def level6():
        run = True
        health = 10
        hit = 0
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pe1.y = 2

            pe2.width += 2.5

            if pe2.width > 510:
                pe2.width = 90

            bulli.x -= 4
            bulli2.y -= 4.2
            bulli3.y -= 4.2
            bulli4.x -= 4.2
            bulli5.x -= 3.8

            if bulli4.x <= 0:
                bulli4.x = 460

            if bulli5.x <= 0:
                bulli5.x = 460

            if bulli.x <= 0:
                bulli.x = 470

            if bulli2.y <= 0:
                bulli2.y = 310

            if bulli3.y <= 0:
                bulli3.y = 290

            pe1.y += 4.4
            if pe1.y >= 600:
                level.level7()

            if pe1.colliderect(pe3):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pe1.colliderect(pe2):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pe1.colliderect(pe4):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            
            if pe1.colliderect(pe5):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pe1.colliderect(pe6):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pe1.colliderect(pe7):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            
            if pe1.colliderect(pe8):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pe1.colliderect(bulli):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pe1.colliderect(bulli2):
                pe1.x = 70
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pe1.colliderect(bulli3):
                pe1.x = 280
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            if pe1.colliderect(bulli4):
                pe1.y = 20
                health -= 1
                s2.play()
                hit += 1

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level6()

            draw6(health, hit)
            move6()

        pygame.quit()

    def level7():
        run = True
        clock = pygame.time.Clock()
        health = 10
        hit = 0
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pf1.y = 2

            if pf1.colliderect(pf4):
                pf1.x -= 120
                s2.play()
                health -= 1  
                hit += 1

            pf4.height += 2.5
            pf4.y -= 1.5
            if pf4.height >= 300:
                pf4.height = 40

            if pf4.y <= 20:
                pf4.y = 320

            pf2.width += 2.8 
            if pf2.width == 510:
                pf2.width = 90  

            bullj3.x -= 4.2
            bullj4.x -= 4.2
            bullj1.x -= 3.8
            if bullj3.x <= 0:
                bullj3.x = 460  

            if bullj4.x <= 0:
                bullj4.x = 400  

            if bullj1.x <= 0:
                bullj1.x = 400  

            bullj2.y -= 4.2
            if bullj2.y <= 0:
                bullj2.y = 290

            if bullj2.colliderect(pf1):
                pf1.x = 280 
                s2.play()
                health -= 1 
                hit += 1 

            pf1.y += 4.4
            if pf1.y >= 600:
                level.level8() 

            if pf1.colliderect(pf2):
                pf1.y = 20
                s2.play()
                health -= 1
                hit += 1  

            if pf1.colliderect(pf3):
                s2.play()
                pf1.y = 20
                health -= 1  
                hit += 1

            if pf1.colliderect(pf5):
                pf1.y = 20
                s2.play()
                health -= 1  
                hit += 1   

            if pf1.colliderect(pf6):
                pf1.y = 20
                s2.play()
                health -= 1 
                hit += 1    

            if pf1.colliderect(pf7):
                pf1.y = 20
                s2.play()
                health -= 1 
                hit += 1    

            if pf1.colliderect(pf8):
                pf1.y = 20 
                s2.play()
                health -= 1  
                hit += 1   

            if pf1.colliderect(bullj3):
                pf1.y = 20
                s2.play()
                health -= 1  
                hit+= 1   

            if pf1.colliderect(bullj2):
                pf1.y = 20
                s2.play() 
                health -= 1 
                hit += 1 

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level7()   

            draw7(health, hit)
            move7()

        pygame.quit()  

    def level8():
        run = True
        health = 10
        hit = 0
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pg1.y = 2

                    if event.key == pygame.K_r:
                        level.level8()

            pg1.y += 4.4

            pg2.height += 3
            pg2.y -= 2

            if pg2.y == 40:
                pg2.y = 500

            pg3.height += 3
            pg3.y -= 2

            if pg3.y == 40:
                pg3.y = 500

            pg4.height += 3
            pg4.y -= 2

            if pg4.y == 40:
                pg4.y = 500

            if pg1.colliderect(pg2):
                pg1.y = 20
                pg1.x = 170
                health -= 1
                s2.play()
                hit += 1

            if pg1.colliderect(pg3):
                pg1.y = 20
                health -= 1
                pg1.x = 380
                s2.play()
                hit += 1

            if pg1.colliderect(pg4):
                pg1.y = 20
                health -= 1
                pg1.x= 280
                s2.play()
                hit += 1
    
            if pg1.colliderect(pg5):
                pg1.y = 20
                health -= 1
                pg1.x = 280
                s2.play()
                hit += 1
                pg1.x = 280

            if pg1.colliderect(bullk1):
                pg1.y = 20
                health -= 1
                s2.play()
                hit += 1
                pg1.x = 280

            if pg1.colliderect(bullk2):
                pg1.y = 20
                health -= 1
                s2.play()
                hit += 1
                pg1.x = 280

            if pg1.colliderect(pg6):
                pg1.y = 20
                pg1.x = 280
                health -= 1
                s2.play()
                hit += 1
                pg1.x = 280

            if pg1.y >= 600:
                level.level9()

            bullk1.x -= 1
            bullk2.x += 1
            if bullk1.colliderect(pg4):
                bullk1.x = 495

            if bullk2.colliderect(pg3):
                bullk2.x = 80

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level8()   



            draw8(health, hit)
            move8()

        pygame.quit() 

    def level9():
        run = True
        hit = 0
        health = 10
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ph1.y = 2

            ph1.y += 4.4

            ph2.height += 3
            ph2.y -= 2

            if ph2.y == 40:
                ph2.y = 500

            ph3.height += 3
            ph3.y -= 2

            if ph3.y == 40:
                ph3.y = 500

            ph4.height += 3
            ph4.y -= 2

            if ph4.y == 40:
                ph4.y = 500

            if ph1.colliderect(ph2):
                ph1.y = 20
                ph1.x = 170
                health -= 1
                s2.play()
                hit += 1

            if ph1.colliderect(ph3):
                ph1.y = 20
                health -= 1
                ph1.x = 380
                s2.play()
                hit += 1

            if ph1.colliderect(ph4):
                ph1.y = 20
                health -= 1
                ph1.x= 280
                s2.play()
                hit += 1

            if ph1.colliderect(ph5):
                ph1.y = 20
                health -= 1
                ph1.x= 280
                s2.play()
                hit += 1

            if ph1.colliderect(ph6):
                ph1.y = 20
                health -= 1
                ph1.x= 280
                s2.play()
                hit += 1

            if ph1.colliderect(bullm1):
                ph1.y = 20
                health -= 1
                ph1.x= 280
                s2.play()
                hit += 1

            if ph1.colliderect(bullm2):
                ph1.y = 20
                health -= 1
                ph1.x= 280
                s2.play()
                hit += 1

            if ph1.colliderect(bullm3):
                ph1.y = 20
                health -= 1
                ph1.x= 280
                s2.play()
                hit += 1

            if ph1.colliderect(bullm4):
                ph1.y = 20
                health -= 1
                ph1.x= 280
                s2.play()
                hit += 1

            bullm1.x -= 2
            bullm2.x += 2
            bullm3.x -= 1.5
            bullm4.x += 1.5
            if bullm1.colliderect(ph4):
                bullm1.x = 495

            if bullm2.colliderect(ph3):
                bullm2.x = 40

            if bullm3.colliderect(ph2):
                bullm3.x = 565

            if bullm4.colliderect(ph2):
                bullm4.x = 40

            if ph1.y >= 600:
                level.level10()

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level9()   

            
            draw9(health, hit)
            move9()

        pygame.quit()   

    def level10():
        run = True
        health = 10
        hit = 0
        clock = pygame.time.Clock()
        while run:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pi1.y = 2

            pi1.y += 4.4
            pi2.x -= 3.5

            if pi2.x <= 20:
                pi2.x = 510

            bulln.y -= 4
            bulln2.x -= 4
            bulln3.x += 4
            if bulln.y <= 20:
                bulln.y = 270

            if pi1.colliderect(pi2):
                pi1.x = 280
                pi1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if pi1.colliderect(bulln):
                pi1.x = 280
                pi1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if bulln2.colliderect(pi4):
                bulln2.x = 495

            if bulln3.colliderect(pi3):
                bulln3.x = 80

            if pi1.colliderect(pi3):
                pi1.y = 20
                pi1.x = 280
                s2.play()
                health -= 1
                hit += 1

            if pi1.colliderect(pi4):
                pi1.y = 20
                pi1.x = 280
                s2.play()
                health -= 1
                hit += 1

            if pi1.colliderect(bulln2):
                pi1.x = 280
                pi1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if pi1.colliderect(bulln3):
                pi1.x = 280
                pi1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if pi1.colliderect(pi5):
                pi1.x = 280
                pi1.y = 20
                s2.play()
                health -= 1
                hit += 1

            if pi1.y >= 600:
                level.fin()

            loser_text = ""
            if health <= 0:
                loser_text = "YOU LOSE!"
                s2.stop()
                s1.play()

            if loser_text != "":
                draw_loser(loser_text)
                level.level10()   


            draw10(health, hit)
            move10()

        pygame.quit()  

    def fin():
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        level.level1()

                    if event.key == pygame.K_q:
                        pygame.quit()
            
            win.fill((217, 217, 217))
            t1.render_to(win, (20, 200), "YOU FINISHED ALL THE LEVELS!")
            t2.render_to(win, (100, 245), "PRESS SPACE TO DO IT AGAIN")
            t3.render_to(win, (180, 290), "PRESS Q TO QUIT")

            pygame.display.update()

        pygame.quit()    

def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(120)
        level.entry()

if __name__ == "__main__":
    main()
