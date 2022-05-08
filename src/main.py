import translators as ts
import pinyin
import kroman


def chinese(text2translate):
    translation = ts.google(text2translate, to_language='zh')
    pinyinline = pinyin.get(translation, delimiter=" ")
    translatelines = text2translate + '\n' + translation + '\n' + pinyinline + '\n'
    file = open('output/chinese.txt', 'w', encoding='utf-8')
    file.write(translatelines)


def korean(text2translate):
    translation = ts.google(text2translate, to_language='ko')
    koreanroman = kroman.parse(translation)
    translatelines = text2translate + '\n' + \
        translation + '\n' + koreanroman + '\n'
    file = open('output/korean.txt', 'w', encoding='utf-8')
    file.write(translatelines)


def spanish(text2translate):
    translation = ts.google(text2translate, to_language='es')
    koreanroman = kroman.parse(translation)
    translatelines = text2translate + '\n' + koreanroman + '\n'
    file = open('output/spanish.txt', 'w', encoding='utf-8')
    file.write(translatelines)


def french(text2translate):
    translation = ts.google(text2translate, to_language='fr')
    translatelines = text2translate + '\n' + translation + '\n'
    file = open('output/french.txt', 'w', encoding='utf-8')
    file.write(translatelines)


def german(text2translate):
    translation = ts.google(text2translate, to_language='de')
    translatelines = text2translate + '\n' + translation + '\n'
    file = open('output/german.txt', 'w', encoding='utf-8')
    file.write(translatelines)


def malay(text2translate):
    translation = ts.google(text2translate, to_language='ms')
    translatelines = text2translate + '\n' + translation + '\n'
    file = open('output/malay.txt', 'w', encoding='utf-8')
    file.write(translatelines)


def arabic(text2translate):
    translation = ts.google(text2translate, to_language='ar')  # zh, ko
    # TODO: Add romanisation translator
    translatelines = text2translate + '\n' + \
        translation + '\n' + koreanroman + '\n'
    file = open('output/arabic.txt', 'w', encoding='utf-8')
    file.write(translatelines)


if __name__ == "__main__":
    text2trans = "Today I am going to the bar at newton street."

    chinese(text2trans)
    korean(text2trans)
    spanish(text2trans)
    french(text2trans)
    german(text2trans)
