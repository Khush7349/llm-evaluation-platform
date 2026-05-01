import hashlib
from backend.llm import call
from backend.scoring import parse, average
from backend.cache import get, set
from backend.logger import logger
FAIL_THRESHOLD = 15
def make_key(prompt, inp):
    raw = f"{prompt}-{inp}"
    return hashlib.md5(raw.encode()).hexdigest()
def judge(inp, out):
    prompt = f"""
You are an evaluator.
Return ONLY valid JSON:
{{"relevance": number, "clarity": number, "accuracy": number}}
Score each from 1-10.
Input:
{inp}
Output:
{out}
"""
    try:
        response = call(prompt)
        return parse(response)
    except Exception:
        return {"relevance": 0, "clarity": 0, "accuracy": 0}
def evaluate_full(inputs, prompts):
    results = {}
    for p in prompts:
        logger.info(f"Evaluating prompt: {p}")
        scores_all = []
        outputs = []
        for inp in inputs:
            key = make_key(p, inp)
            cached = get(key)
            if cached:
                out, score = cached
            else:
                try:
                    out = call(f"{p}\n\nInput:\n{inp}")
                    score = judge(inp, out)
                    set(key, (out, score))
                except Exception:
                    out = "Error generating output"
                    score = {"relevance": 0, "clarity": 0, "accuracy": 0}
            outputs.append(out)
            scores_all.append(score)
        avg = average(scores_all)
        failure_cases = [
            inp for inp, s in zip(inputs, scores_all)
            if sum(s.values()) < FAIL_THRESHOLD
        ]
        results[p] = {
            "average": avg,
            "failures": failure_cases,
            "sample_outputs": outputs[:2]
        }
    leaderboard = sorted(
        results.items(),
        key=lambda x: sum(x[1]["average"].values()),
        reverse=True
    )
    return {
        "leaderboard": leaderboard,
        "details": results
    }