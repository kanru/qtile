from .. import bar
import base

class TextBox(base._TextBox):
    def __init__(self, name, text=" ", width=bar.STRETCH):
        """
            :name Name for this widget.
            :text Initial widget text.
            :width Either an integer width, or the STRETCH constant.
        """
        self.name = name
        base._TextBox.__init__(self, text, width)

    def update(self, text):
        self.text = text
        self.draw()

    def cmd_update(self, text):
        """
            Update the text in a TextBox widget.
        """
        self.update(text)

    def cmd_get(self):
        """
            Retrieve the text in a TextBox widget.
        """
        return self.text

