class Solution:
    def __init__(self):
        self.last = []
        self.text = []
        
    def append(self, x):
        self.text.append(x)

    def undo(self):
        self.last.append(self.text[-1])
        self.text.pop()

    def redo(self):
        self.text.append(self.last[-1])
        self.last.pop()
    def read(self):
        return "".join(self.text)