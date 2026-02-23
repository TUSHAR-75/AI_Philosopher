# This module handles ML/DL-based response generation

from transformers import pipeline

# load once (important for performance)
_generator = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=60
)


def generate_ai_response(prompt):
    """
    Generates a philosophical response using a pre-trained language model.
    This function is only responsible for language generation.
    """
    try:
        output = _generator(prompt)
        text = output[0]["generated_text"]

        # keep response short and clean
        return text[len(prompt):].strip()

    except Exception:
        return "Let us pause and reflect quietly."

