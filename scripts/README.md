## User Guide - Interaction with Blockcain Part

you need to install web3.py in order to run python scripts

```shell
# Install pip if it is not available:
which pip || curl https://bootstrap.pypa.io/get-pip.py | python

# Install virtualenv if it is not available:
which virtualenv || pip install --upgrade virtualenv

# *If* the above command displays an error, you can try installing as root:
sudo pip install virtualenv

# Create a virtual environment:
virtualenv -p python3 ~/.venv-py3

# Activate your new virtual environment:
source ~/.venv-py3/bin/activate

# With virtualenv active, make sure you have the latest packaging tools
pip install --upgrade pip setuptools

# Now we can install web3.py...
pip install --upgrade web3
```
