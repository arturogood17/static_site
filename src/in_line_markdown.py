from textnode import TextNode, text_type_text, text_type_link, text_type_bold, text_type_image, text_type_italic, text_type_code


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
    