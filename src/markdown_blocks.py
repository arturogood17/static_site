import re
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
        return "heading"
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"): #Tiene que ser len() > 1 porque son cierre y final
        return "code"
    if block.startswith("> "):
        for i in lines:
            if not i.startswith("> "):
                return "paragraph"
        return "quote"
    
    if block.startswith("* "):
        for i in lines:
            if not i.startswith("* ") :
                return "paragraph"
        return "unordered_list"
    
    if block.startswith("- "):
        for i in lines:
            if not i.startswith("- "):
                return "paragraph"
        return "unordered_list"
    
    if block.startswith("1. "):
        for index, value in enumerate(lines[1:]):
            if not value.startswith(f"{index + 2}. "):
                return "paragraph"
        return "ordered_list"
    return "paragraph"