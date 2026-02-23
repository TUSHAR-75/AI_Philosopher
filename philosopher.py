
# philosopher.py


def build_prompt(intent, question):
    """
    Builds a controlled philosophical prompt
    based on detected intent.
    """

    if intent == "existential":
        return f"Reflect deeply on the meaning of life and existence.\nQuestion: {question}\nThoughtful response:"

    elif intent == "emotional":
        return f"Respond calmly and thoughtfully to this emotional reflection.\nQuestion: {question}\nResponse:"

    elif intent == "philosophical":
        return f"Provide a wise philosophical reflection.\nQuestion: {question}\nReflection:"

    else:
        return f"Offer a thoughtful philosophical response to the following.\nQuestion: {question}\nResponse:"
#Before pretrained model 
def respond_by_intent(intent):
   
    if intent == "existential":
        return "Meaning often emerges from the choices we take responsibility for."
    elif intent == "emotional":
        return "It may help to observe what lies within your control and what does not."
    elif intent == "philosophical":
        return "What do you believe makes something true?"
    else:
        return "Your question invites reflection beyond clear categories."



# def socratic_response(question):
#     return "What do you believe lies at the heart of this question?"


# def stoic_response(question):
#     return "Some things are within our control, and others are not. Reflect on which this belongs to."


# def existential_response(question):
#     return "Meaning is not given to us; it is shaped by the choices we make."
