class HTMLNode():
    def __init__(self):
        self.tag = None
        self.value = None
        self.children = None
        self.props = None

    def to_html(self):
            raise NotImplementedError
    
    def props_to_html(self):
        props_list = []
        for key, value in self.props.items():
            adjusted_txt = ' %s="%s"' % (key,value)
            props_list.append(adjusted_txt)
        props_text = ''.join(props_list)
        return props_text
    
    def __repr__(self):
         repr = "HTMLNode(%s,%s,%s,%s)" % (self.tag,self.value,self.children,self.props)
         return repr
    