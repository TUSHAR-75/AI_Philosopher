from philosopher import socratic_response, stoic_response, existential_response


def choose_style(question):
    if "meaning" in question or "purpose" in question:
        return existential_response
    elif "control" in question or "fear" in question:
        return stoic_response
    else:
        return socratic_response


def normalize_input(text):
    # converting input to lowercase and removing extra spaces
    # helps in matching keywords properly
    return text.lower().strip()


def get_philosophical_response(question):
    responses = {
        "life": "Life is not discovered, it is created.",
        "death": "Death gives life its urgency.",
        "freedom": "Freedom demands responsibility.",
        "meaning": "Meaning arises from choice."
    }

    for key in responses:
        if key in question.split():
            return responses[key]

    return "Your question invites contemplation beyond simple answers."


def main():
    print("Welcome to AI Philosopher")

    try:
        question = input("Ask a philosophical question: ").lower().strip()

        if question == "":
            print("Silence itself can be philosophical.")
            return

        response_function = choose_style(question)
        print(response_function(question))

    except Exception:
        print("Even philosophers pause at uncertainty.")



main()
