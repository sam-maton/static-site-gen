class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f'HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}'

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ""
        if self.props:
            for k,v in self.props.items():
                props_string += f' {k}="{v}"'
        return props_string
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError('A value must be given to a leaf node')
        
        if self.tag == None:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError('A valid HTML tag must be given')
        
        if self.children == None:
            raise ValueError('Parent nodes must containt some valid children')
        
        