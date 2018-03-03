def web_page(url):
    """
    Loads Stack Overflow response webpage.

    Input:
        url: Full URL to stack overflow response webpage. Character type.
    Output:
        q: The question being asked on the given Stack Overflow response webpage. Character type. If unsuccessful corresponding error will be returned.
    """


def popular(url, type):
    """
    Returns most popular response on webpage.

    Inputs:
        url: An object that used the `web_page()` function.
        type: "likes" returns response with the most likes. "author" returns response confirmed by author of question.
    Output:
        reponse: Returns a response. This will be of a character type.
    """


def response_stats(url):
    """
    Returns general statistics about question being asked on a Stack Overflow page.

    Input:
        url: An object that used the `web_page()` function.
    Output:
	Returns a list of length 4 that includes 
        n: Returns number of responses
        m: Average reputation score
        t: Top reputation score
        a: Author reputation score.
    """
