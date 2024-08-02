from pathlib import Path
from pylexibank.providers import tob

from pylexibank.forms import FormSpec


class Dataset(tob.TOB):
    form_spec = FormSpec(
        brackets={"(": ")"},
        separators=";/,~",
        missing_data=("?", "-", ""),
        replacements=[(" #", "")],
        strip_inside_brackets=True,
    )

    dir = Path(__file__).parent
    id = "starostinkaren"
    pages = 10
    name = "krn"
    dset = "stb"
