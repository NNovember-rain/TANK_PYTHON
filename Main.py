import pygame
import sys
import Button
import subprocess
import os

pygame.init()
WIDTH_SCREEN=1220
HEIGHT_SCREEN=700
#tạo cửa sổ gâme
SCREEEN=pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))

path = ''

#hàm set thuộc tính cho font chữ với đối số là size chữ
def get_font(size):
    return pygame.font.Font(r'images/font.ttf',size) #trả về kiểu font chữ and size

def tutorial(): #tutorial screen
    # final = False
    Tutorial_Screen=pygame.image.load(r'images/game_ttral.jpg')
    Tutorial_Screen=pygame.transform.scale(Tutorial_Screen,(WIDTH_SCREEN,HEIGHT_SCREEN))
    pygame.display.set_caption("Tutorial")
    while True:
        TUTORIAL_GET_POS=pygame.mouse.get_pos()

        #vẽ nền 
        SCREEEN.blit(Tutorial_Screen,(0,0))

        #Tạo nút trở về menu
        
        #tạo đối tượng nền ảnh của button
        image_buttonback=pygame.image.load(r'images/Tutorial_Rect.png')
        image_buttonback=pygame.transform.scale(image_buttonback,(90,50))

        TUTORIAL_BACK=Button.Button(image_buttonback,pos=(70,680),text_input="BACK",font=get_font(15),
                                    base_color="#d7fcd4",hovering_color="yellow")
        TUTORIAL_BACK.changeColor(TUTORIAL_GET_POS)
        TUTORIAL_BACK.update(SCREEEN)

        #sử lí sự kiện
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                sys.exit()
            #nếu bắt được sự kiện click chuột
            if event.type==pygame.MOUSEBUTTONDOWN:
                if TUTORIAL_BACK.checkForInput(TUTORIAL_GET_POS):
                    return
        pygame.display.update()

def main_menu(): #menu screen
    pygame.display.set_caption("Menu")
    BG=pygame.image.load(r'images/MENU_BG.jpg')
    BG=pygame.transform.scale(BG,(WIDTH_SCREEN,HEIGHT_SCREEN))
    while True:

        SCREEEN.blit(BG,(0,0))
        
        #lấy vị trí của chuột,để kiểm tra xem có nhấn vào hoặc di chuyển qua nó
        MENU_MOUSE_POS=pygame.mouse.get_pos() 
       
        #tạo đối tượng văn bản main menu và vẽ lên màn hình
        NAME_TEXT=get_font(90).render("TANK WAR",True,"#D07A04")
        NAME_TEXT_RECT=NAME_TEXT.get_rect(center=(WIDTH_SCREEN/2,100))
        SCREEEN.blit(NAME_TEXT,NAME_TEXT_RECT)
        
        #tạo danh sách chứa các đối tượng nút
        LIST_OPTIONS=[]

        #tạo ra n nút bằng cách tạo ra n đối tượng nút
        image_button=pygame.image.load(r'images/Tutorial_Rect.png')
        image_button=pygame.transform.scale(image_button,(450,80))
        #Nut Play
        PLAY_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,250),text_input="PLAY",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white") #(ảnh botton,vị trí,text trên buton,đối tượng font chữ và size, màu chưa di chuột vào,màu hover chuột)
        LIST_OPTIONS.append(PLAY_BUTTON)
        
        #nút SOLO vd Friend
        SOLO_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,350),text_input="SOLO vs FRIEND",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white") #(ảnh botton,vị trí,text trên buton,đối tượng font chữ và size, màu chưa di chuột vào,màu hover chuột)
        LIST_OPTIONS.append(SOLO_BUTTON)

        #nút luyện tập
        TRAIN_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,450),text_input="TRAIN",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white")
        LIST_OPTIONS.append(TRAIN_BUTTON)

        #nút hướng dẫn
        TUTORIAL_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,550),text_input="TUTORIAL",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white")
        LIST_OPTIONS.append(TUTORIAL_BUTTON)

        #nút thoát game
        QUIT_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,650),text_input="QUIT GAME",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white")
        LIST_OPTIONS.append(QUIT_BUTTON)
        #vẽ văn bản Main Menu

        # vẽ các nút chế độ trên màn hình menu
        for button in LIST_OPTIONS: 
            button.changeColor(MENU_MOUSE_POS) #truyền vị trí chuột để thay đổi màu
            button.update(SCREEEN)
        
        for event in pygame.event.get():
            global path
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # kiểm tra nó là sự kiện click thì xem nó có click chúng nút nào không
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    with open('level.txt', 'w') as file:
                        file.write('1')
                    path = r'PvE_2.py'
                    break
                if SOLO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    path = r'PvP.py'
                    break
                if TRAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    path = r'PvE_1.py'
                    break
                if TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    tutorial()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        if path != '':
            break

main_menu()  
subprocess.Popen(["python", "exit_pygame.py"])
subprocess.Popen(["python", path])