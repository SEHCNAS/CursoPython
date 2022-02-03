class HtmlToStringMixin:
    def __str__(self):
        # Conversao para html
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'

class Humano:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + '(pet)' if self.pet else ''

# Ordem das classes - HtmlToStringMixin > Humano
class HumanoHtml(HtmlToStringMixin, Humano):
    pass

class AnimalHtml(HtmlToStringMixin, Animal):
    pass

if __name__ == '__main__':
    p1 = Humano('Maria')
    print(p1)

    p2 = HumanoHtml('Roberto')
    print(p2)

    a1 = AnimalHtml('toto')
    print(a1)