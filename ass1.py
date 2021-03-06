import argparse
import logging
import time
import string
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)


def process(file_path):
    ''' found the frequences of the differnt letters and return a list with the occurrences '''
    logging.info('Reading input file %s ...', file_path)
    # virgola, anzichè % file_path. il punto è che logging è fatto in modo da
    # formattare la stringa solo se deve stampare la particolare stringa-->dipende
    # dal level di logging
    with open(file_path) as input_file:
        # with permette di aprire il file in modo più bello:
        # quando esco dal with il file viene chiuso automaticamente!!
        text = input_file.read()
    num_chars = len(text)
    logging.info('Done, %d characters found', num_chars)

    char_dict = {ch : 0 for ch in string.ascii_lowercase}
    for ch in text:
        try:
            char_dict[ch.lower()] = char_dict[ch.lower()] + 1
        except KeyError:
            pass
    # KeyError viene sollevato quando tento di accedere a un dizionario con una chiave che non esiste

    # Il libro vero inizia con 'I went down'

    num_letters = sum(char_dict.values())
    logging.debug(char_dict)
    logging.info('Done, %d valid characters found', num_letters)
    for ch, num in char_dict.items():
        print(f'{ch} -> {num/num_letters:.3%}')

    return [occ/num_letters for occ in list(char_dict.values())]


def histogram(occ):
    ''' produces an histogram with the given frequences of the letters '''
    plt.bar(list(string.ascii_lowercase), occ)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type = str, help='Path to the input file')
    parser.add_argument('hist', type = int, nargs = '?', const= 1, default = 0 ,help='set 1 to create histogram of letter-occurrences, set 0 to not create the histogram')
    args = parser.parse_args()
    start_time = time.time()
    occur = process(args.infile)
    elapsed_time = time.time() - start_time
    logging.info('Done in %.4f seconds', elapsed_time)
    if (args.hist==1):
        histogram(occur)
