def greet_user():
    print("Welcome to AI Philosopher")


def get_user_question():
    return input("Ask a philosophical question: ").strip()


def validate_question(question):
    if question == "":
        return "Silence can be philosophical. What would you like to explore?"
    elif len(question) < 5:
        return "A thought needs more depth. Could you elaborate?"
    elif any(word in question.lower() for word in ["2+2", "math", "weather", "price"]):
        return "That feels practical rather than philosophical. Let us reflect more deeply."
    else:
        return None


def philosopher_response(question):
    return "The philosopher reflects on: " + question


def main():
    greet_user()
    try:
        question = get_user_question()
        validation = validate_question(question)

        if validation:
            print(validation)
        else:
            print(philosopher_response(question))

    except Exception:
        print("Even philosophers face uncertainty. Please try again.")


main()
