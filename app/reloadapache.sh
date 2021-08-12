#!/usr/bin/tcsh    

set cuser = `/usr/bin/whoami`
# /sbin/apachectl status

echo "---> cycle 1 apache"
/sbin/apachectl stop
/sbin/apachectl start
/sbin/apachectl status

echo "---> cycle 2 apache"
/sbin/apachectl stop
/sbin/apachectl start
/sbin/apachectl status

echo "---> cycle 3 apache"
/sbin/apachectl stop
/sbin/apachectl start
/sbin/apachectl status

