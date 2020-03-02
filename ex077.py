words = ('aprender', 'matar', 'esquartejar', 'jogar', 'brincar', 'atirar', 'programar', 'acalmar')

for i in sorted(words):
    print("Na palavra {} temos " .format(i), end='')
    for n in i:
        if n.lower() in 'aeiou':
            print(n, end=' ')

    print('')
