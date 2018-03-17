from bs4 import BeautifulSoup
import requests
import re
import numpy as np

def response_stats(url):
    """
    This function returns a list of statistics about the question being asked on a Stack Overflow page.

    Input:
        url: An object that used the `web_page()` function.
    Output:
	    list: Returns a dictionary of length 4 that includes number of responses, average reputation score,
              top reputation score and author's reputation score.
    """

    # load the webpage and select all responses
    web_data3 = requests.get(url)
    soup3 = BeautifulSoup(web_data3.text, "lxml")
    responses = soup3.select("#answers .post-text")

    # get all reputation scores appear on the specified webpage in a list
    scores = soup3.select(".reputation-score")
    scores_str = []
    # remove HTML tags
    for i in range(0, len(scores)):
        scores_str.append(re.sub(r'</?\w+[^>]*>','', str(scores[i])))

    for j in range(0, len(scores_str)):
        # for example: change 1.3k into 1300
        if '.' in scores_str[j]:
            scores_str[j] = re.sub(r'\.', '', scores_str[j])
            scores_str[j] = re.sub(r'k', '00', scores_str[j])

        # for example: change 13k into 13000
        if 'k' in scores_str[j]:
            scores_str[j] = re.sub(r'k', '000', scores_str[j])

        # for example: change 1,234 into 1234
        if ',' in scores_str[j]:
            scores_str[j] = re.sub(r',', '', scores_str[j])

    # convert all list elements into interger
    scores_int = [int(i) for i in scores_str]
    # calculate the average reputation score
    avg_score = round(sum(scores_int) / len(scores_int))
    # calulate the top reputation score
    top_score = scores_int[np.argmax(scores_int)]

    # get the author's reputation score and remove tags
    author_score = soup3.select(".owner .reputation-score")
    author_score_str = re.sub(r'</?\w+[^>]*>','', str(author_score[0]))

    if '.' in author_score_str:
        author_score_str = re.sub(r'\.', '', author_score_str)
        author_score_str = re.sub(r'k', '00', author_score_str)

    if 'k' in author_score_str:
        author_score_str = re.sub(r'k', '000', author_score_str)

    if ',' in author_score_str:
        author_score_str = re.sub(r',', '', author_score_str)

    author_score_int = int(author_score_str)

    # put all 4 numbers into a result dictionary
    result_dict = {'Number of responses': len(responses),
                   'Average reputation score': avg_score,
                   'Top reputation score': top_score,
                   "Author's reputation score": author_score_int}
    return result_dict
