from bs4 import BeautifulSoup
import requests

def get_html(url):
    return requests.get(url).text

refrigerators_url = 'https://www.extra.com.br/c/eletrodomesticos/refrigeradores/?filtro=c13_c14_c13&des=0TO25'

tvs_url = 'https://www.extra.com.br/c/tv-e-video/televisores/\
          ?filtro=c1_c2&nid=202485'

printers_url = 'https://www.extra.com.br/c/informatica/z\
                impressoras/?filtro=c56_c61'
