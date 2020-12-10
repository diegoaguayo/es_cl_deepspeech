Primero instalar python 3.6 con los siguientes comandos:

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

Luego instalar y crear un ambiente virtual:

apt-get update
apt-get install python3-virtualenv
virtualenv -p /usr/bin/python3.6 venv

Finalmente activar el ambiente con:

source ./venv/bin/activate


