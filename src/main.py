import re
from typing import List, Tuple
from textnode import TextNode
# from htmlnode import HTMLNode
from leafnode import LeafNode
# from parentnode import ParentNode


def main():
    # node = TextNode(text="testing", text_type="bold", url="http://googo.go")
    # node = TextNode(text="This is text with a `code` block word", text_type="text")
    # new_nodes = split_nodes_delimiter([node], "`", txt_type="code")
    # print(new_nodes)
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    print(extract_markdown_images(text))
# [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text))
# [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
    
    # return text_node_to_html_node(node)


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type not in ["text", "bold", "italic", "code", "link", "image"]:
        raise Exception("Not a valid text type.")
    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(tag='b', value=text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode(tag='i', value=text_node.text)
    elif text_node.text_type == "code":
        return LeafNode(tag='code', value=text_node.text)
    elif text_node.text_type == "link":
        return LeafNode(tag='a', value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode(tag='img', value="", props={"src": text_node.url, "alt": text_node.text})


def split_nodes_delimiter(old_nodes, delimiter, txt_type):
    new_nodes = []
    for node in old_nodes:
        if type(node).__name__ != "TextNode":
            new_nodes.extend(node)
        else:
            orig_type = node.text_type
            arr = node.text.split(delimiter)
            new_node = []
            if len(arr) % 2 == 0:
                raise Exception("Not valid markdown")
            for i, elem in enumerate(arr):
                if i % 2 == 0:
                    new_node.append(TextNode(text=elem, text_type=orig_type))
                else:
                    new_node.append(TextNode(text=elem, text_type=txt_type))
            new_nodes.extend(new_node)
    return new_nodes


def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches    

def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches    
main()
