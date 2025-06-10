class DocumentEditor:
    def __init__(self):
        self.document_elements = []
        self.rendered_document = ""

    def add_text(self, text):
        self.document_elements.append(text)

    def add_image(self, image_path):
        self.document_elements.append(f"[Image: {image_path}]")

    def render_document(self):
        if not self.rendered_document:
            self.rendered_document = "\n".join(self.document_elements)
        return self.rendered_document

    def save_to_file(self, filename="document.txt"):
        try:
            with open(filename, 'w') as file:
                file.write(self.render_document())
            print(f"Document saved to {filename}")
        except IOError:
            print("Error: Unable to open file for writing.")