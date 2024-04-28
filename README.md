# Terminal Website 
This project runs a server and that server is connected to you terminal and you can do things like sudo apt update and much more

# Installation

```
cd
sudo apt install python3
sudo apt install python3.11-venv
python3 -m venv venv
source venv/bin/activate
pip install Flask
pip install flask-socketio
sudo apt install git
git clone https://github.com/Momwhyareyouhere/Terminal-Website.git
cd Terminal-Website
python app.py
```

# Uninstall

```
cd
sudo rm -rf Terminal-Website
```

# Remove venv (optional):

```
cd
deactivate
sudo apt remove python3.11-venv
sudo rm -rf venv
```
