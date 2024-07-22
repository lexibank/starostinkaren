from pathlib import Path
from pylexibank.providers import tob


class Dataset(tob.TOB):
    dir = Path(__file__).parent
    id = "starostinkaren"
    pages = 10
    name = "krn"
    dset = "stb"
