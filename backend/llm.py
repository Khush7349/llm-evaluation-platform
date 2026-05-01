import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
def call(prompt, model=DEFAULT_MODEL, temperature=0.2, timeout=30, retries=2):
    for attempt in range(retries + 1):
        try:
            res = requests.post(
                OLLAMA_URL,
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": temperature}
                },
                timeout=timeout
            )
            res.raise_for_status()
            data = res.json()
            if "response" not in data:
                return "LLM Error: Invalid response format"
            return data["response"].strip()
        except requests.exceptions.Timeout:
            error = "LLM Error: Timeout"
        except requests.exceptions.ConnectionError:
            error = "LLM Error: Cannot connect to Ollama"
        except requests.exceptions.HTTPError:
            error = f"LLM Error: HTTP {res.status_code}"
        except Exception as e:
            error = f"LLM Error: {str(e)}"
        if attempt < retries:
            time.sleep(1)
        else:
            return error