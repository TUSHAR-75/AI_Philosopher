import torch
from .intent_model import IntentModel

LABELS = ["existential", "emotional", "philosophical"]
MAX_LEN = 10


def simple_tokenize(text, vocab):
    tokens = [vocab.get(word, 0) for word in text.split()]
    tokens = tokens[:MAX_LEN]
    tokens += [0] * (MAX_LEN - len(tokens))
    return torch.tensor(tokens).unsqueeze(0)


def predict_intent(text):
    try:
        checkpoint = torch.load("ml_model/model.pth", map_location="cpu",weights_only=True)
    

        vocab = checkpoint["vocab"]
        model_state = checkpoint["model"]

        model = IntentModel(
            vocab_size=len(vocab) + 1,
            embed_dim=16,
            num_classes=3
        )

        model.load_state_dict(model_state)
        model.eval()

        tokens = simple_tokenize(text, vocab)

        with torch.no_grad():
            output = model(tokens)
            probs = torch.softmax(output, dim=1)
            confidence, idx = torch.max(probs, dim=1)

        if confidence.item() < 0.6:
            return None  # fallback trigger

        return LABELS[idx.item()]

    except Exception:
        return None
