# item-1-backend-v1

This is a flask web server that integrates the telegram bot with an llm. Different llms can be used based on environment variables.

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