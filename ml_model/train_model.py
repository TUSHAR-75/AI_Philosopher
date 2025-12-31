import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd

from intent_model import IntentModel

# ----------------------------
# Load dataset
# ----------------------------
data = pd.read_csv("dataset.csv")

texts = data["text"].tolist()
labels_text = data["intent"].tolist()

label_map = {
    "existential": 0,
    "emotional": 1,
    "philosophical": 2
}

labels = [label_map[l] for l in labels_text]

# ----------------------------
# Build vocabulary
# ----------------------------
vocab = {}
for text in texts:
    for word in text.split():
        if word not in vocab:
            vocab[word] = len(vocab) + 1

def encode(text, max_len=10):
    tokens = [vocab.get(w, 0) for w in text.split()]
    tokens = tokens[:max_len]
    tokens += [0] * (max_len - len(tokens))
    return tokens

X = torch.tensor([encode(t) for t in texts])
y = torch.tensor(labels)

# ----------------------------
# Model setup
# ----------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

model = IntentModel(
    vocab_size=len(vocab) + 1,
    embed_dim=16,
    num_classes=3
).to(device)

X = X.to(device)
y = y.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# ----------------------------
# Training loop
# ----------------------------
epochs = 30

for epoch in range(epochs):
    optimizer.zero_grad()

    outputs = model(X)
    loss = criterion(outputs, y)

    loss.backward()
    optimizer.step()

    if epoch % 5 == 0:
        print(f"Epoch {epoch} | Loss: {loss.item():.4f}")

# ----------------------------
# Save model
# ----------------------------
torch.save({
    "model": model.state_dict(),
    "vocab": vocab
}, "model.pth")

print("Model training complete and saved.")
