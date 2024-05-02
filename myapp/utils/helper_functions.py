import textwrap
from bs4 import BeautifulSoup

# Wraps the method into 50 chartacters when saved
def word_wrap(text, width=50):
    wrapped_text = textwrap.fill(text, width=width)

    return wrapped_text

def get_first_sentence(text):
    # Find the first period in the text
    period_index = text.find('.')

    # Check if there is a period in the text
    if period_index != -1:

        # Return the text up to the first period
        return text[:period_index + 1]
    else:
        return text

def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    clean_text = soup.get_text()
    return clean_text
