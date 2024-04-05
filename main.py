import re

def count_words_sentences(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Використовуємо некаптурючу групу для розділових знаків речень
    sentence_pattern = r'[.!?]|(?:\.\.\.)'
    sentences = re.split(sentence_pattern, text)
    sentences = [s for s in sentences if s and s.strip()]  # Фільтруємо None і пусті строки

    # Регулярний вираз для знаходження слів
    word_pattern = r'[,\s:;]+'
    words = re.split(word_pattern, text)
    words = [w for w in words if w and w.strip()]  # Фільтруємо None і пусті строки

    return len(words), len(sentences)

