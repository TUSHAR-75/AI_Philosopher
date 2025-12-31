def respond_by_intent(intent):
   
    if intent == "existential":
        return "Meaning often emerges from the choices we take responsibility for."
    elif intent == "emotional":
        return "It may help to observe what lies within your control and what does not."
    elif intent == "philosophical":
        return "What do you believe makes something true?"
    else:
        return "Your question invites reflection beyond clear categories."



def socratic_response(question):
    return "What do you believe lies at the heart of this question?"


def stoic_response(question):
    return "Some things are within our control, and others are not. Reflect on which this belongs to."


def existential_response(question):
    return "Meaning is not given to us; it is shaped by the choices we make."
