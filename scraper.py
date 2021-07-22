from bs4 import BeautifulSoup
import requests
import re


def print_paragraphs(paragraph_list):
    j = 0
    for i in paragraph_list:
        j += 1
        print(j)
        i = i.text.strip()
        i = i.replace('\n', '')
        i = re.sub('\s\s+', ' ', i)
        print(i)
        print('\n')


def get_paragraps(url, class_name_filter):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    paragraph_list = soup.find_all("p", class_=class_name_filter)
    return paragraph_list


def main():
    # TODO
    # 1
    # create db
    # create dictionary of links
    # compare url to dictionary
    # if not found get site as object
    #  link
    #  title
    #  paragraph_list
    # save to db

    # 2
    # make scritp that scans links from https://yle.fi/uutiset/tuoreimmat
    # compare list to dictionary and operate accordingly

    url = 'https://yle.fi/uutiset/3-12025156'
    filter_pattern = 'yle__article__paragraph'
    paragraph_list = get_paragraps(url, filter_pattern)
    print_paragraphs(paragraph_list)


if __name__ == "__main__":
    main()
