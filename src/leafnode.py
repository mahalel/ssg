from typing import Dict, Any
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str = None, props: Dict[str, Any] = None) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if len(self.value) == 0:
            raise ValueError('All leaf nodes require a value')
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
