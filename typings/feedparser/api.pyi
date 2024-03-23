"""
This type stub file was generated by pyright.
"""

from .exceptions import *
from .sgml import *

PREFERRED_XML_PARSERS = ...
_XML_AVAILABLE = ...
SUPPORTED_VERSIONS = ...
LooseFeedParser = ...
StrictFeedParser = ...

def parse(
    url_file_stream_or_string,
    etag=...,
    modified=...,
    agent=...,
    referrer=...,
    handlers=...,
    request_headers=...,
    response_headers=...,
    resolve_relative_uris=...,
    sanitize_html=...,
):
    """Parse a feed from a URL, file, stream, or string.

    :param url_file_stream_or_string:
        File-like object, URL, file path, or string. Both byte and text strings
        are accepted. If necessary, encoding will be derived from the response
        headers or automatically detected.

        Note that strings may trigger network I/O or filesystem access
        depending on the value. Wrap an untrusted string in
        a :class:`io.StringIO` or :class:`io.BytesIO` to avoid this. Do not
        pass untrusted strings to this function.

        When a URL is not passed the feed location to use in relative URL
        resolution should be passed in the ``Content-Location`` response header
        (see ``response_headers`` below).

    :param str etag: HTTP ``ETag`` request header.
    :param modified: HTTP ``Last-Modified`` request header.
    :type modified: :class:`str`, :class:`time.struct_time` 9-tuple, or
        :class:`datetime.datetime`
    :param str agent: HTTP ``User-Agent`` request header, which defaults to
        the value of :data:`feedparser.USER_AGENT`.
    :param referrer: HTTP ``Referer`` [sic] request header.
    :param request_headers:
        A mapping of HTTP header name to HTTP header value to add to the
        request, overriding internally generated values.
    :type request_headers: :class:`dict` mapping :class:`str` to :class:`str`
    :param response_headers:
        A mapping of HTTP header name to HTTP header value. Multiple values may
        be joined with a comma. If a HTTP request was made, these headers
        override any matching headers in the response. Otherwise this specifies
        the entirety of the response headers.
    :type response_headers: :class:`dict` mapping :class:`str` to :class:`str`

    :param bool resolve_relative_uris:
        Should feedparser attempt to resolve relative URIs absolute ones within
        HTML content?  Defaults to the value of
        :data:`feedparser.RESOLVE_RELATIVE_URIS`, which is ``True``.
    :param bool sanitize_html:
        Should feedparser skip HTML sanitization? Only disable this if you know
        what you are doing!  Defaults to the value of
        :data:`feedparser.SANITIZE_HTML`, which is ``True``.

    :return: A :class:`FeedParserDict`.
    """
    ...
