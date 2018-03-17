import pytest
from SOresponse_Py import web_page

def test_Url():
      """
      This function tests whether the input is a valid Stack Overflow webpage
      """
      good_url = 'https://stackoverflow.com/questions/68645/static-class-variables-in-python?rq=1'

      bad_url = 'https://google.com'

      # return no error
      web_page(good_url)

      # raise type error for invalid URL
      with pytest.raises(TypeError):
          # raise type error
          web_page(bad_url)

def test_resultOfWebpage():
      """
      This function tests the output of the funtion
      """
      url = 'https://stackoverflow.com/questions/68645/static-class-variables-in-python?rq=1'
      obs = web_page(url)
      exp = 'Static class variables in Python'
      # return an error if these two results are not equal
      assert obs == exp
