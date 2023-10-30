import pygame
class Button():
    def __init__(self,image,pos,text_input,font,base_color,hovering_color):
        self.image=image 
        self.font=font 
        self.x_pos,self.y_pos=pos[0],pos[1] 
        self.base_color,self.hovering_color=base_color,hovering_color 
        self.text_input=text_input 
        self.text=self.font.render(self.text_input,True,self.base_color) 
        if self.image is None: 
            self.image=self.text
        self.img_rect=self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.text_rect=self.text.get_rect(center=(self.x_pos,self.y_pos))
    
    #hiển thị button
    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image,self.img_rect)
        screen.blit(self.text,self.text_rect)
    
    #check click vào khu vực nút , đối số là vị trí tọa độ của chuột
    def checkForInput(self,position):
        if position[0] in range (self.img_rect.left,self.img_rect.right) and position[1] in range (self.img_rect.top,self.img_rect.bottom):
            return True
        return False
    
    #check click vào khu vực nút and Hover,đối số là vị trí tọa độ của chuột
    def changeColor(self,position):
        if position[0] in range (self.img_rect.left,self.img_rect.right) and position[1] in range (self.img_rect.top,self.img_rect.bottom):
            self.text=self.font.render(self.text_input,True,self.hovering_color)
        else:
            self.text=self.font.render(self.text_input,True,self.base_color)

