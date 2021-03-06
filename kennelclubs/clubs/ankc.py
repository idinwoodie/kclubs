from bs4 import BeautifulSoup
import csv
import os
import requests


def fetch_data(data_dir):
    page = requests.get(
        'http://ankc.org.au/Breed/Index/0?Search.ItemsPerPage=0')
    soup = BeautifulSoup(page.text, 'html.parser')
    selection = soup.find(id='LstBreeds')
    with open(os.path.join(data_dir, 'ankc.csv'), 'w') as outfile:
        wr = csv.writer(outfile, lineterminator=',\n')
        for linenum, breed in enumerate(selection.find_all(class_='custom-padding-left-20 title')):
            if not linenum:
                wr.writerow(['breed'])
            wr.writerow([breed.text.rstrip()])


if __name__ == '__main__':
    club_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
    data_dir = os.path.join(os.path.split(club_dir)[0], 'data')
    fetch_data(data_dir)
