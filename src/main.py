from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    # txt = TextNode('one', 'bold', 'some_url')
    # print(repr(txt))
    html = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    # print(repr(html))
    leaf2 = LeafNode(value="Click me!", tag="a", props={"href": "https://www.google.com"})
    # print(leaf2.props)
    print(leaf2.props_to_html())
    # print(leaf1.to_html())
    # print(leaf2.to_html())


main()
