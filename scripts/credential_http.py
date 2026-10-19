"""Authenticated provider HTTP requests must never follow credential-bearing redirects."""
from urllib.request import HTTPRedirectHandler, build_opener


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def urlopen(request, *, timeout):
    # Keep the standard HTTPS certificate validation and environment proxy support.
    return build_opener(NoRedirect()).open(request, timeout=timeout)
