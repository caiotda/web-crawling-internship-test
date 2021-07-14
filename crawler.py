from bs4 import BeautifulSoup
import pandas as pd
import requests

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', 'Upgrade-Insecure-Requests': '1','DNT': '1','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate'}
    return requests.get(url, headers=headers).text

def extract_product_offers(url):
    wrapper_class_name = 'styles__Wrapper-crf3j2-0 eFgqLx'
    product_wrapper_class = 'styles__ProductGridItem-crf3j2-1'

    productss_html = get_html(url)
    soup = BeautifulSoup(productss_html, 'html.parser')

    wrapper = soup.find('div', {'class': wrapper_class_name})
    products = wrapper.find_all('div', {'class': product_wrapper_class})

    products_df = pd.DataFrame([], columns=['Title', 'Url', 'Sdk'])
    for product in products:
        image = product.find('a', {'class': 'styles__CardMediaWrapper-sc-1gzprri-4 WLhYY'})
        title = image['title']
        url = image['href']
        ind = url.rfind('/')+1
        sdk = url[ind:]
        products_df = products_df.append({'Title': title, 'Url': url, 'Sdk': sdk}, ignore_index=True)
    return products_df

refrigerators_url = 'https://www.extra.com.br/c/eletrodomesticos/refrigeradores/?filtro=c13_c14_c13&des=0TO25'

tvs_url = 'https://www.extra.com.br/c/tv-e-video/televisores/\
          ?filtro=c1_c2&nid=202485&des=0TO100'

printers_url = 'https://www.extra.com.br/c/informatica/z\
                impressoras/?filtro=c56_c61&des=0TO100'


refrigerators = extract_product_offers(refrigerators_url)
tvs = extract_product_offers(tvs_url)
printers = extract_product_offers(printers_url)
print(refrigerators)
print(tvs)
print(printers)