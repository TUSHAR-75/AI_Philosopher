def detect_intent(question):
    if any(word in question for word in ["meaning", "purpose", "existence", "life"]):
        return "existential"

    elif any(word in question for word in ["fear", "anxiety", "happiness", "sad", "emotion"]):
        return "emotional"

    elif any(word in question for word in ["truth", "reality", "knowledge", "philosophy"]):
        return "philosophical"

    else:
        return "unknown"






# def detect_intent(question):
#     if any(word in question for word in ["meaning", "purpose", "existence"]):
#         return "existential"
#     elif any(word in question for word in ["fear", "anxiety", "control"]):
#         return "emotional"
#     elif any(word in question for word in ["truth", "reality", "knowledge"]):
#         return "philosophical"
#     else:
#         return "unknown"
