# coding=utf-8
from __future__ import unicode_literals, print_function

from clldutils.path import Path
from pylexibank.providers import tob
from pylexibank.dataset import Metadata


class Dataset(tob.TOB):
    dir = Path(__file__).parent
    id = 'starostinkaren'
    pages = 1
    name = 'krn'
    dset = 'stb'
