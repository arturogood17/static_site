def extract_title(markdown):
    content= markdown.strip().split("\n")
    first_heading = content[0]
    if not first_heading.startswith("# "):
        raise Exception("Title not found.")
    return first_heading.strip("# ")