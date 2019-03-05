from django.db import models
from DANTSOVA import Stego


class AcroText(models.Model):
    text = str()
    count = int()
    acrotext = models.CharField(max_length=1000)
    top_last_words = list()

    def set_text(self, text):
        self.text = text
        self.count = 0

    def do_word(self, previous_word):
        while self.text[self.count] == " ":
            self.count += 1
        words = Stego.main(previous_word, self.text[self.count])
        if words == "":
            message = "Выберите другое слово"
            return message
        self.count += 1
        self.top_last_words = words
        self.acrotext = self.acrotext + " " + previous_word


    def get_top_words(self):
        return self.top_last_words

    def get_acrotext(self):
        return self.acrotext
