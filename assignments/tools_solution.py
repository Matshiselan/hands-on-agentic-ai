class TitleCaser:
    @staticmethod
    def enforce(text: str) -> str:
        """Return text in Title Case (basic heuristic; ignores small-word exceptions)."""
        if not text:
            return ""
        words = text.split()
        return " ".join(w.capitalize() for w in words)
