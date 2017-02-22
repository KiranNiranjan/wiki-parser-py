from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import unicodedata
import re


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

    def get_paragraph(self, num):
        p_to_json = Converter(self.html_content.find_all('div', class_='mw-content-ltr')[0])
        return p_to_json.paragraph_to_json(num)

    def get_main_image(self):
        img_to_json = Converter(self.html_content.find_all('div', class_='mw-content-ltr')[0])
        return img_to_json.img_to_json()


class Converter:
    def __init__(self, data):
        self._data = data
        pass

    def table_to_json(self):
        trs = self._data.find_all('tr')
        table_data = {}
        for tr in trs:
            key = None
            value = None
            data = self.data_to_array(tr)

            for i, item in enumerate(data):

                if i == 0:
                    if hasattr(item, 'string'):
                        key = self.process_td_key(item)
                        key = self.string_normalize(key)
                else:
                    value = self.process_td_value(item)
                    value = self.string_normalize(value)

            if key and value is not None: table_data[key] = value

        return table_data

    """ Method To get Paragraph """

    def paragraph_to_json(self, num):
        paras = self._data.find_all('p')
        paragraph_data = {}
        strings = ''
        for i, para in enumerate(paras):
            data = self.data_to_array(para)

            if i > num:
                break
            for string in data.find_all(string=True):
                string = self.string_normalize(string)
                if string is not None and string != '\n': strings += string
        paragraph_data['data'] = strings
        return paragraph_data

    """ Method To get Main Image """

    def img_to_json(self):
        images = self._data.find_all('img')
        img_string = images[0]['src']
        index = img_string.rfind('/') + 1
        img_object = {'fileName': img_string[index:], 'link': 'https:' + img_string}
        return img_object

    @staticmethod
    def process_td_key(item):
        for string in item.find_all(string=True):
            if string is not None and string != '\n': return string

    @staticmethod
    def process_td_value(items):
        strings = ''
        for string in items.find_all(string=True):
            if string != '\n': strings += ' ' + string
        return strings.strip()

    @staticmethod
    def data_to_array(data):
        try:
            while '\n' in data.contents: data.contents.remove('\n')
        except:
            pass
        return data

    @staticmethod
    def string_normalize(string):
        if string is not None:
            string = unicodedata.normalize("NFKD", string)
            string = string.replace('\n', ' ')
            string = re.sub('\\[.*?\\]', '', string)
        return string


# Method to get info box from wikipedia
def infoBox(url):
    features = GetFeatures(url)
    return features.get_info_box()


# Method to get paragraph from wikipedia
def getParagraph(url, num=2):
    features = GetFeatures(url)
    return features.get_paragraph(num)


# Method to get Main image from wikipedia
def getMainImage(url):
    features = GetFeatures(url)
    return features.get_main_image()


# Main functions
def wiki_parser(url):
    soup = GetData(url)


if __name__ == "__main__": wiki_parser()
