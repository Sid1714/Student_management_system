def summarize_feedback(feedback_list):
    summary = {
        "total": len(feedback_list),
        "positive": sum("good" in f.lower() or "great" in f.lower() for f in feedback_list),
        "negative": sum("bad" in f.lower() or "poor" in f.lower() for f in feedback_list),
    }
    return summary

