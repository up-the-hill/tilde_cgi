#!/bin/bash

first_half=$(sed -n "1,/print <<HTML_PAGE;/p" index.cgi)
echo "$first_half" >index.cgi
cat index.html >>index.cgi
echo "HTML_PAGE" >>index.cgi
cp index.cgi ~/tilde.club/public_html/index.cgi
cp style.css ~/tilde.club/public_html/style.css
cp add.cgi ~/tilde.club/public_html/add.cgi

echo "successfully uploaded!"
