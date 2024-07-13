import pyscreenshot

YELLOW = (122, 122, 16, 255)
GREEN = (105, 133, 88, 255)
BLUE = (64, 150, 193, 255)
RED = (207, 102, 90, 255)


class observer:

    def __init__(self, bbox, name: str, c: str = "white"):

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
        # Get four points around the corners
        quarter_width = i.width/4
        quarter_height = i.height/4

        test_points = [
            (quarter_width, quarter_height),
            (width - quarter_width, quarter_height),
            (quarter_width, height - quarter_height),
            (width - quarter_width, height - quarter_height),
        ]
        
        for point in test_points:
            if check_color_in_range(pixels[point[0], point[1]], GREEN, 20):
                return 'GREEN'
            if check_color_in_range(point, RED, 20):
                return 'RED'
            if check_color_in_range(point, BLUE, 20):
                return 'BLUE'
            if check_color_in_range(point, YELLOW, 20):
                return 'YELLOW'

        return 'NONE'
