import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        document = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        self.assertListEqual(markdown_to_blocks(document), [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        document = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        self.assertListEqual(markdown_to_blocks(document), [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            )
        
    def test_markdown_block_type(self):
        block= "# heading"
        self.assertEqual(block_to_block_type(block), "heading")
        block= "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "code")
        block= "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), "quote")
        block= "* list\n* items"
        self.assertEqual(block_to_block_type(block), "unordered_list")
        block= "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), "ordered_list")
        block= "paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")
        block = "* item 1\n+ item 2\n* item 3"
        self.assertEqual(block_to_block_type(block), "paragraph")

if __name__== "__main__":
    unittest.main()
