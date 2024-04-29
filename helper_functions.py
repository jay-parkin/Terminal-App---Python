import textwrap
from bs4 import BeautifulSoup

# Wraps the method into 50 chartacters when saved
def word_wrap(text, width=50):
    wrapped_text = textwrap.fill(text, width=width)

    return wrapped_text

def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    clean_text = soup.get_text()
    return clean_text