import pytest
from SOresponse_Py import popular

def test_lenOfResponse():
    """
    This function tests if the question has any answer
    """
    with pytest.raises(TypeError):
        popular('https://stackoverflow.com/questions/49010465/override-class-for-plugin-in-elasticsearch', 'likes')

def test_resultOfLikes():
    """
    This function tests the output if choice equals likes
    """
    obs = popular('https://stackoverflow.com/questions/49218133/gulp-js-minifies-uglifies-and-copies-all-the-files-but-still-the-app-in-the-dis', 'likes')
    exp = '\nWhat do you mean by screwed up? Can you give an example of what is happening and what you would expect to happen.\n'
    assert obs == exp

def test_noAuthorAccepted():
    """
    This function tests if the question has author accepted answer
    """
    with pytest.raises(TypeError):
        popular('https://stackoverflow.com/questions/49218133/gulp-js-minifies-uglifies-and-copies-all-the-files-but-still-the-app-in-the-dis', 'author')

def test_resultOfAuthor():
    """
    This function tests the output if choice equals author
    """
    obs1 = popular('https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument', 'author')
    exp1 = '\nActually, this is not a design flaw, and it is not because of internals, or performance.\nIt comes simply from the fact that functions in Python are first-class objects, and not only a piece of code.\nAs soon as you get to think into this way, then it completely makes sense: a function is an object being evaluated on its definition; default parameters are kind of "member data" and therefore their state may change from one call to the other - exactly as in any other object.\nIn any case, Effbot has a very nice explanation of the reasons for this behavior in Default Parameter Values in Python.\nI found it very clear, and I really suggest reading it for a better knowledge of how function objects work.\n'
    assert obs1 == exp1

def test_inputOfChoice():
    """
    This function tests if the input of chice argument is likes or author
    """
    with pytest.raises(ValueError):
        popular('https://stackoverflow.com/questions/49218133/gulp-js-minifies-uglifies-and-copies-all-the-files-but-still-the-app-in-the-dis', 'lalala')
