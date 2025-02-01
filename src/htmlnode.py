class HTMLNode():
    """
    Represent HTML nodes in an HTML document tree
    
    Members:
        tag (str): HTML tag name
        value (str): value of HTML tag (ie: text in a paragraph) 
        children (list): HTMLNode objects representing children of this node
        props (dict): key-value pairs representing attributes of HTML tag
    """
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
            raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        """
        Return a string that represents HTML attributes of a node
        """
        props_list = []
        props_text = ''
        
        if self.props == None:
             return props_text
        for key, value in self.props.items():
            adjusted_txt = f' {key}="{value}"'
            props_list.append(adjusted_txt)
        props_text = ''.join(props_list)
        return props_text
    
    def __repr__(self):
         repr = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
         return repr
    