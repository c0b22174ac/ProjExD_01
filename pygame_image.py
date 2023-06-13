import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    #鳥の画像読み込み
    bard_img = pg.image.load("ex01-20230613/fig/3.png")
    bg_img0 = pg.transform.flip(bg_img,True,False)
    bg_img1 = pg.transform.flip(bg_img,False,False)
    bg_img = [bg_img0,bg_img1]
    bard_img = pg.transform.flip(bard_img,True,False)
    bard_imgs = [bard_img,pg.transform.rotate(bard_img,6),pg.transform.rotate(bard_img,10),pg.transform.rotate(bard_img,4)]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img[0], [-tmr, 0])
        screen.blit(bg_img[1],[1600-tmr,0])
        screen.blit(bg_img[0],[3200-tmr,0])
        screen.blit(bard_imgs[tmr%200//50],[300,200])
        pg.display.update()
        tmr += 1      
        clock.tick(200)
        if(tmr>3199):
            tmr=0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()