from src.feedback_entry import collect_feedback

def test_collect_feedback(monkeypatch):
    inputs = iter(["Great course!", "Needs improvement", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = collect_feedback()
    assert result == ["Great course!", "Needs improvement"]
