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
from typing import List, Any, Union

__version__ = "07.09.2014"
__author__ = 'PavelMSTU'
__copyright__ = 'LGPL'

import os
import random
from DANTSOVA import MarkoffLib

# Path to built platform
PLATFORM_PATH = os.path.join("DANTSOVA/platform_build", "dantsova.d0.plf")

# Correct alphabet of your language
CORRECT_ALPHABET = "йцукенгшщзхъфывапролджэячсмитьбю"


def test(message):
    random.seed(message)
    platform = MarkoffLib.load_chain(PLATFORM_PATH)

    if not platform:
        error = 'Not platform in "{0}"'.format(PLATFORM_PATH)
        raise EnvironmentError(error)

    all_text_by_c = dict()
    for c in [8, 10, 12, 20]:
        text = MarkoffLib.make_acrotext(platform, message, c=c, correct_alphabet=CORRECT_ALPHABET)
        #print("return text. c=@c@ message='@m@'::" \
        #     .replace('@c@', str(c)) \
        #      .replace('@m@', message))
        #print("::::")
        #text2 = text.replace(u'.', u'.\n')
        #all_text_by_c[c] = text
        #print(text2)
        #print("::::")

    #print(u'All text by c param:')
    #for c in all_text_by_c.keys():
    #    print(u"c={0}. m={1}. text={2}".format(c, message, all_text_by_c[c]))
    return text


##############
def main(message):
    acrotext = test(message)
    return acrotext
