import pyscreenshot

GREEN = (105, 133, 88, 255)
BLUE = (64, 150, 193, 255)
YELLOW = (122, 122, 16, 255)
RED = (207, 102, 90, 255)


class observer:

    def __init__(self, bbox, name:str, c:str="white"):

        self.x = bbox['x']
        self.y = bbox['y']
        self.x1 = self.x + bbox['width']
        self.y1 = self.y + bbox['height']
        self.width = bbox['width']
        self.height = bbox['height']
        self.color = c
        self.name = name

    def poll(self):
        i = pyscreenshot.grab(bbox=[self.x, self.y, self.x1, self.y1])
        # i.save(f"{self.name}.png")
        pixels = i.load()
        width = i.width
        height = i.height

        all_pixels = []
        for x in range(width):
            for y in range(height):
                # all_pixels.append(pixels[x, y])
                # print(pixels[x,y])
                if pixels[x,y] == GREEN:
                    return 'GREEN'
                elif pixels[x,y] == RED:
                    return 'RED'
                elif pixels[x,y] == BLUE:
                    return 'BLUE'
                elif pixels[x,y] == YELLOW:
                    return 'YELLOW'
        # return all_pixels
        return 'NONE'
