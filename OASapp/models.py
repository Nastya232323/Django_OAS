from django.db import models
from DANTSOVA import Stego


class AcroText(models.Model):
    acrotext = models.CharField(max_length=1000)
    top_last_words = list()

    def __init__(self, text):
        result = Stego.main(text)
        self.acrotext = result[0]
        self.top_last_words = result[1]

    def get_top_words(self):
        return self.top_last_words
