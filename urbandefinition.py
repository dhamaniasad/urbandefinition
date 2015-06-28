import requests
from bs4 import BeautifulSoup
import argparse


def get_definition(term):
    r = requests.get('http://www.urbandictionary.com/define.php?term={}'.format(term))
    soup = BeautifulSoup(r.content)
    definition = soup.find(class_='def-panel')
    meaning = definition.find(class_='meaning').text
    print "Meaning: {}".format(meaning)
    example = definition.find(class_='example')
    breaks = example.find_all('br')
    for br in breaks:
        br.replace_with('\n')
    print "Example: {}".format(example.text)



def command_line_runner():
    parser = argparse.ArgumentParser(description="Get Urban Dictionary definitions from the terminal")
    parser.add_argument('term', type=str, nargs='*', help='The term you want the urban definition for')
    args = parser.parse_args()
    if not args.term:
        parser.print_help()
    else:
        get_definition(' '.join(args.term))


if __name__ == '__main__':
    command_line_runner()
