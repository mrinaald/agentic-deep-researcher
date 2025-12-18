# agentic-deep-researcher

## Setup
Install `ollama`

Pull `llama3.1` model
```sh
# This pulls the 8B parameter model (approx 4.7GB).
ollama pull llama3.1
```

Setup python virtual environment and install python requirements:
```sh
pip install -r requirements.txt
```
For this, I used python `3.12.3` inside WSL2 Ubuntu.

Test ollama using:
```sh
python test_ollama.py
```

## Usage
Activate the python environment.

Test whether environment setup is working properly or not using:
```sh
python tests/agent_test.py
```

To run the agent:
```sh
python search_agent.py
```
