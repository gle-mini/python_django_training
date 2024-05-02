class Text(str):
    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;').replace('>','&gt;').replace('"', '"').replace('\n', '\n<br />\n')


class Elem:
    class ValidationError(Exception):
        def __init__(self):
            super().__init__("Type error the content isn't made of Text or Elem.")

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        if attr is None:
            attr = {}
        self.tag = tag
        self.attr = attr
        self.content = []
        self.tag_type = tag_type
        if content is not None:
            self.add_content(content)

    def __str__(self):
        attributes = self.__make_attr()
        if self.tag_type == 'double':
            return f'<{self.tag}{attributes}>{self.__make_content()}</{self.tag}>'
        elif self.tag_type == 'simple':
            return f'<{self.tag}{attributes} />' 

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ""
        result = "\n"
        for elem in self.content:
            if (len(str(elem)) != 0):
                result += "{elem}\n".format(elem=elem)
        result = "  ".join(line for line in result.splitlines(True))
        if len(result.strip()) == 0:
            return ''
        return result

    def add_content(self, content):
        if isinstance(content, str):
            content = Text(content)
        if not self.check_type(content):
            raise Elem.ValidationError
        if isinstance(content, list):
            self.content.extend([c if isinstance(c, Elem) or isinstance(c, Text) else Text(c) for c in content])
        else:
            self.content.append(content)

    @staticmethod
    def check_type(content): 
        return isinstance(content, (Elem, Text)) or \
            (isinstance(content, list) and all(isinstance(elem, (Elem, Text)) for elem in content))


def test():
    html = Elem('html', content=[
                Elem('head', content=Elem(
                    'title', content=Text('"Hello ground!"'))),
                Elem('body', content=[Elem('h1', content=Text('"Oh no, not again!"')),
                                      Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')])])
    print(html)

if __name__ == '__main__':
    test()
