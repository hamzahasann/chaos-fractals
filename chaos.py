import sys
import pygame
import random

#COLOURS
BLACK=(0,0,0)
WHITE=(200,200,200)
RED=(128,0,0)
GREEN=(0,128,0)
BLUE=(0,0,128)

#DISPLAY
FPS=60
SCREEN_W=1024
SCREEN_H=768
SCREEN=pygame.display.set_mode([SCREEN_W,SCREEN_H])

#CONSTANTS
tpnt=3
R=0.5
point=[]
def main():
    # tpnt=3
    iter=0
    cnt=0
    p=[0,0]
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1) and cnt<=tpnt:
                i,j=pygame.mouse.get_pos()
                create_point(i,j)
                p=[i,j]
                if(cnt<tpnt):
                    point.append([i,j])
                cnt+=1
                # print(point)
        if cnt>tpnt:
            r=random.randint(0,tpnt-1)
            q=point[r]
            p=[p[0]+int(R*(q[0]-p[0])),p[1]+int(R*(q[1]-p[1]))]
            create_point(p[0],p[1])
            iter+=1
            # create_text("iter = {}".format(iter),SCREEN_W/2,SCREEN_H/10)
        pygame.display.update()
        Clock.tick(FPS)

def create_point(i,j):
    pygame.draw.circle(SCREEN,WHITE,(i,j),3)
# def create_text(txt,i,j):
#     font=pygame.font.Font('freesansbold.ttf',32)
#     txt=font.render(txt,True,WHITE,BLACK)
#     rct=txt.get_rect()
#     rct.center=(i,j)
#     SCREEN.blit(txt,rct)

if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption('CHAOS')
    Clock=pygame.time.Clock()
    while True:
        main()
