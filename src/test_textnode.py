import unittest

from textnode import (TextNode, text_type_bold, text_type_code, text_type_image, text_type_italic,
text_type_text, text_type_link, text_node_to_html_node,) 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


    def test_dif_t_type(self):
        n1 = TextNode("This is a text node", "italic")
        n2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(n1, n2)

    def test_url(self):
        n3 = TextNode("This is a text node", "italic", "www.marca.com")
        n4 = TextNode("This is a text node", "italic", "www.marca.com")
        self.assertEqual(n3, n4)

    def test_not_equal(self):
        n5 = TextNode("This is a text node", "bold", "www.marca.com")
        n6 = TextNode("This is a text node", "italic", "www.marca.com")
        self.assertNotEqual(n5, n6)

    def test_printing(self):
        n7 = TextNode("This is a text node", "bold", "www.marca.com")
        self.assertEqual("TextNode(This is a text node, bold, www.marca.com)", repr(n7))


class TestTextNodetoHtml(unittest.TestCase):
    def test_text(self):
        node1= TextNode("This is just text", text_type_text)
        html_node = text_node_to_html_node(node1)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is just text")

    def test_image(self):
        node1= TextNode("image", text_type_image, "https://www.boot.dev")
        html_node = text_node_to_html_node(node1)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "image"})

    def test_bold(self):
        node1= TextNode("bold", text_type_bold)
        html_node = text_node_to_html_node(node1)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold")

if __name__ == "__main__":
    unittest.main()