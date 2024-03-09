from textnode import TextNode
from htmlnode import HTMLNode


def main():
    txt = TextNode('one', 'bold', 'some_url')
    print(repr(txt))
    html = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(repr(html))


main()
