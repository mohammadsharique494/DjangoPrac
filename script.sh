# /bin/bash

sudo apt update
sudo apt upgrade -y

apt install python3
apt install python3-venv -y
python3 -m venv myenv
source myenv/bin/activate
pip3 i
