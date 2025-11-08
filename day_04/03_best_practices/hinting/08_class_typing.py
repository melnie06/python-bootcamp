class Paper:
    def __init__(self):
        self.content = ""


class Pen:
    def __init__(self, ink_level: int):
        self.ink_level = ink_level

    def write(self, paper: Paper, text: str):
        if self.ink_level > 0:
            paper.content += text


pen = Pen(100)
paper_piece = Paper()
pen.write(paper_piece, "Example")
print(paper_piece.content)
