from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text

class Page:
    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise Elem.ValidationError("Provided element is not an instance of Elem.")
        self.elem = elem

    def __str__(self):
        return "<!DOCTYPE html>\n" + str(self.elem) if isinstance(self.elem, Html) else str(self.elem)

    def write_to_file(self, path):
        with open(path, "w") as f:
            f.write(str(self))

    def is_valid(self):
        return self.__recursive_check(self.elem)

    def __recursive_check(self, elem):
        valid_elements = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)
        if not isinstance(elem, valid_elements):
            return False
        if isinstance(elem, (Meta, Text)):
            return True
        if isinstance(elem, Html) and len(elem.content) == 2 and isinstance(elem.content[0], Head) and isinstance(elem.content[1], Body):
            return all(self.__recursive_check(child) for child in elem.content)
        if isinstance(elem, Head) and sum(isinstance(child, Title) for child in elem.content) == 1:
            return all(self.__recursive_check(child) for child in elem.content)
        if isinstance(elem, (Body, Div)) and all(isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for child in elem.content):
            return all(self.__recursive_check(child) for child in elem.content)
        if isinstance(elem, (Title, H1, H2, Li, Th, Td)) and len(elem.content) == 1 and isinstance(elem.content[0], Text):
            return True
        if isinstance(elem, P) and all(isinstance(child, Text) for child in elem.content):
            return True
        if isinstance(elem, Span) and all(isinstance(child, (Text, P)) for child in elem.content):
            return all(self.__recursive_check(child) for child in elem.content)
        if isinstance(elem, (Ul, Ol)) and len(elem.content) > 0 and all(isinstance(child, Li) for child in elem.content):
            return all(self.__recursive_check(child) for child in elem.content)
        if isinstance(elem, Tr) and all(isinstance(child, (Th, Td)) for child in elem.content) and all(type(child) == type(elem.content[0]) for child in elem.content):
            return True
        if isinstance(elem, Table) and all(isinstance(child, Tr) for child in elem.content):
            return True
        return False

if __name__ == "__main__":
    __test()
