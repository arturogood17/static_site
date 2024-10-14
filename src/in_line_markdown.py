from textnode import TextNode, text_type_text, text_type_link, text_type_bold, text_type_image, text_type_italic, text_type_code
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    if delimiter is None:
       raise ValueError("Please input a delimeter.") 
    for node in old_nodes:
        if (delimiter in node.text) and (node.text_type == text_type_text):
            split = node.text.split(delimiter)
            if len(split) % 2 != 1:
                raise Exception("Delimeter not closed.")
            for index, val in enumerate(split):
                if val == "":
                    continue
                if index % 2 == 0:
                    new_nodes.append(TextNode(val, text_type_text))
                else:
                    new_nodes.append(TextNode(val, text_type))
        else:
            new_nodes.append(node)
    return new_nodes


def extract_markdown_images(text):
    images= re.findall(r"!\[([^\]]*?)\]\(([^\(\)]*)\)", text)
    return images
    

def extract_markdown_links(text):
    links= re.findall(r"\[([^\]]*?)\]\(([^\(\)]*)\)", text)
    return links

def split_nodes_image(old_nodes):
    new_nodes= []
    for node in old_nodes:
        while node.text:
            images = extract_markdown_images(node.text)
            if images:
                alt_image, link = images[0]
                split_node = node.text.split(f"![{alt_image}]({link})", 1)
                if len(split_node) != 2:
                    raise Exception("Invalid markdown, image section not closed.")
                if split_node[0]:
                    new_nodes.append(TextNode(split_node[0], text_type_text))
                new_nodes.append(TextNode(alt_image, text_type_image, link))
                node.text= split_node[1]
            else:
                new_nodes.append(node)
                break
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes= []
    for node in old_nodes:
        while node.text:
            links = extract_markdown_links(node.text)
            if links:
                alt_link, url = links[0]
                split_node = node.text.split(f"[{alt_link}]({url})", 1)
                if len(split_node) != 2:
                    raise Exception("Invalid markdown, link section not closed.")
                if split_node[0]:
                    new_nodes.append(TextNode(split_node[0], text_type_text))
                new_nodes.append(TextNode(alt_link, text_type_link, url))
                node.text= split_node[1]
            else:
                new_nodes.append(node)
                break
    return new_nodes