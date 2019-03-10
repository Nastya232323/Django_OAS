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
        if self.count == len(self.text):
            message = "Вы сгенерировали Ваш акротекст"
            self.top_last_words = []
            return message
        while self.text[self.count] == " ":
            self.count += 1
        if self.count > len(self.text):
            message = "Вы сгенерировали Ваш акротекст"
            self.top_last_words = []
            return message
        words = Stego.main(previous_word, self.text[self.count])
        print(words)
        if len(words) == 0:
            print("alarm")
            message = "Выберите другое слово"
            return message
        self.count += 1
        self.top_last_words = words
        print(self.count)
        return "Ok"

    def return_word(self, previous_word):
        self.count -= 2
        while self.text[self.count] == " ":
            self.count -= 1
        print(self.count)
        words = Stego.main(previous_word, self.text[self.count])
        print(words)
        self.count += 1
        self.top_last_words = words
        return "Ok"

    def get_top_words(self):
        return self.top_last_words

