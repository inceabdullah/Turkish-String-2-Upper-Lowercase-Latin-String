
lower_map = { # `ı, İ, ü, Ü, ğ, Ğ, ş, Ş, ç, Ç, â, î, û`, ö, Ö
    ord(u'ı'): u'i',
    ord(u'İ'): u'i',
    ord(u'ü'): u'u',
    ord(u'Ü'): u'u',
    ord(u'ğ'): u'g',
    ord(u'Ğ'): u'g',
    ord(u'ş'): u's',
    ord(u'Ş'): u's',
    ord(u'ç'): u'c',
    ord(u'Ç'): u'c',
    ord(u'â'): u'a',
    ord(u'î'): u'i',
    ord(u'û'): u'ü',
    ord(u'ö'): u'o',
    ord(u'Ö'): u'o',
    
    }

    # lower_map from https://stackoverflow.com/questions/19030948/python-utf-8-lowercase-turkish-specific-letter?answertab=votes#tab-top

def konvert(turkishString, convert2 = "L"): # lowercase, uppercase. ilk versiyon sadece lowercase icin

    # first, lowercase function
    lowerTurkishString = turkishString.lower()
    translatedLowerTurkishString = bytes(lowerTurkishString, encoding='utf8').decode("utf-8").translate(lower_map)

    return translatedLowerTurkishString