# This file handles what the AI should NOT answer directly

def is_sensitive_topic(question):
    sensitive_keywords = [
        "suicide", "kill myself", "depression",
        "cure", "medicine", "legal advice",
        "crime", "hate", "violence","investment",
        "stock","crypto",
    ]

    for word in sensitive_keywords:
        if word in question:
            return True

    return False


def safe_response():
    return (
        "This is a sensitive topic. "
        "Rather than giving direct advice, "
        "it may help to reflect deeply or seek guidance from a trusted human."
    )
