import pykakasi
import dic

kks = pykakasi.kakasi()

def convert(string):
    hiragana_array = []
    hiragana = ""
    ans = ""

    result = kks.convert(string)
    for item in result:
        hiragana_array.append(item["hira"])

    hiragana = str(" ".join(hiragana_array))

    for i in hiragana:
        if i not in dic.morse:
            ans += i + " "
        else:
            ans += dic.morse[i] + " "
    return ans