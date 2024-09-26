from htmlnode import LeafNode, ParentNode
from text_utils import text_to_textnodes, text_node_to_html_node

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
    children = []

    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case type if type == block_type_code:
                children.append(code_to_html_node(block))
            case type if type == block_type_heading:
                blocks = block.split('/n')
                for b in blocks:
                    children.append(heading_to_html_node(b))
            case type if type == block_type_quote:
                children.append(quote_to_html_node(block))
            case type if type == block_type_paragraph:
                children.append(paragraph_to_html_node(block))
            case type if type == block_type_ordered_list:
                children.append(ol_to_html_node(block))
            case type if type == block_type_unordered_list:
                children.append(ul_to_html_node(block))
    
    return ParentNode('div', children)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    nodes = text_to_textnodes(paragraph)

    paragraph_children = []
    for n in nodes:
        paragraph_children.append(text_node_to_html_node(n))

    final_paragraph = ParentNode('p', paragraph_children)
    return final_paragraph

def code_to_html_node(block):
    children = []
    nodes = text_to_textnodes(block)

    for n in nodes:
        children.append(text_node_to_html_node(n))

    second_parent = ParentNode('pre', children)
    return second_parent

def heading_to_html_node(block):
    children = []
    count = 0
    for l in block:
        if l == "#":
            count += 1
        else:
            break
    text_nodes = text_to_textnodes(block[count + 1:])
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    
    return ParentNode(f"h{count}", children)

def quote_to_html_node(block):
    children = []
    lines = block.split('\n')

    for i in range(len(lines)):
        lines[i] = lines[i][1:]
    
    text_nodes = text_to_textnodes(''.join(lines).strip())

    for node in text_nodes:
        children.append(text_node_to_html_node(node))

    return ParentNode('blockquote', children)

def ul_to_html_node(block):
    children = []
    lines = block.split('\n')

    for i in range(len(lines)):
        lines[i] = lines[i][2:]

    nodes = []
    for l in lines:
        text_nodes = text_to_textnodes(l)
        html_nodes = list(map(lambda x: text_node_to_html_node(x), text_nodes))
        nodes.append(html_nodes)

    for n in nodes:
        children.append(ParentNode('li', n))
    
    return ParentNode('ul', children)

def ol_to_html_node(block):
    children = []
    lines = block.split('\n')

    for i in range(len(lines)):
        lines[i] = lines[i][3:]

    nodes = []
    for l in lines:
        text_nodes = text_to_textnodes(l)
        html_nodes = list(map(lambda x: text_node_to_html_node(x), text_nodes))
        nodes.append(html_nodes)

    for n in nodes:
        children.append(ParentNode('li', n))
    
    return ParentNode('ol', children)
