from feedback_summary import summarize_feedback

def test_feedback_summary():
    data = ["Great experience", "Poor service", "Good support", "Bad response"]
    result = summarize_feedback(data)
    assert result["total"] == 4
    assert result["positive"] == 2
    assert result["negative"] == 2