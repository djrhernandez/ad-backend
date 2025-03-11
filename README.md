## Installation
1. Run these commands in your terminal. These will install the modules needed to run this application, in case you don't have them:
```bash
sudo apt install python3 python3-tk build-essential git -y
```

It's generally a good practice to update your kernel environment using the `update` and `upgrade` command from time to time. Run these for now:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt autoremove
```

2. Then, install the dependencies
```bash
pip install -r requirements.txt
```

3. Finally, run the project for backend development & debugging:
```bash
python main.py
```