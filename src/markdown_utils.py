def markdown_to_blocks(markdown):
    split_blocks = markdown.split('\n\n')
    formatted_blocks = []
    for block in split_blocks:
        if block.strip() == "":
            continue
        else:
            formatted_blocks.append(block.strip())
    return formatted_blocks