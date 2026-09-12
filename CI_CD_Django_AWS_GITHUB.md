# CI-CD pipe line Django 

# STEP 1 : 
* Launch instance
* Update and install dependiencies

# STEP 2: 
* Install python for django
* Create new venv

# STEP 3: 
* Install Nginx or apache
* Install Gunicorn

# STEP 4: 
* Bind Gunicorn with WSGI.py of project


# STEP 5: 
* Add site info to ngnix (sites-avilable)
* Add site to sites-enabled

# Flow : 
* User -> Ngnix(80, 443)-> Gunicorn -> Django server


# STEP & CODE : 
* ssh -i your-key.pem ubuntu@your-ec2-public-ip
* sudo apt update && sudo apt upgrade -y
* sudo apt update && sudo apt upgrade -y
* sudo apt install python3-pip python3-dev python3-venv -y
* sudo apt install git -y
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
* python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
* pip install gunicorn
gunicorn --bind 0.0.0.0:8000 yourproject.wsgi
* sudo apt install nginx -y
* sudo nano /etc/nginx/sites-available/django_project
```js
server {
    listen 80;
    server_name YOUR_EC2_PUBLIC_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/YOUR_REPO;
    }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
    }
}

```
* sudo ln -s /etc/nginx/sites-available/django_project /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
* sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx
