from enum import Enum

class TextType(Enum):
    NORMAL = "air"
    BOLD = "water"
    ITALIC = "earth"
    CODE = "fire"
    LINKS = ""
    IMAGES = ""

class TextNode():
    '''
    Parses inline markdown text and outputs HTML
    
    Members:
        text (str): content
        text_type (TextType): normal, bold, italic etc
        url (str): web page location
    '''
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_text_node):
        if vars(self).items() == vars(other_text_node).items():
            return True
        else:
            return False
    def __repr__(self):
        repr = f"TextNode({self.text}, {self.text_type.value}, {self.url})"
        return repr