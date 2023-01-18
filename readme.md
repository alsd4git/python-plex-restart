# Restart Plex

This is a python server using flask and basic auth to restart plex on a local machine (running windows) from an http request

## Requirements

- Python 3.x
- pip

requirements.txt generated with: (inside myEnv)

```python
pip freeze > requirements.txt
```

## Installation

1. Clone the project and navigate to the directory in your terminal.

2. Create a virtual environment and activate it:

```bash
python -m venv myEnv
source myEnv/bin/activate (Linux or MacOS)
myEnv\Scripts\activate (Windows)
```

3. Install the dependencies:

```pwsh
pip install -r requirements.txt
```

4. Run the server

python server.py
To exit the virtual environment use the command deactivate

## Usage

example request:

```pwsh
curl -u admin:password -X POST -H "Content-Type: application/json" -d '{"command": "start"}' http://{your_server_address}:{your_server_port}/
```
