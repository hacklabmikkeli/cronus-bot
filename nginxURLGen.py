import os
from subprocess import call

def createConf(printer, token, ip):
    for file in os.scandir("/var/git/proxy-pass-octoprint/nginxConfig"):
        os.remove(file.path)

    myfile = "/var/git/proxy-pass-octoprint/nginxConfig/"+ printer +".dynamic.hacklabmikkeli.fi"
    config = 'server { listen 80; listen [::]:80; server_name ' + printer + '.dynamic.hacklabmikkeli.fi; location / { return 301 https://$server_name$request_uri; } } server { listen 443 ssl http2; listen [::]:443 ssl http2; ssl_certificate /etc/letsencrypt/live/hades.dynamic.hacklabmikkeli.fi/fullchain.pem; ssl_certificate_key /etc/letsencrypt/live/hades.dynamic.hacklabmikkeli.fi/privkey.pem; ssl_trusted_certificate /etc/letsencrypt/live/hades.dynamic.hacklabmikkeli.fi/chain.pem; include /etc/letsencrypt/options-ssl-nginx.conf; ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; add_header X-Frame-Options "SAMEORIGIN"; add_header Strict-Transport-Security "max-age=31536000; includeSubdomains; preload"; add_header X-XSS-Protection "1; mode=block"; add_header X-Content-Type-Options nosniff; add_header X-Robots-Tag none; add_header X-Download-Options noopen; add_header Access-Control-Allow-Origin *; add_header X-Permitted-Cross-Domain-Policies none; add_header Referrer-Policy no-referrer; server_name ' + printer + '.dynamic.hacklabmikkeli.fi; error_log /var/log/nginx/proxy-pass-octoprint/' + printer + '.error; access_log /var/log/nginx/proxy-pass-octoprint/' + printer + '.access; location /' + token + '/ { proxy_pass http://192.168.8.' + ip + '/; proxy_set_header Host $http_host; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade"; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Scheme $scheme; proxy_set_header X-Script-Name /' + token + '; proxy_http_version 1.1; client_max_body_size 0; } location /webcam/ { proxy_pass http://192.168.8.' + ip + '/webcam/; } }'
    with open(myfile, 'w'): pass
    with open(myfile, "r+") as p:
        data = p.read()
        p.seek(0)
        p.write(config)
        p.truncate()

    call(["/var/git/proxy-pass-octoprint/elevatePerm", "args", "to", "elevatePerm"])