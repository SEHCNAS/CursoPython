# <p class = "alert"><span>Curso de python 3, por </span>
#   <strong id="jf"> Juracy Filho</strong>
#   <span> e </span><strong id="ll">Leonardo Leitao</strong><span>.</span></p>

def Tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    atrs = ''.join(f'{K} = {W}' for K, W in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {atrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(
        Tag('p',
            Tag('span', 'Curso de python 3, por'),
            Tag('strong', 'Juracy Filho', id='jf'),
            Tag('span', 'e'),
            Tag('strong', 'Leonardo Leitao', id='ll'),
            Tag('span', '.'),
            html_class='alert')
    )
