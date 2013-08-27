# XXX: Decided to use urllib3 instead of python-requests as python-requests doesn't support the CONNECT method.
import urllib3

# XXX: Monkey patching for correcting a bug in httplib
import httplib

def _r(self, *args):
    return self._readline()

httplib.LineAndFileWrapper._readline = httplib.LineAndFileWrapper.readline
httplib.LineAndFileWrapper.readline = _r


STANDARD_HTTP_METHODS = ["GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "TRACE"]
# XXX: OPTIONS and TRACE are defined in HTTP/1.1, but usually refered to as WevDAV.
WEBDAV_METHODS = ["COPY", "MOVE", "LOCK", "MKCOL", "PROPFIND", "PROPPATCH", "UNLOCK", "PATCH"]
HTTP_METHODS = STANDARD_HTTP_METHODS + WEBDAV_METHODS

HTTP_SUCCESS_CODE = 200

# Argh... Too many arguments
def perform_request(url, proxy=None, method='GET', request_body_hack=False, verify_status=HTTP_SUCCESS_CODE, pool_manager=None, **kw):
    if pool_manager is None:
        http = create_pool_manager(proxy)
    else:
        http = pool_manager
    if request_body_hack:
        # This will enable us to send body as a buffer or as a file object. Otherwise, urllib3 will try to encode the body,
        # which is fine, but no what we want...
        http._encode_url_methods = set(HTTP_METHODS)
    response = http.request(method, url, **kw)
    if verify_status is not None:
        assert verify_status == response.status, "Expected status %d, received %d" % (verify_status, response.status)
    return response

def make_url(scheme, server, port=None, path=''):
    if port is None:
        port_string = ""
    else:
        port_string = ":%d" % (port, )
    return "%s://%s%s/%s" % (scheme, server, port_string, path)

def create_pool_manager(proxy=None, **kw):
    if proxy is not None:
        return urllib3.ProxyManager(proxy, **kw)
    return urllib3.PoolManager(**kw)
