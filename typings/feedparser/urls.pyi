"""
This type stub file was generated by pyright.
"""

from .html import _BaseHTMLProcessor

ACCEPTABLE_URI_SCHEMES = ...
_urifixer = ...

def convert_to_idn(url):  # -> Literal[b""]:
    """Convert a URL to IDN notation"""
    ...

def make_safe_absolute_uri(base, rel=...):  # -> str:
    ...

class RelativeURIResolver(_BaseHTMLProcessor):
    relative_uris = ...
    def __init__(self, baseuri, encoding, _type) -> None: ...
    def resolve_uri(self, uri):  # -> str:
        ...
    def unknown_starttag(self, tag, attrs):  # -> None:
        ...

def resolve_relative_uris(html_source, base_uri, encoding, type_):  # -> LiteralString:
    ...
