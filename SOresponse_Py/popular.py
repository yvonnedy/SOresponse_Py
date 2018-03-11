def popular(url, choice):
    """
    This function returns an answer with the most likes or a author accepted answer.
    on specified webpage.

    Inputs:
        url: An object that used the `web_page()` function.
        choice: "likes" returns the response with the most likes;
                "author" returns the response accepted by the author.
    Output:
        reponse: An answer on the webpage in the type of String.
    """

    from bs4 import BeautifulSoup
    import requests
    import re
    import numpy as np

    # load the webpage and select all responses
    web_data2 = requests.get(url)
    soup2 = BeautifulSoup(web_data2.text, "lxml")
    responses = soup2.select("#answers .post-text")

    # raise an error if the question has no response
    if len(responses) == 0:
        raise TypeError("This question has no answer!")

    else:
        if choice == 'likes':
            # select number of likes for each reponse
            likes = soup2.select("#answers .vote-count-post")
            likes_str = []
            # remove HTML tags for these number of likes
            for i in range(0, len(likes)):
                likes_str.append(re.sub(r'</?\w+[^>]*>','', str(likes[i])))
            # change the type into interger in the list
            likes_int = [int(i) for i in likes_str]

            # find the response with most likes
            response1 = responses[np.argmax(likes_int)]
            str_r1 = re.sub(r'</?\w+[^>]*>','', str(response1))
            return str_r1

        if choice == 'author':
            # select the author accepted answer
            response2 = soup2.select(".accepted-answer .post-text")
            if len(response2) == 0:
                # raise an error is there is no author accepted answer
                raise TypeError("There is no author accepted answer for this question!")
            else:
                str_r2 = re.sub(r'</?\w+[^>]*>','', str(response2[0]))
                return str_r2

        else:
            # raise an error is the input for choice is not valid
            raise ValueError("Input for choice can only be likes or author!")
