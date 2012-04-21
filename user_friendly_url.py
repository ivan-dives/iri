
import urlparse, urllib, re

def user_friendly_url(url, __cache = {}):
    result = __cache.get(url)
    if result != None:
        return result

    url_with_proto = url
    if not re.match('^[a-zA-Z][a-zA-Z0-9.+-]*://', url):
        url_with_proto = 'http://' + url

    protocol, host, path, query, fragment = list(urlparse.urlsplit(url_with_proto))

    try: host = host.decode('idna').encode('UTF-8') #punycode to utf-8
    except: pass

    #decode urlencode to utf-8, if possible
    def urldecode(s):
        if '%' not in s:
            return s
        try: 
            def replace_if_url_safe_symbol(match):
                txt = match.group(0)
                c = chr(int(txt[1:], 16))
                if ord(c) >= 128 or c in ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"\'()*-.:<>[]^`{|}~''':
                    return c
                else:
                    return txt
            s2 = re.sub('%[0-9A-Fa-f]{2}', replace_if_url_safe_symbol, s)
            s2 = s2.decode('UTF-8').encode('UTF-8') #check, is valid UTF-8
            return s2
        except UnicodeError: 
            return s
    
    path = urldecode(path)
    query = urldecode(query)
    fragment = urldecode(fragment)
    
    result = host 
    if protocol and protocol.lower() != "http":
        result = protocol + "://" + result
    after_host = path
    if query:
        after_host += '?' + query
    if fragment:
        after_host += '#' + fragment
    if after_host != '/':
        result += after_host
        
    __cache[url] = result
    return result

if __name__ == "__main__":
    import sys
    print user_friendly_url(sys.argv[1])

