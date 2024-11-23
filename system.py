class System:
    def __init__(self, width, height, masses):
        self.width = width
        self.height = height
        self.masses = masses
        
    def update(self):
        for mass in self.masses:
            mass.update()
        
    
        