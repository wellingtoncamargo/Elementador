"""
Metodos para realizar busca em todos os Atributos da página
"""


def busca_tags(_elements):
    """
    Realiza uma varredura em todas as tags da página para auxiliar na busca de atributos do campo
    :param _elements: Objeto texto do html
    :return: Lista de Tags que a página contem
        Ex:
            ['div', 'a', 'p', 'option']

    """
    tag_line = set()
    for _element in _elements.find_all('body'):
        limpando = str(_element).replace('>', ' ')
        limpando = limpando.replace('\n', ' ')
        limpando = limpando.replace('<!--', '')
        tags = limpando.split(' ')
        for i in tags:
            if '<' in i and '/' not in i:
                if i not in tag_line:
                    tag_line.add(i.replace('<', ''))
    return sorted(tag_line)


def retorna_texto(elements):
    """
    Realiza uma busca em todos os textos da página
    :param elements: Objeto texto do html
    :return: Lista com o nome e o Xpath dos campos que contem texto
        Ex:
            text_Estado = "//*[contains(text(),'Estado')]" tipo="XPATH"
    """
    tags = [i for i in busca_tags(elements)]
    _element_text = set()
    for _element in elements.find_all(tags):
        limping = str(_element).split('\n')
        Texts = set()
        for i in limping:
            try:
                for tags in busca_tags(elements):
                    if i.find(tags) != -1:
                        i = i.replace('<!-- -->', '')
                        i = i.replace('\n', ' ')
                        for n in i.split('<'):
                            if n:
                                if n:
                                    n = n.replace('/>', '>').strip()
                                    n_1 = n.split('>')[-1].strip()
                                    if n_1.strip():
                                        if n_1 not in Texts:
                                            Texts.add(n_1)
                                        pass
            except TypeError:
                pass

        if sorted(Texts):
            for i in sorted(Texts):
                if i.strip() not in _element_text:
                    i1 = i.strip().replace(' ', '_')
                    i1 = i1.strip().replace('.', '')
                    i1 = i1.strip().replace(',', '_')
                    i2 = f"'{i.strip()}'"
                    _element_text.add(f'text_{i1} = "//*[contains(text(),{i2})]" tipo="XPATH"')

    return sorted(_element_text)


def retorna_id(elements):
    """
    Realiza uma busca em todos os id da página
    :param elements: Objeto texto do html
    :return: Lista com o nome e o id dos campos
        Ex:
            id_navbarDropdown= id="'navbarDropdown'" tipo="ID"
    """
    attributes = "id"
    tags = [i for i in busca_tags(elements)]
    _element_id = set()
    for _element in elements.find_all(tags):
        try:
            if _element.get(attributes) is not None:
                if _element.get(attributes) not in _element_id:
                    _i = _element.get(attributes).strip()
                    id1 = f"'{_i}'"
                    _element_id.add(f'{attributes}_{_i} = {attributes}="{id1}" tipo="{attributes.upper()}"')
        except Exception:
            pass
    return sorted(_element_id)


def retorna_class(elements):
    """
    Realiza uma busca em todos os class da página
    :param elements: Objeto texto do html
    :return: Lista com o nome e o class dos campos
        Ex:
            class_vaga= class="vaga" tipo="CLASS"
    """
    attributes = "class"
    tags = [i for i in busca_tags(elements)]
    _element_class = set()
    for _element in elements.find_all(tags):
        for i in _element.find_all(tags):
            if i.get(attributes) is not None:
                for i in i.get(attributes):
                    if i not in _element_class:
                        _i = i.strip()
                        _element_class.add(f'{attributes}_{_i} = {attributes}="{_i}" tipo="{attributes.upper()}"')

    return sorted(_element_class)


def retorna_name(elements):
    """
    Realiza uma busca em todos os id da página
    :param elements: Objeto texto do html
    :return: Lista com o nome e o name dos campos
        Ex:
            name_pesquisa= name="pesquisa" tipo="NAME"
    """
    attributes = "name"
    tags = [i for i in busca_tags(elements)]
    _element_name = set()
    for _element in elements.find_all(tags):
        if _element.get(attributes):
            name = str(_element.get(attributes)).strip()
            if name:
                atr_name = f'{attributes}_{name}= {attributes}="{name}" tipo="{attributes.upper()}"'
                if atr_name not in _element_name:
                    _element_name.add(atr_name)

    return sorted(_element_name)


def retorna_xpath(elements):
    """
    Realiza uma busca em todos os textos da página
    :param elements: Objeto texto do html
    :return: Lista com o nome e o Xpath dos campos que contem texto
        Ex:
            text_Estado = "//*[contains(text(),'Estado')]" tipo="XPATH"
    """
    tags = [i for i in busca_tags(elements)]
    _element_text = set()
    for _element in elements.find_all(tags):
        limping = str(_element).split('\n')
        atrib = set()
        for i in limping:
            try:
                for _tags in busca_tags(elements):
                    if i.find(_tags) != -1:
                        for n in i.split(' '):
                            if '<' in n and '/' not in n:
                                anot = n.split('>').pop()
                                if '<' in anot and '!--' not in anot and ':' not in anot:
                                    anot = anot.replace('<', '').strip()
                                    if anot.islower():
                                        anot
                            if '=' in n:
                                atr = str(n.split('=')[0]).strip()
                                if atr not in atrib:
                                    atr

                                    if anot and atr and ':' not in anot and '<' not in anot:
                                        a = anot, atr
                                        if a not in atrib:
                                            atrib.add(a)

                for at in sorted(atrib):
                    value = _element.get(at[1])
                    if value:
                        # if len(value[1]) > 1:
                        #     print(at[0], at[1], ' '.join(value))
                        # if len(value[1]) == 1:
                        print(at[0], at[1], value)
            except Exception or TypeError:
                pass


    #         for i in sorted(Texts):
    #             if i:
    #                 name = i.replace(']', '')
    #                 name = name.replace('"', '')
    #                 name = name.replace('/', '-')
    #                 name = name.replace('?', '')
    #                 name = name.split('=')[1].replace(' ', '_')
    #                 if name:
    #                     xpth = f'xpath_{name} = "//{i}" tipo="XPATH"'
    #                     if i not in _element_text and i is not None:
    #                         _element_text.add(xpth)
    #
    # for i in sorted(_element_text):
    #     print(i)


def retorna_custom(elements, attrib):
    """
    Realiza uma busca em todos os id da página
    :param attrib: Atributo que deseja buscar
    :param elements: Objeto texto do html
    :return: Lista com o nome e o name dos campos
        Ex:
            name_pesquisa= name="pesquisa" tipo="NAME"
    """
    attributes = attrib
    tags = [i for i in busca_tags(elements)]
    _element_custom = set()
    for _element in elements.find_all(tags):
        if _element.get(attributes):
            custom = str(_element.get(attributes)).strip()
            custom1 = f"'{custom}'"
            if custom:
                xpath = f'custom_{custom} = "//*[@{attributes}={custom1}]" tipo="XPATH"'
                if xpath not in _element_custom:
                    _element_custom.add(xpath)

    return sorted(_element_custom)
