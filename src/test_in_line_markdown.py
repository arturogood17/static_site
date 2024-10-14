import unittest

from in_line_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link

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


    def test_node_image(self):
        node= TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )


    def test_just_image(self):
        node= TextNode("![image](https://www.example.COM/IMAGE.PNG)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_double_image(self):
        node= TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes= split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ), ], new_nodes,)
        
    def test_node_link(self):
        node = TextNode("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
                        text_type_text)
        new_nodes= split_nodes_link([node])
        self.assertListEqual([
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,)


if __name__=="__main__":
    unittest.main()