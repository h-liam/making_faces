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
    test = CreateFace()
    
    test.random_color()
    test.draw_face()
    test.show_image()
    print("hje")