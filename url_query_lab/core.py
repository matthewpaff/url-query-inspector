"""Inspect HTTP(S) URLs and decoded query values. Never makes a network request."""
import re
from urllib.parse import parse_qs, urlsplit


def inspect_url(url):
    if not isinstance(url, str) or not url or len(url) > 8192:
        raise ValueError("Supply a URL of 1–8192 characters")
    if any(char.isspace() or ord(char) < 32 or ord(char) == 127 for char in url) or "\\" in url:
        raise ValueError("Whitespace, control characters, and backslashes are not supported")
    try:
        parsed = urlsplit(url)
        port = parsed.port
        if parsed.scheme not in ("http", "https") or not parsed.hostname or port == 0:
            raise ValueError("Use an http:// or https:// URL")
        if parsed.username is not None or parsed.password is not None:
            raise ValueError("URLs containing credentials are not supported")
        if re.search(r"%(?![0-9A-Fa-f]{2})", parsed.query):
            raise ValueError("Query contains an invalid percent escape")
        query = parse_qs(parsed.query, keep_blank_values=True, max_num_fields=100, encoding="utf-8", errors="strict")
    except (ValueError, UnicodeError) as error:
        raise ValueError("Invalid URL: " + str(error)) from error
    return {"scheme": parsed.scheme, "host": parsed.hostname.lower(),
            "port": port or (443 if parsed.scheme == "https" else 80),
            "path": parsed.path or "/", "fragment": parsed.fragment,
            "query": dict(sorted(query.items()))}
