from bs4 import BeautifulSoup, NavigableString, Tag
import requests


class GetData:
    def __init__(self, url):
        self._url = url

        """ Get Html content """
        web_page = requests.get(self._url)
        self.html_content = BeautifulSoup(web_page.text, 'html.parser')

    def get_data(self):
        return self.html_content

    def get_tables(self):
        return self.html_content.find_all('table')


class GetFeatures(GetData):
    def __init__(self, url):
        super().__init__(url)

    def get_info_box(self):
        t_to_json = Converter(self.html_content.find_all('table', class_='infobox')[0])
        return t_to_json.table_to_json()


class Converter:
    def __init__(self, data):
        self._data = data
        pass

    def table_to_json(self):
        trs = self._data.find_all('tr')
        table_data = {}
        for tr in trs:
            if tr.td:
                key = self.process_td_key(tr.td)
                for i, td_siblings in enumerate(tr):
                    if isinstance(td_siblings, NavigableString):
                        continue
                    if isinstance(td_siblings, Tag):
                        value = self.process_td_value(td_siblings)
                        if key and value: table_data[key] = value
        print(table_data)

    @staticmethod
    def process_td_key(td):

        if td.a:
            if hasattr(td.a, 'string'):
                return td.a.string
            elif td.a.span:
                if hasattr(td.a.span, 'string'):
                    return td.a.span.string

        if td.span:
            if hasattr(td.span, 'string'):
                return td.span.string

        if hasattr(td, 'string'):
            return td.string

    @staticmethod
    def process_td_value(td):

        if td.a:
            if hasattr(td.a, 'string'):
                return td.a.string

        if td.span:
            if hasattr(td.span, 'string'):
                return td.span.string

        if hasattr(td, 'string'):
            return td.string


# Method to get info box from wikipedia
def infoBox(url):
    features = GetFeatures(url)
    print(features.get_info_box())


# Main functions
def wiki_parser(url):
    soup = GetData(url)

    return infoBox(url)


if __name__ == "__main__": wiki_parser("https://en.wikipedia.org/wiki/Methane")
