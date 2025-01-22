from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value):
        super().__init__(value)
        self.children = None

    def to_html(self):
        if self.value == None: 
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            return self.props_to_html()
        pass 