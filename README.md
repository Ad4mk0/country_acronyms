
# Project description
## country_acronyms
This package was made for everyone who needs to find all possible translations, acronyms for a specific country name / country iso.



## Acknowledgements
country_acronyms provides the support for the:
- ISO 3166-1 alpha-2 
- ISO 3166-1 alpha-3 




## Contributions
The code lives in a [git repository on GitHub](https://github.com/Ad4mk0/country_acronyms), and issues must be reported in there as well.


## Installation

Install country_acronyms by running:

```bash
  pip install country_acronyms
```
    
## Usage/Examples

```python
from country_acronyms import get_supported_languages, 
                             get_country_acronyms, 
                             get_country_acronyms_iso, 
                             get_all_country_acronyms

# get available languages
get_supported_languages()

>>> {'afrikaans': 'af', 'albanian': 'sq', ... , 'yoruba': 'yo', 'zulu': 'zu'}

# acronyms for given country name
get_country_acronyms("Austria")

>>> {'af': 'Oostenryk', ... , 'zu': 'E-Austria'}

# acronyms for given country iso
get_country_acronyms_iso("it")

>>> {'af': 'Italië', ... , 'zu': 'Italy'}

# acronyms for given country iso
get_country_acronyms_iso("usa")

>>> {'af': 'Verenigde State', ... , 'zu': 'iziwe Ezihlangene'}

# getting all country acronyms by scraping wiki
get_all_country_acronyms()

>>> {'Abkhazia': ['Abcasia', ... , 'Apxazeti'], , 'Afghanistan': ['Æfganisthanaya', ... , 'l-Afghanistan'], ... }

```


## Credits
This package uses the deep_translator, pycountry and bs4.
Big up for those!
## License

The project is licensed under the [MIT License](https://github.com/Ad4mk0/country_acronyms/LICENCE).

