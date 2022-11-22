## CLI app for cheking all available http methods  

***
CLI app which determine if strings are URL, and what http methods  available for this URL  

***How to start***  

```bash
git clone <project>
cd <project>
```

**If you use Poetry:**  
```bash
poetry install
# Run any of these files:
poetry run python cli/cli_asyncio.py
poetry run python cli/cli_threading.py
# CLI will activate
# For test from urls.txt file enter:
urls_test
# For test your strings or URLS input
<your string or URL> # Enter -> start -> Enter
# Available CLI commands:
# start, stop, urls_test
```
**If you use venv:**  
```bash
python -m venv venv
# Windows
. venv/scripts/activate 
# Linux
. venv/bin/activate
python -m pip install --upgrade pip
pip freeze -r for_venv/requirements.txt
# Run any of these files:
python cli/cli_asyncio.py
python cli/cli_threading.py
# CLI will activate
# For test from urls.txt file enter:
urls_test
# For test your strings or URLS input
<your string or URL> # Enter -> start -> Enter
# Available CLI commands:
start, stop, urls_test
```

Dev time ~ 15 hours  
percent_covered_display - 83%