from typing import Dict, List, Any
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, children: List['HTMLNode'], tag: str = None, props: Dict[str, Any] = None) -> None:
        super().__init__(children=children, tag=tag, props=props)

    def to_html(self) -> str:  # TODO
        if len(self.tag) == 0:
            raise ValueError('All parent nodes require a tag')
        if len(self.children) == 0:
            raise ValueError(' This parent is not a parent')

        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def props_to_html(self) -> str:
        props_list = []
        if self.props is not None:
            for i in self.props:
                props_list.append(f' {i}="{self.props[i]}"')
            return "".join(props_list)
        return ""

    def __repr__(self) -> str:
        return f'LeafNode({self.value}, {self.tag}, {self.props})'
