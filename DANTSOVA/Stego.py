# -*- coding: utf-8 -*-
"""
    This is module of acrostego.
    You can use it, if platform is build.

    If platform is not build, please use:
    1) collect *.fb2 files in your language
    2) run build_platform
    3) spend a lot of time... (Ha-ha-ha!! MANY TIME!!!)
    4) rejoice!
    5) run this module
    6) rejoice again!

    PavelMSTU@stego.su
    ~I am SOMBE(=Sorry Of My Bad English)
    create in: 2014-08-06
"""

__version__ = "07.09.2014"
__author__ = 'PavelMSTU'
__copyright__ = 'LGPL'

import os
from DANTSOVA import MarkoffLib

# Path to built platform
PLATFORM_PATH = os.path.join("DANTSOVA/platform_build", "dantsova.d0.plf")

# Correct alphabet of your language
CORRECT_ALPHABET = "йцукенгшщзхъфывапролджэячсмитьбю"


def test(previous_word, letter, count_of_words):
    platform = MarkoffLib.load_chain(PLATFORM_PATH)
    if not platform:
        error = 'Not platform in "{0}"'.format(PLATFORM_PATH)
        raise EnvironmentError(error)
    words = MarkoffLib.get_last_words(previous_word, platform, letter, count_of_words)
    return words


def main(previous_word, letter, count_of_words):
    top_words = test(previous_word, letter, count_of_words)
    return top_words
