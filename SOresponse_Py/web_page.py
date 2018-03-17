from bs4 import BeautifulSoup
import requests
import re

def web_page(url):
    """
    This function loads Stack Overflow response webpage and returns the title of question.

    Input:
        url: A valid URL of a Stack Overflow webpage. Must be the type of String.
    Output:
        qestion: The question being asked on the given Stack Overflow response webpage.
           If unsuccessful corresponding error will be returned.
    """

    try:
        # load the webpage
        web_data1 = requests.get(url)
        soup1 = BeautifulSoup(web_data1.text, "lxml")
        # select title of question in webpage
        question1 = soup1.select("#question-header .question-hyperlink")
        # remove HTML tags using regular expression
        str_q1 = re.sub(r'</?\w+[^>]*>','', str(question1[0]))
        return str_q1

    except:
        # raise an error if the link is invalid
        raise TypeError("This is not a valid Stack Overflow link!")
