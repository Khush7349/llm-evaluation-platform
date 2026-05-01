import json
import re
DEFAULT = {"relevance": 0, "clarity": 0, "accuracy": 0}
def parse(text):
    if not text:
        return DEFAULT.copy()
    try:
        data = json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            return DEFAULT.copy()
        try:
            data = json.loads(match.group())
        except:
            return DEFAULT.copy()
    clean = {}
    for k in DEFAULT:
        v = data.get(k, 0)
        try:
            v = float(v)
        except:
            v = 0
        clean[k] = max(0, min(10, v))
    return clean
def average(scores):
    if not scores:
        return DEFAULT.copy()
    avg = {k: 0 for k in DEFAULT}
    n = len(scores)
    for s in scores:
        for k in avg:
            avg[k] += s.get(k, 0)
    return {k: round(v / n, 2) for k, v in avg.items()}