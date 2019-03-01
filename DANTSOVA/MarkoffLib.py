# -*- coding: utf-8 -*-
"""
    This module contains two functions:
      * safe_chain
      * load_chain
      * make_acrotext

    PavelMSTU@stego.su
    ~I am SOMBE(=Sorry Of My Bad English)
    create in: 2014-08-03
"""
__version__ = "07.09.2014"
__author__ = 'PavelMSTU'
__copyright__ = 'LGPL'


import codecs
import datetime
import json
import sys


def safe_chain(chain, path):
    """
    safe chain
    """
    fw= codecs.open (path, 'w', encoding='utf8')
    begin = datetime.datetime.now()
    print("SafeChain:")
    str_chain = json.dumps(chain,
              sort_keys=True,
              ensure_ascii=False
              )

    #INFO для удобства восприятия в Notepad++
    str_chain = str_chain.replace(']], ', ']],\n')
    str_chain = str_chain.replace('], ', '],\n\t')
    u_str_chain = str_chain.decode('utf8')
    fw.write(u_str_chain)

    end = datetime.datetime.now()
    spendtime = (end-begin)

    print(":done. " + str(spendtime))

    fw.close()


def load_chain(path):
    """

    """
    chain = None
    fr = None
    try:
        fr = open(path, 'r')
        chain = json.load(fr)
    except:
        print("ERROR: " + str(sys.exc_info()))
        return None
    finally:
        if fr != None:
            fr.close()
    return chain


def __step(platform, keys, keys_letter,  letter, textlist, c, error_words=None, depth=0):
    """
    Шаг алгоритма
    TODO
    :param platform:
    :param keys:
    :param keys_letter:
    :param letter:
    :param textlist:
    :param c:
    :return: True -- если удалось. False -- если ошибка стеганографии
    """
    def __count_words(textlist):
        count = 1
        while textlist[-count] != u".":
            count += 1
        return count

    depth_bad_error = list()
    while(True):

        if error_words is None:
            error_words = list()

        next_word = None
        last_word = textlist[-1]

        point_exist = False
        if last_word == u'.':
            words = keys_letter[letter]
            #i = random.randrange(len(words))
            i_max = -1
            max = 0
            for i in range(len(words)):
                next_word = words[i]
                pot = platform[next_word]
                if len(pot) > max:
                    i_max = i
                    max = len(pot)
            next_word = words[i_max]
            textlist.append(next_word)
            return True

        pot = platform[last_word]
        i_pot_good = list()

        #Найдём все слова.
        for i in range(len(pot)):
            #if i == 578:
            #    print 'dd'
            #print i
            word = pot[i][0]
            if len(word)<1 and word != u'.':
                mess= u'Мусор в i=@i@ в слове "@last_word@"->"@word@"'\
                    .replace(u'@last_word@', last_word)\
                    .replace(u'@i@', str(i))\
                    .replace(u'@word@', word)
                #TODO print mess
                continue
            if word[0] == letter:
                i_pot_good.append(i)
            if word == u'.':
                point_exist = True

        i_max = -1
        max = 0
        for i in i_pot_good:
            count = pot[i][1]
            if count > max:

                #Проверяем, что слово не из левого списка:
                word = pot[i][0]
                isuse = True
                for word_ch in error_words:
                    if word_ch == word:
                        isuse = False
                        break

                if isuse:
                    i_max = i
                    max = count

        if i_max==-1:
            if point_exist:
                next_word = u'.'
                textlist.append(next_word)
                return __step (platform, keys, keys_letter,  letter, textlist, c)
            #мы не нашли слова -- ошибка стеганографии.

            #TODO сделать глубину более глубокой, чем на 1
            if depth == 0:
                bad_word = textlist[-1]
                print(u">>-" + bad_word)
                textlist.pop(-1)
                depth_letter = bad_word[0]
                depth_bad_error.append(bad_word)
                is_good = __step (
                    platform, keys, keys_letter, depth_letter,  textlist, c,
                    error_words=depth_bad_error, depth=depth+1
                )
                if is_good:
                    print(u">>+" + textlist[-1])
                    continue
                #else
                #уберём слово и добавим прошлое
                textlist.pop(-1)
                textlist.append(bad_word)
                #сознательно допускаем ошибку
            i_max = -1
            max = 0
            for i in range(len(pot)):
                count = pot[i][1]
                if count > max:
                    i_max = i
            next_word = pot[i_max][0]
            textlist.append(next_word)
            return False
        else:
            next_word = pot[i_max][0]
            textlist.append(next_word)

            if __count_words(textlist) > c:
                if point_exist:
                    next_word = u"."
                    textlist.append(next_word)
            return True


def generation_top_last_words(top_last_words, new_word):
    if new_word[0] == '.' or new_word[0] == "":
        return top_last_words
    position = 0
    i = 0
    while (new_word[1] < top_last_words[i][1]) and (i < len(top_last_words)):
        if i == len(top_last_words) - 1:
            break
        i += 1
        position += 1
    if position < 100:
        append_word = new_word
        extract_word = top_last_words[position]
        for j in range(position, len(top_last_words)):
            top_last_words[j] = append_word
            append_word = extract_word
            if j != len(top_last_words) - 1:
                extract_word = top_last_words[j+1]
            else:
                top_last_words.append(append_word)
    if len(top_last_words) > 100:
        top_last_words.pop()
    return top_last_words


def get_last_words(acrotext, platform, letter):
    top_last_words = list()
    top_last_message = list()
    last_words = platform[acrotext[len(acrotext) - 2]]
    for i in range(len(last_words) - 1):
        if len(top_last_words) == 0:
            top_last_words.append(last_words[i])
            continue
        if last_words[i][0] == "":
            continue
        if last_words[i][0][0] == letter:
            top_last_words = generation_top_last_words(top_last_words, last_words[i])
    for i in range(len(top_last_words) - 1):
        top_last_message.append(top_last_words[i][0])
    print(top_last_message)
    return top_last_message


def make_acrotext(platform, message, c=10, ret_list=False, correct_alphabet= "йцукенгшщзхфвапролджэячсмитбю"):
    """
    Make acrotext by platform.
    platform must be build by build_platform function

    If you don't know, what is acrotext, you must do:
        1) learn Russian
        2) read article by Ivan Chudasoff "ОТ АКРОСТИХА К АКРОКОНСТРУКЦИИ":http://rifma.com.ru/Chudasov-2.htm
    Good luck! Don't worry, because it can be worse, if language will be Hungarian...
    O... You can read wiki in english: https://en.wikipedia.org/wiki/Acrostic
    But acrotext is a more general concept...

    :param platform: platform, built by load_chain function.
    :param message: message in u'...' format
    :param c: параметр, показывающий со скольки слов можно ставить '.'
    :return: возвращает текст, на перывх буквах которых стоит текст message
    """
    textlist = list()
    keys = list()
    keys_letter = dict()
    for key in platform:
        if len(key) < 2:
            # INFO garbage in platform
            continue
        keys.append(key)
        letter = key[0]
        if keys_letter.get(letter):
            keys_letter[letter].append(key)
        else:
            new_letter_list = list()
            new_letter_list.append(key)
            keys_letter[letter] = new_letter_list

    textlist.append(u'.')
    correct_count = 0
    uncorrect_count = 0
    for letter in message:
        if letter not in correct_alphabet:
            continue
        try:
            correct = __step(platform, keys, keys_letter, letter, textlist, c)
        except:
            print(u"ERROR in __step(platform, keys, keys_letter, letter, textlist, c)"\
                .replace(u'letter', letter)\
                .replace(u'c', str(c)))
            print(str(sys.exc_info()))
            correct = __step(platform, keys, keys_letter, letter, textlist, c)
        if correct:
            correct_count += 1
        else:
            uncorrect_count += 0
        print(correct)

        print(u">>" + textlist[-1])

    rettext = ""
    top_last_message = get_last_words(textlist, platform, message[len(message) - 1])
    print(top_last_message)
    textlist.pop()
    for word in textlist:
        rettext += word
        if word != ".":
            rettext += " "
    return rettext, top_last_message

