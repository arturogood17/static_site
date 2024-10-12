import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_text_to_htmlnode(self):
        node1= HTMLNode("p", "the text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"},)
        self.assertEqual(node1.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_printing_node(self):
        node1= HTMLNode("div", "hello world", None, {"href": "https://www.google.com", "target": "_blank"},)
        self.assertEqual(repr(node1), "HTMLNode(div, hello world, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_values(self):
        node1 = HTMLNode("a", "Don't stop me now!", None, None,)
        self.assertEqual(node1.tag, "a")
        self.assertEqual(node1.value, "Don't stop me now!")
        self.assertEqual(node1.children, None)
        self.assertEqual(node1.props, None)

    def test_leafnode_printing(self):
        node1= LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1.__repr__(), "LeafNode(p, This is a paragraph of text.)")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.__repr__(), "LeafNode(a, Click me!, {'href': 'https://www.google.com'})")

    def test_render_leafnode(self):
        node1= LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_without_tag(self):
        node1= LeafNode(None, "¡Hola, cara de bola!")
        self.assertEqual(node1.to_html(), "¡Hola, cara de bola!")

    def test_parentnode_printing(self):
        node1 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node1.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def to_html_with_children(self):
        child_node= LeafNode("span", "child")
        parent= ParentNode("div", [child_node])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def to_html_with_grandchildren(self):
        grandchild_node= LeafNode("b", "grandchild")
        child_node= ParentNode("span", [grandchild_node])
        parent= ParentNode("div", [child_node])
        self.assertEqual(parent.to_html(), "<div><span><b>grandchild</b></span></div>",)
        

if __name__ == "__main__":
    unittest.main()