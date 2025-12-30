def normalize_input(text):
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
        question = input("Ask a philosophical question: ")
        question = normalize_input(question)

        if question == "":
            print("Silence itself can be philosophical.")
        else:
            print(get_philosophical_response(question))

    except Exception:
        print("Even philosophers pause at uncertainty.")


main()
