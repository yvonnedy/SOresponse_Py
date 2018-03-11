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

def test_noAuthotAccepted():
    """
    This function tests if the question has author accepted answer
    """
    with pytest.raises(TypeError):
        popular('https://stackoverflow.com/questions/49218133/gulp-js-minifies-uglifies-and-copies-all-the-files-but-still-the-app-in-the-dis', 'author')

def test_inputOfChoice():
    """
    This function tests if the input of chice argument is likes or author
    """
    with pytest.raises(ValueError):
        popular('https://stackoverflow.com/questions/49218133/gulp-js-minifies-uglifies-and-copies-all-the-files-but-still-the-app-in-the-dis', 'lalala')
