server {
    # /etc/nginx/sites-available/app
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /usr/share/nginx/html;
    index index.html index.htm;

    client_max_body_size 4G;
    server_name _;

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

    location ~ /.well-known { 
        root /home/django/deploy/app/static;
        allow all;
    }

    # proxy the static assests for the django admin panel
    location /static/admin {
       alias /home/django/deploy/app/static/admin;
    }

    location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
            proxy_buffering off;

            proxy_pass http://unix:/home/django/gunicorn.socket;
    }

}
