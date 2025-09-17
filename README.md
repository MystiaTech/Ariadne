# Ariadne

Beginner-to-LLM educational chatbot project.

## Quick start (Python 3.10.6)

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

pip install -e ".[dev]"
pre-commit install

ariadne --name Dani
pytest
