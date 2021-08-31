server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name kalodev.site www.kalodev.site;
    return 301 https://$server_name$request_uri;
}

server {

    # SSL configuration
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;

    include snippets/ssl-www.kalodev.site.conf;
    include snippets/ssl-params.conf;

    access_log /var/log/nginx/kalodev_access.log combined;
    error_log /var/log/nginx/kalodev_error.log error;

    root /usr/share/nginx/html;
    index index.html index.htm;

    client_max_body_size 4G;

    keepalive_timeout 5;

    location /favicon.ico  {
        alias /home/django/deploy/app/static/ico/favicon.ico;
    }

    # django project media files
    location /media  {
        alias /home/django/deploy/app/media;
    }

    # django project static files
    location /static {
        alias /home/django/deploy/app/static;
    }

    # proxy the static assests for the django admin panel
    location /static/admin {
        alias /home/django/deploy/app/static/admin;
    }

    location /robots.txt {
        alias /home/django/deploy/app/static/robots.txt;
    }

    location /cv {
        alias /home/django/deploy/app/static/pdf/back-end.pdf;
    }

    location ~ /pdf {
        root /home/django/deploy/app/static;
        allow all;
    }

    location ~ /img {
        root /home/django/deploy/app/static;
        allow all;
    }

    location ~ /.well-known { 
        root /home/django/deploy/app/static;
        allow all;
    }

    location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
            proxy_buffering off;
            proxy_pass http://unix:/home/django/gunicorn.socket;
    }

}
