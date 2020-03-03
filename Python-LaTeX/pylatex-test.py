from pylatex import  Document, Section, Subsection, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic, NoEscape
import numpy as np

class MyDocument(Document):
    def create_exercise(self):
        with self.create(Section('Oefening')):
            self.append('Bereken:')        

    def __init__(self):
        super().__init__()

        #self.preamble.append(Command('title', 'Awesome Title'))
        #self.preamble.append(Command('author', 'Anonymous author'))
        #self.preamble.append(Command('date', NoEscape(r'\today')))
        #self.append(NoEscape(r'\maketitle'))

    def fill_document(self):
        """Add a section, a subsection and some text to the document."""
        with self.create(Section('A section')):            
            a = 3
            tmp = Math(data=['a = ', a], inline=True)
            self.append(tmp)
        #create_exercise(self)
        with self.create(Section('Oefening',label=False)):
            self.append('Bereken:')            
            cdot = UnsafeCommand('cdot')
            numbers = np.random.randint(low=1, high=20, size=4)
            a = numbers[0]
            question = Math(data=[numbers[0], ' - ', numbers[1], cdot, numbers[2], ' + ', numbers[3]], inline=True)
            self.append(question)


if __name__ == '__main__':

    # Document
    doc = MyDocument()

    # Call function to add text
    doc.fill_document()

    doc.generate_pdf('test-exercises', clean_tex=False)
    tex = doc.dumps()  # The document as string in LaTeX syntax
