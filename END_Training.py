import pygame
import sys
import Button
import subprocess
import os
pygame.init()
WIDTH_SCREEN=1150
HEIGHT_SCREEN=700

#vẽ cửa sổ game
SCREEEN=pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))

#hàm set thuộc tính cho font chữ với đối số là size chữ
def get_font(size):
    return pygame.font.Font(r'images/font.ttf',size) #trả về kiểu font chữ and size

pygame.display.set_caption("END")


#tạo nền cho màn hình
END_BG_Screen=pygame.image.load(r'images/grass.png')
END_BG_Screen=pygame.transform.scale(END_BG_Screen,(WIDTH_SCREEN,HEIGHT_SCREEN))
path = ''


while True:

    #lấy vị trí của chuột
    END_GET_POS=pygame.mouse.get_pos()

    #vẽ background
    SCREEEN.blit(END_BG_Screen,(0,0))
   
    #đối tượng ảnh button
    image_button=pygame.image.load(r'images/Tutorial_Rect.png')
    image_button=pygame.transform.scale(image_button,(400,100))
    
    #nút về menu
    BackMenu=Button.Button(image_button,pos=(WIDTH_SCREEN/2,380),text_input="MENU",font=get_font(50),
                                base_color="#d7fcd4",hovering_color="yellow")
    
    #check xem chuột có tác động đến nút ?
    BackMenu.changeColor(END_GET_POS)
    #vẽ nút
    BackMenu.update(SCREEEN)

    #vẽ chữ END lên màn hình
    END_TEXT=get_font(100).render("END",True,"#d7fcd4")
    END_TEXT_RECT=END_TEXT.get_rect(center=(WIDTH_SCREEN/2,150))
    SCREEEN.blit(END_TEXT,END_TEXT_RECT)

    #sử lí sự kiện
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if BackMenu.checkForInput(END_GET_POS):
                path = 'Main.py'
                break
    if path != '':
        break
                
    pygame.display.update()
subprocess.Popen(["python", "exit_pygame.py"])
subprocess.Popen(["python", path])