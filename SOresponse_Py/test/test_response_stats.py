import pytest
from SOresponse_Py import response_stats

def test_result():
      """
      This function tests if the output list is correct.
      """
      obs1 = response_stats('https://stackoverflow.com/questions/49010465/override-class-for-plugin-in-elasticsearch')
      exp1 = {"Author's reputation score": 283,
              'Average reputation score': 1220,
              'Number of responses': 0,
              'Top reputation score': 2157}
      assert obs1 == exp1

      obs2 = response_stats('https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python?rq=1')
      exp2 = {"Author's reputation score": 317000,
              'Average reputation score': 35527,
              'Number of responses': 17,
              'Top reputation score': 317000}
      assert obs2 == exp2

      obs3 = response_stats('https://stackoverflow.com/questions/49206233/how-can-i-convert-this-date-03-01-2018-1200-am-to-2018-03-01-in-c')
      exp3 = {"Author's reputation score": 1,
              'Average reputation score': 66997,
              'Number of responses': 5,
              'Top reputation score': 530000}
      assert obs3 == exp3

      obs4 = response_stats('https://stackoverflow.com/questions/49218523/highcharts-drilldown-json-from-php-mysql')
      exp4 = {"Author's reputation score": 76,
              'Average reputation score': 76,
              'Number of responses': 1,
              'Top reputation score': 76}
      assert obs4 == exp4
