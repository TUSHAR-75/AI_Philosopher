from flask import Flask, render_template, request
from guardrails import is_sensitive_topic, safe_response
from intent import detect_intent
from ml_model.predict import predict_intent
from philosopher import build_prompt
from ai_engine import generate_ai_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        question = request.form["question"].lower().strip()

        if question == "":
            response = "Silence itself can be philosophical."

        elif is_sensitive_topic(question):
            response = safe_response()

        else:
            intent = predict_intent(question)
            if intent is None:
                intent = detect_intent(question)

            prompt = build_prompt(intent, question)
            response = generate_ai_response(prompt)

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)