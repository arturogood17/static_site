from htmlnode import LeafNode
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"
class TextNode:

    def __init__(self, text, text_type, url= None): #url es dict
        self.text= text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textnode2) -> bool:
        if self.text == textnode2.text and self.text_type == textnode2.text_type and self.url == textnode2.url:
            return True
    
    def __repr__(self) -> str:
        if self.url:
            return f"TextNode({self.text}, {self.text_type}, {self.url})"
        else:
            return f"TextNode({self.text}, {self.text_type})"
        
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text_type.")