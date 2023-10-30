import pygame
import sys
import Button
import subprocess

pygame.init()
WIDTH_SCREEN=1220
HEIGHT_SCREEN=700
#tạo cửa sổ gâme
SCREEEN=pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))

pygame.display.set_caption("Menu")
BG=pygame.image.load(r'images/MENU_BG.jpg')
BG=pygame.transform.scale(BG,(WIDTH_SCREEN,HEIGHT_SCREEN))

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

        #Xử lí sự kiện
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                sys.exit()
            #nếu bắt được sự kiện click chuột
            if event.type==pygame.MOUSEBUTTONDOWN:
                if TUTORIAL_BACK.checkForInput(TUTORIAL_GET_POS):
                    return
        pygame.display.update()

while True:

    SCREEEN.blit(BG,(0,0))
    MENU_MOUSE_POS=pygame.mouse.get_pos() 
    
    NAME_TEXT=get_font(90).render("TANK WAR",True,"#D07A04")
    NAME_TEXT_RECT=NAME_TEXT.get_rect(center=(WIDTH_SCREEN/2,100))
    SCREEEN.blit(NAME_TEXT,NAME_TEXT_RECT)
    
    image_button=pygame.image.load(r'images/Tutorial_Rect.png')
    image_button=pygame.transform.scale(image_button,(450,80))

    LIST_OPTIONS=[]

    PLAY_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,250),text_input="PLAY",font=get_font(28),
                        base_color='#d7fcd4',hovering_color="white") 
    LIST_OPTIONS.append(PLAY_BUTTON)
    

    SOLO_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,350),text_input="SOLO vs FRIEND",font=get_font(28),
                        base_color='#d7fcd4',hovering_color="white") 
    LIST_OPTIONS.append(SOLO_BUTTON)

    TRAIN_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,450),text_input="TRAIN",font=get_font(28),
                        base_color='#d7fcd4',hovering_color="white")
    LIST_OPTIONS.append(TRAIN_BUTTON)

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
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
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
subprocess.Popen(["python", "exit_pygame.py"])
subprocess.Popen(["python", path])

