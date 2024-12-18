from datetime import datetime

AUTHOR = 'Bob King'
SITENAME = 'Ready-1'
SITEURL = 'wwww.getready1.com'

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

USE_FOLDER_AS_CATEGORY = True

STATIC_PATHS = ['pdfs', 'images', 'extras']
# ARTICLE_PATHS = ['articles']

DEFAULT_PAGINATION = 10

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "simple"
THEME = 'themes/pelican-bootstrap-5'
THEME__BOOTSWATCH = 'litera'

COPYRIGHT_YEAR = datetime.now().year