# -*- coding: utf-8 -*-

# python imports
from datetime import datetime
from calendar import timegm
from time import time


def utcnowts():
    return time()


def strutcts(date_string, format):
    return timegm(datetime.strptime(date_string, format).utctimetuple())

