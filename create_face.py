from PIL import Image, ImageDraw
from dataclasses import dataclass
import random

class CreateFace:
    def __init__(self, width:int=400, height:int=400) -> None:
        self.width = width
        self.height = height
        self.image = None
        self.get_random_color = lambda: (random.randint(0,255),random.randint(0,255),random.randint(0,255)) # kinda like a factory function I guess
    
    
    def random_color(self) -> None:
        image = Image.new(mode="RGB", size=(self.width, self.height), color=self.get_random_color())
        self.image = image
        
    def drawing_random_circle(self, amount:int=1) -> None:
        draw = ImageDraw.Draw(self.image)
        for _ in range(amount):
            start_x,start_y = random.randint(0,self.width//2), random.randint(0,self.height//2)
            end_x, end_y = random.randint(start_x, self.width), random.randint(start_y, self.height)
            draw.ellipse([(start_x,start_y), (end_x,end_y)], fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    
    def draw_face(self) -> None:
        draw = ImageDraw.Draw(self.image)
        eye_colour = self.get_random_color()
        draw.ellipse([(.25*self.width, .2*self.height), (.4*self.width, .4*self.height)], fill=eye_colour)
        draw.ellipse([(.60*self.width, .2*self.height), (.75*self.width, .4*self.height)], fill=eye_colour)
        draw.chord([(.25*self.width, .75*self.height), (.75*self.width, .90*self.height)], 0, 180, fill=self.get_random_color())
        
    
    def roblox_meme_face(self)-> None:
        draw = ImageDraw.Draw(self.image)
        
        draw.arc([(322, 151), (363, 268)], -180, -90, fill=0, width=4)
        draw.arc([(117, 171), (305, 217)], 0, 115, fill=0, width=4)
        draw.arc([(168, 201), (208, 226)], 115, 200, fill=0, width=4)
        draw.line([(90, 67), (159, 67)], fill=0, width=1)
        draw.line([(84, 79), (144, 79)], fill=0, width=3)
        draw.line([(144, 79), (156, 83)], fill=0, width=3)
        draw.line([(138, 79), (151, 101)], fill=0, width=3)
        draw.line([(75, 105), (157, 105)], fill=0, width=3)
        draw.line([(66, 98), (75, 105)], fill=0, width=3)
        draw.line([(56, 101), (84, 79)], fill=0, width=3)
        draw.arc([(164, 72), (167, 102)], -30, 10, fill=0, width=4)
        draw.rounded_rectangle([(94, 80), (131, 102)], radius=4, fill=0, width=4)
        draw.rounded_rectangle([(115, 86), (120, 91)], radius=1, fill=(255,255,255), width=4)

    
    def show_image(self) -> None:
        self.image.show()
        
    def save_image(self) -> None:
        self.image.save("image.jpg")
        
    def throw_image(self) -> Image:
        return self.image
        
@dataclass
class Ellipses:
    image_id: int
    circle_dims: dict

if __name__ == "__main__":
    # test = CreateFace()
    
    # test.random_color()
    # test.draw_face()
    # test.show_image()
    # print("hje")
    print(image_size := Image.open("roblox_face.png").size) # walrus operator goes ooooouuuuh