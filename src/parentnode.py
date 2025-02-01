from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    """
    
    """
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: no tag")
        if self.children == None:
            raise ValueError("Invalid HTML: no children")
        else:
            # What I think is interesting is, I get every child node using a loop, then recurse over all over all those. I thought recursion worked differently
            children_html = ''
            for child in self.children:
                    children_html += child.to_html()
            
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
            
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
