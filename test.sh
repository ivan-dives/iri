#!/bin/sh

x=`python user_friendly_url.py "http://xn--80a1acny.xn--p1ai/resp_engine.aspx?Path=RP/INDEX/RU/Home/Search&keyword=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82"`

if [ "x$x" == "xпочта.рф/resp_engine.aspx?Path=RP/INDEX/RU/Home/Search&keyword=привет" ]; then
    echo OK
else
    echo FAIL
fi
