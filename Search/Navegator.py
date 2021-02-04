import webdriver_manager.chrome as chrome
import webdriver_manager.firefox as firefox
import webdriver_manager.microsoft as microsoft
from bs4 import BeautifulSoup as bs
from requests import get
from selenium import webdriver

from Search.Elementors import retorna_class


def browser(_url, navegador=None, visivel=False):
    if str(navegador).lower() == 'firefox':
        if visivel is not False:
            op = webdriver.FirefoxOptions()
            op.set_headless()
            _driver = webdriver.Firefox(firefox.GeckoDriverManager().install(), options=op)
        _driver = webdriver.Firefox(firefox.GeckoDriverManager().install())

    elif str(navegador).lower() == 'ie':
        _driver = webdriver.Ie(microsoft.IEDriverManager().install())
    elif str(navegador).lower() == 'edge':
        _driver = webdriver.Edge(microsoft.EdgeChromiumDriverManager().install())
    else:
        if visivel is not False:
            op = webdriver.ChromeOptions()
            op.set_headless()
            _driver = webdriver.Chrome(chrome.ChromeDriverManager().install(), options=op)
        else:
            _driver = webdriver.Chrome(chrome.ChromeDriverManager().install())

    _driver.implicitly_wait(30)
    assert isinstance(_url, object)
    _driver.get(_url)
    _text = _driver.page_source
    _driver.close()
    _driver.quit()

    return _text


def request(_url):
    _text = get(_url).text
    return _text


def documents(path):
    _text = open(path, 'r', encoding='utf8')
    _element = bs(_text, 'html.parser')
    return str(_element)


# xpto = browser('../Tela_Cadastro.txt')
xpto = browser('https://www.pyjobs.com.br/jobs/')
elemento = bs(xpto, 'html.parser')

for i in retorna_class(elemento):
    print(i)
