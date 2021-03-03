# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из двух случайных слов, взятых из трёх списков:
import random


def get_jokes(n=4, flag=False):
    """ get_jokes(n, flag=True) Функция принимает количество n генерируемых шуток (по умолчанию 4), сформированных из
     случайных слов, взятых из трёх списков. flag=True - запрещает повтор слов в шутках """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    for i in range(n):
        joke_noun = random.choice(nouns)
        joke_adverb = random.choice(adverbs)
        joke_adjective = random.choice(adjectives)
        if flag:
            new_joke = joke_noun + ' ' + joke_adverb + ' ' + joke_adjective
            joke.append(new_joke)
            nouns.remove(joke_noun)
            adverbs.remove(joke_adverb)
            adjectives.remove(joke_adjective)
        else:
            new_joke = joke_noun + ' ' + joke_adverb + ' ' + joke_adjective
            joke.append(new_joke)

    return joke


print(get_jokes.__doc__)
print(get_jokes())
