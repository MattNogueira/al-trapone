import json
from pathlib import Path

LOCALES_DIR = Path(__file__).resolve().parent.parent / "locales"

TRANSLATIONS = {
    path.stem: json.loads(path.read_text(encoding="utf-8"))
    for path in LOCALES_DIR.glob("*.json")
}

def get_texts(locale: str) -> dict:
    return TRANSLATIONS.get(locale, TRANSLATIONS["pt-BR"])