class HTMLNode:
    def __init__(self, tag= None, value= None, children= None, props= None): #tag: str, value: str, children: list, props: dict
        self.tag= tag
        self.value= value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_to_html = ""
        for key, value in self.props.items():
            props_to_html += f'{key}="{value}" '
        return props_to_html.rstrip()
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("There's most be a tag.")
        if self.children is None:
            raise ValueError("The parent node must have children.")
        children_html= ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        if self.props is None:
            return f"LeafNode({self.tag}, {self.value})"
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

