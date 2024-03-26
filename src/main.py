from src.inline_markdown import split_nodes_image, text_to_textnodes
from textnode import TextNode, text_type_text


def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(text)
    print(new_nodes)


main()
