# Multi-Tool Math Toolkit Agent

A compact Python agent that demonstrates natural-language math translation and factual lookups using LangChain tools and an LLM.

**Keywords**: math, natural-language, calculator, langchain, agent, llm, python, tools, wikipedia, math-translation, compute

**Features**
- **Natural Language Math**: Translate plain-English math queries into computed answers.
- **Factual Fetching**: Combine web or tool lookups (e.g., Wikipedia) with numeric computation.
- **Extensible Tools**: Designed so additional tools can be added to `tool_kit`.

**Prerequisites**
- **Python**: 3.10 or later recommended.
- **Dependencies**: Install from `requirement.txt`.

**Install**
```bash
python -m pip install -r requirement.txt
```

**Quick Start**
- Review the runner at [agents.py](agents.py).
- Run the example agent:
```bash
python agents.py
```
The script runs two short demos: a natural-language math translation and a Wikipedia-backed numeric example.

**Files of interest**
- [agents.py](agents.py) : main agent runner and demo flows.
- [tools.py](tools.py) : tool definitions included in the toolkit.
- [llm.py](llm.py) : LLM configuration used by the agent.
- [requirement.txt](requirement.txt) : dependency list for installation.

**Development**
- Add or adjust tools in `tool_kit` inside `tools.py` to extend capabilities.
- The project uses LangChain's agent APIs; refer to LangChain docs for adapter patterns.

**License & Contributing**
- Open for contributions: open a PR with a short description of changes.
- Include tests or examples for new tools or behaviors.
