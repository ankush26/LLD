class DocumentElement:
    def render(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Document:
    def __init__(self):
        self.document_elements = []

    def add_element(self, element):
        self.document_elements.append(element)

    def render(self):
        return ''.join(element.render() for element in self.document_elements)

class Persistence:
    def save(self, data):
        raise NotImplementedError("Subclasses must implement this method.")

class FileStorage(Persistence):
    def save(self, data):
        with open("document.txt", "w") as file:
            file.write(data)
            print("Document saved to document.txt")

class DocumentEditor:
    def __init__(self, document, storage):
        self.document = document
        self.storage = storage

    def add_text(self, text):
        self.document.add_element(TextElement(text))

    def add_image(self, image_path):
        self.document.add_element(ImageElement(image_path))

    def add_new_line(self):
        self.document.add_element(NewLineElement())

    def add_tab_space(self):
        self.document.add_element(TabSpaceElement())

    def render_document(self):
        return self.document.render()

    def save_document(self):
        self.storage.save(self.render_document())