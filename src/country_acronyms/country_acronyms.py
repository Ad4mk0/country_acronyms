from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
import pycountry
import requests
import re


def get_supported_languages():
    "Returns dict of supported languages"
    translator = GoogleTranslator()
    return translator.get_supported_languages(as_dict=True)


def get_country_acronyms(name: str):
    "Return dictionary of country acronyms for speficied name"
    # Using GoogleTranslator for finding all the acronyms
    translator = GoogleTranslator()
    langs_dict = translator.get_supported_languages(as_dict=True)

    dict = {}

    translated = set()
    for lang in langs_dict:
        translated = GoogleTranslator(
            source='en', target=langs_dict[lang]).translate(name)

        dict[langs_dict[lang]] = translated

    return dict


def get_country_acronyms_iso(iso: str):
    "Return dictionary of country acronyms for speficied country iso"
    # ISO 3166-1 alpha-2 and ISO 3166-1 alpha-3 support, ISO 3166-1 numeric is rubbish
    pattern = r"\b([a-zA-Z]{2,3})\b"
    if not re.match(pattern, iso):
        raise Exception("ISO format is invalid")

    if len(iso) == 3:
        country_details = pycountry.countries.get(alpha_3=iso)
    else:
        country_details = pycountry.countries.get(alpha_2=iso)

    if not country_details:
        raise Exception("Country does not exist")

    return get_country_acronyms(country_details.name)


def get_all_country_acronyms():
    "Will return a dict(List(str)) containing acronyms for every country"

    countries = [r"https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages_(A%E2%80%93C)",
                 r"https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages_(D%E2%80%93I)",
                 r"https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages_(J%E2%80%93P)",
                 r"https://en.wikipedia.org/wiki/List_of_country_names_in_various_languages_(Q%E2%80%93Z)"]

    dict = {}
    for country in countries:
        r = requests.get(country)

        soup = BeautifulSoup(r.text, features="html5lib")

        table = soup.find_all("table")[1]

        s = table.find_all("a")

        for x in s:
            m = table.find_next(x.tag)
            subtable = m.find_all("tr")
            for sub in subtable:
                if len(sub.find_all("td")) > 1:
                    f = sub.find_all("td")[1].find_all("b")
                    list = []
                    for el in f:
                        list.append(el.text)
                    dict[sub.find("td").text.replace("\n", "")] = list

    return dict
