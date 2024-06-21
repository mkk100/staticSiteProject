class HTMLNode:
    def __init__(self, tag='', value='', children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        res = ''
        if self.props == None:
            return ''
        for key in self.props:
            res += f' {key}="{self.props[key]}"'
        return res
    
    def __repr__(self):
        return(f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}")
    
class LeafNode(HTMLNode):
    def __init__(self, tag='', value='', props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag='', children=[], props={}):
        super().__init__(tag,None, children, props)
    
    def to_html(self):
        if self.tag is None or self.children is None:
            raise ValueError
        res = ''
        for child in self.children:
            res += f"{child.to_html()}"
        return f"<{self.tag}>{res}</{self.tag}>"
        

    
    
    
        