class chair():
    def __init__(self,color,height,material):
        self.color=color
        self.height=height
        self.material=material
    def disp(self):
        print(f"It is a chair with color {self.color}, height {self.height} and material {self.material}")

chair1=chair("red","5cm","wood")
chair1.disp()