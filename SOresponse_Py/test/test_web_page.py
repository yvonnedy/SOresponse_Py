import pytest
from SOresponse_Py import web_page

def test_typeOfUrl():
      """
      This function tests type of the input argument
      """
      good_url = 'https://stackoverflow.com/questions/68645/static-class-variables-in-python?rq=1'

      bad_url_string = 'fail'
      bad_url_type = 1231

      # return no error
      web_page(good_url)

      # raise type error for bad URL
      with pytest.raises(MissingSchema):
          # raise type error
          web_page(bad_url_string)

      # raise type error for int
      with pytest.raises(TypeError):
          # raise type error
          web_page(bad_url_type)

def test_resultOfWebpage():
      """
      This function tests the output of the funtion
      """
      url = 'https://stackoverflow.com/questions/68645/static-class-variables-in-python?rq=1'
      obs = web_page(url)
      exp = 'Static class variables in Python'
      # return an error if these two results are not equal
      assert obs == exp
