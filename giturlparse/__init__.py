from .parser import parse as _parse
from .result import GitUrlParsed

__author__ = "Iacopo Spalletti"
__email__ = "i.spalletti@nephila.it"
__version__ = "0.12.0"


def parse(url, check_domain=True, platforms=None):
    return GitUrlParsed(_parse(url, check_domain, platforms))


def validate(url, check_domain=True, platforms=None):
    return parse(url, check_domain, platforms).valid
