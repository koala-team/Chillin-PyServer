# -*- coding: utf-8 -*-

# python imports
from time import mktime
from datetime import datetime


def utcnowts():
    return mktime(datetime.utcnow().timetuple())


def strutcts(date_string, format):
    return mktime(datetime.strptime(date_string, format).timetuple())
