import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = "Kiev, Ukraine"
WEATHER_API_KEY = "815c91a1e5594b43ab9141844191812"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

