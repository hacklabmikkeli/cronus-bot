#!/bin/bash
mv /var/git/proxy-pass-octoprint/nginxConfig/* /etc/nginx/sites-available/
service nginx restart