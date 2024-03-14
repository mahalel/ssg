from textnode import TextNode
# from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    node = TextNode(text="testing", text_type="bold", url="http://googo.go")

    return text_node_to_html_node(node)


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


main()
