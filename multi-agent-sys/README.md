## Dependency setup (CrewAI, CrewAI Tools, LangChain IBM)

### Why you may see install/backtracking errors
- **crewai-tools** recently started depending on a newer **embedchain (0.1.x)** line. On some systems (or Python versions), pip can’t resolve a set of packages that satisfy all constraints.
- When that happens, **pip backtracks** (tries many version combinations). If none works for your Python version, it ends in an error.
- Python 3.11 is the most reliable target for the versions below. Using 3.12/3.13 can trigger resolver loops or incompatible wheels.

### Prerequisite: ensure Python 3.11 is available
You can use pyenv, Homebrew, or conda. Examples (macOS):

```bash
# Verify if you already have it
python3.11 -V

# Example with Homebrew
brew install python@3.11
```

### Create a clean virtual environment (Python 3.11)
```bash
python3.11 -m venv .venv311
source .venv311/bin/activate
```

### Upgrade base tooling
```bash
pip install -U pip setuptools wheel
```

### Install a compatible, working set (avoids embedchain>=0.1.x)
Pinned versions known to work well together:
```bash
pip install \
  "crewai==0.165.1" \
  "crewai-tools==0.60.0" \
  "chromadb==0.5.23" \
  "tiktoken==0.8.0" \
  "litellm==1.74.9" \
  "langchain-ibm==0.3.15"
```

Notes:
- `langchain-ibm` pulls `ibm-watsonx-ai` automatically. If you need a pin: `ibm-watsonx-ai==1.3.34`.
- If you still see resolver loops, double‑check you’re inside the Python 3.11 venv.

### Verify imports (quick check)
```bash
python - <<'PY'
import importlib
mods = ['crewai','crewai.tools','crewai_tools','langchain_ibm']
for m in mods:
    importlib.import_module(m)
print('OK: imports look good')
PY
```

### Correct import names you’ll likely need
- CrewAI core:
  ```python
  from crewai import Agent, Task, Crew
  ```
- CrewAI tools (Serper, DuckDuckGo, Scraper), as exported by `crewai-tools`:
  ```python
  from crewai_tools import SerperDevTool, DuckDuckGoSearchTool, ScrapeWebsiteTool
  ```
- LangChain IBM LLM:
  ```python
  from langchain_ibm import WatsonxLLM  # note the lowercase "x" in Watsonx
  ```

### Environment variables (examples)
```bash
export WATSONX_API_KEY="your-api-key"
export SERPER_API_KEY="your-api-key"
```

### Common issues
- Using Python 3.12/3.13: may cause pip backtracking with no solution. Use Python 3.11.
- Wrong import casing for `WatsonxLLM` (people often try `WatsonXLLM`). Use `WatsonxLLM`.
- Mixed global/site packages with venv: ensure your shell shows the `.venv311` is active.


