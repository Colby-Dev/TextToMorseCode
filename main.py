#This function takes an input then returns the input as morse code. This was a timed challenge and the solution below was created in 5 min 21 seconds (5:23)

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
