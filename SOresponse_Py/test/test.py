import pytest
from SOresponse_Py import SO

url = 'https://stackoverflow.com/questions/68645/static-class-variables-in-python?rq=1'


class Test_web_page:    # test the `web_page()` function

    def test_typeOfUrl():
        """
        test type of the input argument
        """
        assert type(url) == str     # return an error if the type of url is not string

    def test_resultOfWebpage():
        """
        test the output of the funtion
        """
        obs = SO.web_page(url)
        exp = 'Static class variables in Python'
        assert obs == exp      # return an error if these two results are not equal


class Test_popular:    # test the `popular()` function

    def test_type():
        """
        test the content of the `type` arguemnt
        """
        with pytest.raises(TypeError):
            SO.popular(url, (type not in ('likes', 'author')))      # return an error if the type is neither likes nor author

    def test_resultOfPopular():
        """
        test the output of the funtion
        """
        obs = SO.popular(url, type = 'author')
        exp = """\r\nVariables declared inside the class definition, but not inside a method are class or static variables:\n\n>>> class MyClass:\n...     i = 3\n...\n>>> MyClass.i\n3 \n\n\nAs @millerdev points out, this creates a class-level i variable, but this is distinct from any instance-level i variable, so you could have\n\n>>> m = MyClass()\n>>> m.i = 4\n>>> MyClass.i, m.i\n>>> (3, 4)\n\n\nThis is different from C++ and Java, but not so different from C#, where a static member can't be accessed using a reference to an instance.\n\nSee what the Python tutorial has to say on the subject of classes and class objects.\n\n@Steve Johnson has already answered regarding static methods, also documented under \"Built-in Functions\" in the Python Library Reference.\n\nclass C:\n    @staticmethod\n    def f(arg1, arg2, ...): ...\n\n\n@beidy recommends classmethods over staticmethod, as the method then receives the class type as the first argument, but I'm still a little fuzzy on the advantages of this approach over staticmethod. If you are too, then it probably doesn't matter.\n”“”
        assert obs == exp       # return an error if these two results are not the same


class Test_response_stats:     # test the `response_stats()` function

    def test_resultOfStats():
        """
        test the output of the funtion
        """
        obs = SO.response_stats(url)
        exp = [16, 20295, 229000，18300]
        assert obs == exp      # return an error if the return list is not the same with our expected one
