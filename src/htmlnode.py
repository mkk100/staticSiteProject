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
        for key in self.props:
            res += f' {key}="{self.props[key]}"'
        return res
    
    def __repr__(self):
        return(f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}")
    
    
    
    
        