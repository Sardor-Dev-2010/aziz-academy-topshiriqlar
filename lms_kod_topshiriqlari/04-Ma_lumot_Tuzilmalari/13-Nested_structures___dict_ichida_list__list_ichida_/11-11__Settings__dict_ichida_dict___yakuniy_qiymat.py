
th1, lang1, dbg1 = input().split()

th2, lang2, dbg2 = input().split()

settings = {
    'theme': th1,
    'lang': lang1,
    'debug': True if dbg1 == '1' else False,
    'override': {
        'theme': th2,
        'lang': lang2,
        'debug': None if dbg2 == '-' else (True if dbg2 == '1' else False)
    }
}
theme1 = settings['override']['theme'] if settings['override']['theme'] != '-' else settings['theme']
lang1 = settings['override']['lang'] if settings['override']['lang'] != '-' else settings['lang']
debug1 = settings['override']['debug'] if settings['override']['debug'] is not None else settings['debug']
debug2 = '1' if debug1 else '0'
print(theme1, lang1, debug2)

