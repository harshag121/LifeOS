from pathlib import Path
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

MODEL_DIR = Path("data/models")
MODEL_DIR.mkdir(parents=True, exist_ok=True)
MODEL_PATH = MODEL_DIR / "tfidf.pkl"

class LocalNLP:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.corpus: List[str] = [
            "Time blocking improves focus",
            "Pomodoro helps with productivity",
            "Sleep correlates with recovery and performance",
            "Investments can compound over time",
            "Spaced repetition enhances retention"
        ]
        if MODEL_PATH.exists():
            try:
                with open(MODEL_PATH, "rb") as f:
                    self.vectorizer = pickle.load(f)
            except Exception:
                self._train_and_save()
        else:
            self._train_and_save()

    def _train_and_save(self):
        self.vectorizer.fit(self.corpus)
        with open(MODEL_PATH, "wb") as f:
            pickle.dump(self.vectorizer, f)

    def most_similar(self, text: str) -> str:
        v_corpus = self.vectorizer.transform(self.corpus)
        v_q = self.vectorizer.transform([text])
        sims = cosine_similarity(v_q, v_corpus)[0]
        idx = int(sims.argmax())
        return self.corpus[idx]

nlp = LocalNLP()
