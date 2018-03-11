# SOresponse_Py

### Contributors

* Ted Thompson (@TeddTech)
* Fang Yang (@fyang95)
* Ying Dong (@yvonnedy)      
     
### To install package
```
pip install git+https://github.com/UBC-MDS/SOresponse_Py.git
```

### Example of usage in Python
```
from SOresponse_Py.web_page import web_page
from SOresponse_Py.popular import popular
from SOresponse_Py.response_stats import response_stats

web_page('https://stackoverflow.com/questions/68645/static-class-variables-in-python?rq=1')
popular('https://stackoverflow.com/questions/49218133/gulp-js-minifies-uglifies-and-copies-all-the-files-but-still-the-app-in-the-dis', 'likes')
response_stats('https://stackoverflow.com/questions/49206233/how-can-i-convert-this-date-03-01-2018-1200-am-to-2018-03-01-in-c')
```

### To run tests   

1. Clone repo
2. Install pytest (`pip install -U pytest`)
3. Navigate to root directory of `SOresponse_Py` (this is the repo you just cloned) and run `pytest` 

### Overview

The `SOresponse` package is used for text analysis of Stack Overflow responses. There are both R and Python versions for this package. This package will include 3 functions: `web_page()` `popular()` `response_stats()`.

* `web_page(url)`: This function loads Stack Overflow response webpage and returns the title of question.

	*Argument:*

  `url` - A valid URL of a Stack Overflow webpage. Must be the type of String.

	*Value:*

  Returns the question being asked on the given Stack Overflow response webpage. If unsuccessful corresponding error will be returned.     
  
* `popular(url, choice)`: This function returns an answer with the most likes or a author accepted answer on specified webpage.

  *Arguments:*

    `url` - An object that used the `web_page()` function.

    `choice` - "likes" returns the response with the most likes; "author" returns the response accepted by the author.

  *Value:*

    Returns an answer on the webpage in the type of String.

* `response_stats(url)`: This function returns a list of statistics about the question being asked on a Stack Overflow page.

  *Argument:*

    `url` - An object that used the `web_page()` function.

  *Value:*

    Returns a list of length 4 that includes number of responses, average reputation score, top reputation score and author's reputation score.

Similar packages to `SOresponse` are `Py-StackExchange` for python and `overflowr` for R. `Py-StackExchange` is well managed and has been kept up to date. `overflowr` has been abandon. Their links respectively are https://github.com/lucjon/Py-StackExchange and https://meta.stackexchange.com/questions/174972/stackoverflow-api-for-r.
