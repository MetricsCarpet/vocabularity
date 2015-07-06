import os


ROOT = os.path.dirname(__file__)
MIN_LEN = 3


dictionaries = {
    # Apache-office spelling dictionary.
    'apache_openoffice': {
        'language': 'en_US',
        'download_date': '05062015',
        'url': 'http://extensions.openoffice.org/en/project/'
               'english-dictionaries-apache-openoffice',
        'file': os.path.join(ROOT, 'apache_openoffice_7en_US.dic'),
    }
}


def load_dictionary(name):
    location = dictionaries[name]['file']
    return [line for line in open(location).readlines()
            if len(line) >= MIN_LEN]
