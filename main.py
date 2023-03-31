def textToMorse(input):
    listedInput = list(input.upper())
    morse = []
    MorseCodeDict = {
        'A': '. ---',
        'B': '--- . . .',
        'C': '--- . --- .',
        'D': '--- . .',
        'E': '.',
        'F': '.. --- .',
        'G': '--- --- .',
        'H': '. . . .',
        'I': '. .',
        'J': '. --- --- ---',
        'K': '--- . ---',
        'L': '. --- . .',
        'M': '--- ---',
        'N': '--- .',
        'O': '--- --- ---',
        'P': '. --- --- .',
        'Q': '--- --- . ---',
        'R': '. --- .',
        'S': '...',
        'T': '---',
        'U': '. . ---',
        'V': '... ---',
        'W': '. --- ---',
        'X': '--- . . ---',
        'Y': '--- . --- ---',
        'Z': '--- --- . .',
        ' ': ' / '
    }
    
    for each_char in listedInput:
        morse.append(MorseCodeDict[each_char])
    morseText = ''.join(morse)
    return print(f'You entered {input} and the result was {morseText}')


textToMorse('Hello World')