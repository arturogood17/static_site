import re
from htmlnode import ParentNode
from textnode import text_node_to_html_node
from in_line_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    if not markdown:
        return []
    split = markdown.split("\n\n")
    new_blocks = []
    for block in split:
        if block:
            new_blocks.append(block.strip())
    return new_blocks

def block_to_block_type(block):
    patron_heading = r"^#{1,6} "
    lines = block.split("\n")
    if re.match(patron_heading, block):
        return block_type_heading
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"): #Tiene que ser len() > 1 porque son cierre y final
        return block_type_code
    
    if block.startswith("> "):
        for i in lines:
            if not i.startswith("> "):
                return block_type_paragraph
        return block_type_quote
    
    if block.startswith("* "):
        for i in lines:
            if not i.startswith("* ") :
                return block_type_paragraph
        return block_type_ulist
    
    if block.startswith("- "):
        for i in lines:
            if not i.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    
    if block.startswith("1. "):
        for index, value in enumerate(lines[1:]):
            if not value.startswith(f"{index + 2}. "):
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)

def block_to_html_node(block):
    type= block_to_block_type(block)
    if type == block_type_heading:
        return heading_to_html_node(block)
    if type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if type == block_type_quote:
        return quote_to_html_node(block)
    if type == block_type_code:
        return code_to_html_node(block)
    if type == block_type_ulist:
        return ulist_to_html_node(block)
    if type == block_type_olist:
        return ulist_to_html_node(block)

def text_to_children(text):
    children= []
    textnode= text_to_textnodes(text) #Lista
    for i in textnode:
        children.append(text_node_to_html_node(i))
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    lines= block.split()
    level= 0
    for i in lines[0]:
        if i == "#":
            level +=1
        else:
            break
    if level + 1 >= level(block):
        raise ValueError(f"Invalid heading level= {level}")
    text= block[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines=[]
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content= " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("quoteblock", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text= block[4:-3]
    children= text_to_children(text)
    code= ParentNode("code", children)
    return ParentNode("pre", [code])

def ulist_to_html_node(block):
    list= block.split("\n")
    html_items= []
    for i in list:
        text= i[2:]
        children= text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html_node(block):
    list= block.split("\n")
    html_items= []
    for i in list:
        text= i[3:]
        children= text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)