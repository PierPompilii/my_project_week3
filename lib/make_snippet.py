
def make_snippet(words):
    text = words.split(" ")
    if len(text) <= 5:
        return text
    elif len(text) >= 6:
        dot_words = text[:5]
        snippet = " ".join(dot_words)
        return snippet + "..."