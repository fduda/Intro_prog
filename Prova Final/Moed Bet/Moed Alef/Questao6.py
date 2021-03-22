class Photo:

    def __init__(self,name, size, color, description = ""):
        name = self.name
        size = self.size
        color = self.color
        description = self.description

    def get_area(self):
        return self.size[0] * self.size[1]

    def get_name(self):
        return self.name

    def set_description(self, string):
