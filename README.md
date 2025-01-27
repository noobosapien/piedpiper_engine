# Pied Piper Engine

An event driven AI-Agent engine to create robust intelligent applications.





[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![Python](https://img.shields.io/badge/python-3.9+-blue)
[![codecov](https://codecov.io/github/noobosapien/piedpiper_engine/graph/badge.svg?token=BLLPNB3L10)](https://codecov.io/github/noobosapien/piedpiper_engine)

## Installation

Install in a python3 environment

```bash
  pip install piedpiper_engine
```
    
## Running Tests

After cloning the repository, to run tests, run the following command

```bash
  pytest
```


## Usage/Examples
Creating an instance of the engine and running it as non-blocking
```python
from piedpiper_engine import Engine
from custom_modules import module
from custom_system import system
from custom_workflow import workflow

engine = Engine()

engine.add_module(module)
engine.add_system(system)

wf = engine.add_workflow(workflow)

engine.run_non_block()

# Use the workflow 
wf.add_message("Example message from client")
blocked_result = wf.get()

wf.add_message("Another message from client")
non_blocked_result = wf.get_non_block() # None returned if there is no result

engine.remove_workflow(wf)

engine.shutdown()
```


## Tech Stack

**App:** Python, Asyncio, Langchain

## Roadmap

- Build the core engine

## Feedback

If you have any feedback, please reach out to me at devdude@wondersplot.co.nz
