from htmlnode import LeafNode, ParentNode

# Constants
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

# Functions
def markdown_to_blocks(markdown):
    split_blocks = markdown.split('\n\n')
    formatted_blocks = []
    for block in split_blocks:
        if block.strip() == "":
            continue
        else:
            formatted_blocks.append(block.strip())
    return formatted_blocks

def block_to_block_type(block: str):
    #Check fo code block
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    
    #Check for heading block
    if block.startswith("#"):
        if len(block.split('#######')) == 1:
            return block_type_heading
        
    #Check for quote block
    if block.startswith(">"):
        is_quote = True
        lines = block.split('\n')
        for l in lines:
            if not l.startswith('>'):
                is_quote = False
        if is_quote:
            return block_type_quote
    
    #Check for unordered list:
    if block.startswith("*") or block.startswith("-") :
        is_ul = True
        lines = block.split('\n')
        for l in lines:
            if not l.startswith('* ') and not l.startswith('- '):
                is_ul = False
        if is_ul:
            return block_type_unordered_list
    
    #Check for ordered list:
    nums = ['1','2','3','4','5','6','7','8','9']
    if block[0] in nums:
        is_ol = True
        lines = block.split('\n')
        for l in lines:
            if not l[0] in nums or not l[1:3] == '. ':
                is_ol = False
        if is_ol:
            return block_type_ordered_list

    return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    for b in blocks:
        print(block_to_block_type(b))
        print('\n')


md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

1. list item 1
2. list item 2
3. list item 3
"""

markdown_to_html_node(md)