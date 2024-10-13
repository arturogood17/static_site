import unittest

from in_line_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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

    def test_regex_image(self):
        text= "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], images)

    def test_regex_links(self):
        text= "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], links)

if __name__=="__main__":
    unittest.main()