#!/usr/bin/env tcsh
######################
# reload apache 2
# kaloyansen@gmail.com

set cuser = `/usr/bin/whoami`
set retry = 3
set loop = 0
set apa = /sbin/apachectl
# /sbin/apachectl status

while ( $loop < $retry )
    @ loop++
    echo
    echo " user: $cuser ---> cycle $loop/$retry apache"
    echo " ==========================================="
    $apa stop
    $apa start
end

$apa status

