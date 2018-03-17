from distutils.core import setup

setup(
    name = 'SOresponse_Py',
    version = '0.2.0',
    author = 'Ted Thompson, Fang Yang, Ying Dong',
    packages = ['SOresponse_Py'],
    scripts = ['SOresponse_Py/web_page.py', 'SOresponse_Py/popular.py', 'SOresponse_Py/response_stats.py'],
    url = 'https://github.com/UBC-MDS/SOresponse_Py',
    license = 'LICENSE',
    description = 'Analysis of Stack Overflow responses',
    long_description = open('README.md').read(),
    install_requires = ['bs4', 'requests', 'numpy', 'lxml']
)
