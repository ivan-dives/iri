#!/bin/sh

if [ "x$1" == "x-v" ]; then
    verbose=1
fi

_test() {
    x=`python user_friendly_url.py "$1"`

    if [ ! -z $verbose ]; then
        echo "sent:     $1"
        echo "expected: $2"
        echo "got:      $x"
    fi

    if [ "x$x" == "x$2" ]; then
        echo OK
    else
        echo FAIL
    fi
}

_test \
    "http://xn--80a1acny.xn--p1ai/resp_engine.aspx?Path=RP/INDEX/RU/Home/Search&keyword=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82" \
    "http://почта.рф/resp_engine.aspx?Path=RP/INDEX/RU/Home/Search&keyword=привет"

_test \
    "ftp://xn--80a1acny.xn--p1ai/" \
    "ftp://почта.рф/"

_test \
    "xn--80a1acny.xn--p1/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82" \
    "xn--80a1acny.xn--p1/привет"

_test \
    "http://xn--80a1acny.xn--p1ai/?keyword=xn--80a1acny.xn--p1ai" \
    "http://почта.рф/?keyword=xn--80a1acny.xn--p1ai"
