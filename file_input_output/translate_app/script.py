from translate import Translator

translator = Translator(to_lang="en")

def translate_large_text(text, chunk_size=500):
    chunks = []
    while len(text) > chunk_size:
        split_at = text.rfind(' ', 0, chunk_size)
        if split_at == -1:
            split_at = chunk_size
        chunks.append(text[:split_at])
        text = text[split_at:].strip()
    chunks.append(text)
    return ' '.join(translator.translate(chunk) for chunk in chunks)

with open("text.txt", "r") as file:
    translation = translate_large_text(file.read())
    print(translation)