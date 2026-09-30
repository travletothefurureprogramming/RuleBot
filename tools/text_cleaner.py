import unicodedata

def strip_accents(text):
    nfd_form = unicodedata.normalize('NFD', text)
    return ''.join(c for c in nfd_form if unicodedata.category(c) != 'Mn')

def clean_input(text:str):
    text = text.lower().strip()

    return strip_accents(text)