import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# very simple dataset
texts = [
    "what is the meaning of life",
    "why do i feel afraid",
    "what is truth",
]
labels = [0, 1, 2]  # existential, emotional, philosophical

# simple word embedding model
class IntentModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(1000, 16)
        self.fc = nn.Linear(16, 3)

    def forward(self, x):
        x = self.embedding(x)
        x = x.mean(dim=1)
        return self.fc(x)
