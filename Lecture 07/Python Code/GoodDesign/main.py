# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 07\Python Code\GoodDesign\main.py
from elements.text_element import TextElement
from elements.image_element import ImageElement
from elements.new_line_element import NewLineElement
from elements.tab_space_element import TabSpaceElement
from persistence.file_storage import FileStorage
from document_editor import DocumentEditor
from document import Document

def main():
    # Create a new document
    document = Document()
    
    # Create a persistence strategy
    persistence = FileStorage()
    
    # Create a document editor
    editor = DocumentEditor(document, persistence)
    
    # Simulate user interactions
    editor.add_text("Hello, world!")
    editor.add_new_line()
    editor.add_tab_space()
    editor.add_text("This is a well-structured document editor example.")
    editor.add_new_line()
    editor.add_image("image.png")
    
    # Render and display the final document
    print(editor.render_document())
    
    # Save the document
    editor.save_document()

if __name__ == "__main__":
    main()