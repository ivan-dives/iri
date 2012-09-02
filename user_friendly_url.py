import sys
import urllib
import urlparse

cache = {}

def decode_iri_nocache(iri):
    iri = urllib.unquote_plus(iri)
    r = urlparse.urlsplit(iri)

    try:
        host = r.hostname.decode('idna').encode('utf8')
        iri = iri.replace(r.hostname, host, 1)
    except:
        pass

    return iri

def decode_iri(iri):
    c = cache.get(iri)
    if c is None:
        c = cache.setdefault(iri, decode_iri_nocache(iri))

if __name__ == "__main__":
    print decode_iri_nocache(sys.argv[1])

