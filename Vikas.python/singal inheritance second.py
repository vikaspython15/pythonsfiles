class area:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
        class rectangle(area):
            def area_rectangle(self):
                rec_area = self.length * self.width
                