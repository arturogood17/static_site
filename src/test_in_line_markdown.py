import unittest

from in_line_markdown import split_nodes_delimiter

from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code

class TestInLineMarkdown(unittest.TestCase):
    def test_boldedwords(self):
        node = TextNode("This is a **bolded word** inside text", text_type_text)
        new_nodes= split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual([
            TextNode("This is a ", text_type_text),
            TextNode("bolded word", text_type_bold),
            TextNode(" inside text", text_type_text),
        ], new_nodes)

    def test_double_bold(self):
        node = TextNode("This is a **bolded word** inside **text**", text_type_text)
        new_nodes= split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual([
            TextNode("This is a ", text_type_text),
            TextNode("bolded word", text_type_bold),
            TextNode(" inside ", text_type_text),
            TextNode("text", text_type_bold),
        ], new_nodes)
    
    def test_italics(self):
        node = TextNode("This is a *italic text* inside a paragraph", text_type_text)
        new_nodes= split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual([
            TextNode("This is a ", text_type_text),
            TextNode("italic text", text_type_italic),
            TextNode(" inside a paragraph", text_type_text),
        ], new_nodes)

    def test_coded(self):
        node = TextNode("This is a `coded part` inside a paragraph", text_type_text)
        new_nodes= split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual([
            TextNode("This is a ", text_type_text),
            TextNode("coded part", text_type_code),
            TextNode(" inside a paragraph", text_type_text),
        ], new_nodes)

    def test_doubled_troubled(self):
        node = TextNode("This is a *coded part* inside a **paragraph**", text_type_text)
        new_nodes= split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual([
            TextNode("This is a ", text_type_text),
            TextNode("coded part", text_type_italic),
            TextNode(" inside a ", text_type_text),
            TextNode("paragraph", text_type_bold),
        ], new_nodes)

if __name__=="__main__":
    unittest.main()