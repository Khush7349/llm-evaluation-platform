from backend.evaluator import evaluate_full
def test_basic():
    res = evaluate_full(
        ["What is AI?"],
        ["Explain simply"]
    )
    assert "leaderboard" in res