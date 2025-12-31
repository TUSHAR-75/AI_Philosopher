from guardrails import is_sensitive_topic, safe_response
from philosopher import respond_by_intent
from intent import detect_intent
from ml_model.predict import predict_intent


def main():
    print("Welcome to AI Philosopher")

    question = input("Ask a philosophical question: ").lower().strip()

    if question == "":
        print("Silence itself can be philosophical.")
        return

    if is_sensitive_topic(question):
        print(safe_response())
        return

    # Try ML model first
    intent = predict_intent(question)

    # Fallback to rules if ML is unsure
    if intent is None:
        intent = detect_intent(question)

    print(respond_by_intent(intent))


main()




#PREV STAGE
# from guardrails import is_sensitive_topic, safe_response
# from intent import detect_intent
# from ai_engine import generate_ai_response


# def main():
#     print("Welcome to AI Philosopher")

#     try:
#         question = input("Ask a philosophical question: ").lower().strip()

#         if question == "":
#             print("Silence itself can be philosophical.")
#             return

#         if is_sensitive_topic(question):
#             print(safe_response())
#             return

#         intent = detect_intent(question)

#         # ML/DL-based response (mock for now)
#         response = generate_ai_response(question)
#         print(response)

#     except Exception:
#         print("Even philosophers pause at uncertainty.")


# main()



# #   EARLY STAGE:
# # from intent import detect_intent
# # from philosopher import socratic_response, stoic_response, existential_response,respond_by_intent
# # from guardrails import is_sensitive_topic, safe_response

# # def choose_style(question):
# #     if "meaning" in question or "purpose" in question:
# #         return existential_response
# #     elif "control" in question or "fear" in question:
# #         return stoic_response
# #     else:
# #         return socratic_response


# # def normalize_input(text):
# #     # converting input to lowercase and removing extra spaces
# #     # helps in matching keywords properly
# #     return text.lower().strip()


# # def get_philosophical_response(question):
# #     responses = {
# #         "life": "Life is not discovered, it is created.",
# #         "death": "Death gives life its urgency.",
# #         "freedom": "Freedom demands responsibility.",
# #         "meaning": "Meaning arises from choice."
# #     }

# #     for key in responses:
# #         if key in question.split():
# #             return responses[key]

# #     return "Your question invites contemplation beyond simple answers."


# # def main():
# #     print("Welcome to AI Philosopher")

# #     try:
# #         question = input("Ask a philosophical question: ").lower().strip()

# #         if question == "":
# #             print("Silence itself can be philosophical.")
# #             return

# #         if is_sensitive_topic(question):
# #             print(safe_response())
# #             return

# #         intent = detect_intent(question)
# #         response = respond_by_intent(intent)
# #         print(response)

# #     except Exception:
# #         print("Even philosophers pause at uncertainty.")


# # main()








