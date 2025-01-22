from enum import Enum

class TextType(Enum):
    NORMAL = "air"
    BOLD = "water"
    ITALIC = "earth"
    CODE = "fire"
    LINKS = ""
    IMAGES = ""

class TextNode():
    def __init__(self,text,text_type):
        self.text = text
        self.text_type = text_type
        self.url = None

    def __eq__(self, other_text_node):
        if vars(self).items() == vars(other_text_node).items():
            return True
        else:
            return False
    def __repr__(self):
        repr = "TextNode(%s,%s,%s)" % (self.text,self.text_type.value,self.url)
        return repr
    
if __name__ == "__main__":
    print('we jopping')
    a = TextNode('a',TextType.BOLD)
    print(a.__repr__())