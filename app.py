print("Welcome to AI Philosopher")

try:
    question = input("Ask a philosophical question: ").strip()

    if question == "":
        print("Silence can be philosophical. What would you like to explore?")
    elif len(question) < 5:
        print("A thought needs more depth. Could you elaborate?")
    else:
        print("The philosopher reflects on:", question)

except Exception as e:
    print("Even philosophers face uncertainty. Please try again.")
