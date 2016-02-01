import urllib.request, re
from bs4 import BeautifulSoup

url = "http://dqname.jp/index.php?md=top&pg="

def kira_link(href):
    return href and re.compile("index.php\?md=view").search(href)

def get_page(pagenum):
    with urllib.request.urlopen(url + str(pagenum)) as page:
        soup = BeautifulSoup(page.read()) #.decode('euc-jp'))
        return soup.find_all(href=kira_link)

def main():
    names = set()
    for i in range(1, 870):
        for kira_link in get_page(i):
            name = kira_link.string
            hiragana = re.search('（[^）]+）', name).group(0).strip('（').rstrip('）')
            kanji = re.search('([^（]+)', name).group(0)
            # print(name, hiragana, kanji)
            names.add((name, hiragana, kanji))

    for (_, hiragana, kanji) in names:
        print(hiragana, kanji)

if __name__ == '__main__':
    main()
