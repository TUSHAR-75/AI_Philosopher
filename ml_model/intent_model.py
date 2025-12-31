import torch
import torch.nn as nn

class IntentModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_classes):
        super().__init__()

        # word embeddings
        self.embedding = nn.Embedding(vocab_size, embed_dim)

        # simple classifier
        self.fc = nn.Linear(embed_dim, num_classes)

    def forward(self, x):
        # x shape: (batch, sequence)
        x = self.embedding(x)
        x = x.mean(dim=1)  # average embeddings
        return self.fc(x)
