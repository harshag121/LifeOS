import sys
from pathlib import Path

# Ensure project root is on sys.path so `import backend` works
ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
