import pytest
from SOresponse_Py import response_stats

def test_result():
      """
      This function tests if the output list is correct.
      """
      obs1 = response_stats('https://stackoverflow.com/questions/49010465/override-class-for-plugin-in-elasticsearch')
      exp1 = [0, 1215, 2147, 283]
      assert obs1 == exp1

      obs2 = response_stats('https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python?rq=1')
      exp2 = [17, 35443, 317000, 317000]
      assert obs2 == exp2

      obs3 = response_stats('https://stackoverflow.com/questions/49206233/how-can-i-convert-this-date-03-01-2018-1200-am-to-2018-03-01-in-c')
      exp3 = [5, 66804, 529000, 1]
      assert obs3 == exp3

      obs4 = response_stats('https://stackoverflow.com/questions/49218523/highcharts-drilldown-json-from-php-mysql')
      exp4 = [0, 76, 76, 76]
      assert obs4 == exp4
