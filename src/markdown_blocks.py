def markdown_to_blocks(markdown):
    if not markdown:
        return []
    split = (markdown.split("\n"))
    new_blocks = []
    for block in split:
        if block:
          new_blocks.append(block.strip(" "))
        else:
            continue
    return new_blocks

text= """

# Título

   Este es un párrafo con espacios
al inicio y al final.   

* Primer item
* Segundo item


Otro párrafo después de una línea en blanco.

"""

blocks = markdown_to_blocks(text)


print(blocks)