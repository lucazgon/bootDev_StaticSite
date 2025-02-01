from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    """
    Represents a single HTML tag w/ no children. (ie: paragraph tags)
    """
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        """
        renders a leaf node as HTML string
        """
        if self.value == None: 
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"