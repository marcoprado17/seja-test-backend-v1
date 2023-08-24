# item-1-backend-v1

This is a flask web server that integrates the telegram bot with an llm. Different llms can be used based on environment variables.

## TODO's

* Answer the telegram asynchronously.

## Setup on ubuntu server

Clone this repo:

```
cd ~;
git clone https://github.com/marcoprado17/seja-test-backend-v1.git;
```

Install python 3.11:

```
sudo apt update && sudo apt upgrade -y;
sudo apt install software-properties-common -y;
sudo add-apt-repository ppa:deadsnakes/ppa;
sudo apt install python3.11
```

Install pip:

```
cd ~;
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py;
sudo python3.11 get-pip.py;
```

Install the python packages:

```
cd ~/seja-test-backend-v1/item-1-backend-v1;
python3.11 -m pip install -r requirements.txt;
```

Create the .env:

Não se esqueça de atualizar o token do telegram.

```
cd ~/seja-test-backend-v1/item-1-backend-v1;
touch .env;
nano .env;
```

Test web server with gunicorn:

```
python3.11 -m gunicorn --bind 127.0.0.1:5000 app:app;
```

Create the service on systemd:

```
sudo nano /etc/systemd/system/app.service;
```

O conteúdo é o seguinte:

```
[Unit]
Description=Gunicorn daemon to serve my flaskapp
After=network.target
[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/seja-test-backend-v1/item-1-backend-v1
ExecStart=python3.11 -m gunicorn --bind 127.0.0.1:5000 app:app
[Install]
WantedBy=multi-user.target
```

```
sudo systemctl start app;
sudo systemctl enable app;
sudo systemctl status app;
```

Install nginx:

```
sudo apt-get install nginx;
```

Altere no nginx o server_name para a url do servidor e faça o proxy:

```
sudo nano /etc/nginx/sites-enabled/default;
```

Proxy:

```
proxy_pass http://127.0.0.1:5000;
```

Restart o nginx:

```
sudo systemctl restart nginx;
```

Gerar https:

[https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04)
