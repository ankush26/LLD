class ImageElement(DocumentElement):
    def __init__(self, image_path):
        self.image_path = image_path

    def render(self):
        return f"[Image: {self.image_path}]"