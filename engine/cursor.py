class Cursor () :
    def __init__ (self):
        self.x = 0
        self.y = 0
        self.visible = False
        
    def print_to_console (self, console):
        if self.visible:
            console.print(x=self.x, y=self.y, string="X", fg=[0, 255, 255], bg=[0, 0, 0])