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

# Format so the headers are always evenly spaced
def format_header(title, width):
    # print("\n")
    # only used to adjust the title length
    title_len = len(title)
    spacing = (int(width) - int((title_len)))

    # find whether the number is odd
    # Store the larger number as the second variable
    if spacing % 2 == 1:
        first_spacing = int(spacing / 2)
        second_spacing = int(spacing / 2) + 1
    
    else:
        first_spacing = int(spacing / 2)
        second_spacing = int(spacing / 2) + 1

    # name, ingredients, prep_time, cook_time, serves, steps, description
    # layout a nice display of the recipe selected
    print("\n")
    print("*" * first_spacing + f" {title} " + "*" * second_spacing)
    print("\n")