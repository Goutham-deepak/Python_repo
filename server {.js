server {
     listen 80;
     server_name iot.hyperthings.in:4050  www.iot.hyperthings.in:4050;
     return 301 https://iot.hyperthings.in:4050$request_uri;
}


server {
     listen 4050;
     listen 443 ssl;
     ssl on;
     ssl_certificate /home/staging/certs/ca_bundle-chint.crt;
     ssl_certificate_key /home/staging/certs/private.key;

     server_name iot.hyperthings.in:4050  www.iot2.hyperthings.in:4050;
     access_log /var/log/nginx/nginx.vhost.access.log;
     error_log /var/log/nginx/nginx.vhost.error.log;
     client_max_body_size 5M;
     location / {
         proxy_pass http://localhost:4050;
         proxy_redirect     off;
         proxy_set_header HOST $host;
         proxy_set_header Referer $http_referer;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
         proxy_set_header X-Forwarded-Port 443;
         proxy_set_header X-Forwarded-Proto https;
         proxy_connect_timeout 300;
         proxy_set_header Connection "";
         chunked_transfer_encoding off;
     }
}



server {
     listen 80;
     server_name iot.hyperthings.in:4051  www.iot.hyperthings.in:4051;
     return 301 https://iot.hyperthings.in:4051$request_uri;
}


server {
     listen 4051;
     listen 443 ssl;
     ssl on;
     ssl_certificate /home/staging/certs/ca_bundle-chint.crt;
     ssl_certificate_key /home/staging/certs/private.key;
     
     server_name iot.hyperthings.in:4051  www.iot.hyperthings.in:4051;
     access_log /var/log/nginx/nginx.vhost.access.log;
     error_log /var/log/nginx/nginx.vhost.error.log;
     client_max_body_size 5M;
     location / {
         proxy_pass http://localhost:4051;
         proxy_redirect     off;
         proxy_set_header HOST $host;
         proxy_set_header Referer $http_referer;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
         proxy_set_header X-Forwarded-Port 443;
         proxy_set_header X-Forwarded-Proto https;
         proxy_connect_timeout 300;
         proxy_set_header Connection "";
         chunked_transfer_encoding off;
     }
}

