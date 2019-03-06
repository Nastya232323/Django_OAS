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
    print(top_last_words)
    return top_last_words


def append_first_words(words, word, count_of_next_words):
    if word == "." or word == "":
        return words
    position = 0
    i = 0
    while (count_of_next_words < words[i][1]) and (i < len(words)):
        if i == len(words) - 1:
            break
        i += 1
        position += 1
    if position < 100:
        append_word = [word, count_of_next_words]
        extract_word = words[position]
        for j in range(position, len(words)):
            words[j] = append_word
            append_word = extract_word
            if j != len(words) - 1:
                extract_word = words[j+1]
            else:
                words.append(append_word)
    if len(words) > 100:
        words.pop()
    return words


def generation_first_word(letter, platform):
    words = list()
    top_first_words = list()
    for key in platform:
        if key != "":
            if key[0] == letter:
                if len(words) == 0:
                    words.append([key, len(platform[key])])
                else:
                    words = append_first_words(words, key, len(platform[key]))
    for i in range(len(words)):
        top_first_words.append(words[i][0])
    return top_first_words


def get_last_words(previous_word, platform, letter):
    if previous_word == "":
        return generation_first_word(letter, platform)
    print(letter)
    top_last_words = list()
    top_last_message = list()
    last_words = platform[previous_word]
    print(last_words)
    for i in range(len(last_words) - 1):
        if last_words[i][0] == "":
            continue
        if len(top_last_words) == 0:
            if last_words[i][0][0] == letter:
                top_last_words.append(last_words[i])
                continue
        if last_words[i][0][0] == letter:
            top_last_words = generation_top_last_words(top_last_words, last_words[i])
    for i in range(len(top_last_words)):
        top_last_message.append(top_last_words[i][0])
    print(top_last_message)
    return top_last_message


