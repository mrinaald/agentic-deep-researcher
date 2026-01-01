# Agentic Researcher

A minimal yet practical demonstration of Agentic AI with LLM tool use. This project wires a local LLM to a web search tool and implements a ReAct-style agent for deep research, showcasing structured tool invocation, reasoning traces, and final synthesis.

## Highlights

- Local LLM with deterministic tool use via zero temperature
- DuckDuckGo search tool integration
- ReAct agent graph that plans, calls tools, and synthesizes a final answer

## Architecture

- Core script: [search_agent.py](search_agent.py)
  - Agent class: [`DeepSearchReActAgent`](search_agent.py)
  - Model: `ChatOllama` bound to `llama3.1`
  - Tool: `DuckDuckGoSearchRun`
  - Agent creation: `create_agent(model, tools, debug)`
- Test script: [tests/agent_test.py](tests/agent_test.py)
  - Binds the search tool directly to the model with `bind_tools`
  - Invokes the model with a single user message and inspects `tool_calls`

Flow
1. User provides a research query.
2. The ReAct agent plans, optionally calls the search tool, and aggregates findings.
3. The final message in the agent graph is printed as the report.

## Requirements

- Ollama installed locally
- Python 3.12.x
- Dependencies in [requirements.txt](requirements.txt)

## Installation

1. Install Ollama and pull the model:
   ```sh
   ollama pull llama3.1
   ```

2. Create and activate a Python virtual environment.

3. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Quick test to verify environment and tool binding:
```sh
python tests/agent_test.py
```

Run the interactive ReAct agent:
```sh
python search_agent.py
```

This starts an interactive loop and prints a final synthesized report for each query.

## Rationale

- Using `temperature=0` biases the model toward consistent, tool-centric behavior.
- `bind_tools` ensures the model is aware of the available tool and how to call it.
- ReAct scaffolding captures intermediate reasoning and tool outputs before the final answer.

## Troubleshooting

- If the model does not call the tool, confirm that Ollama is running and `llama3.1` is available locally.
- Network issues can affect the DuckDuckGo tool; retry or verify connectivity.

## License

This is a personal learning project. Feel free to use and modify for educational purposes.

## Author

Mrinaal Dogra ([mrinaald](https://github.com/mrinaald))
