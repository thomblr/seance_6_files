import os

books = {
    '000-0000000000': {
        'authors': ('Author One', 'Author Two'),
        'pages': 362,
        'year': 2016
    },
    '978-2290094495': {
        'authors': 'Author Three',
        'pages': 12,
        'year': 1999
    },
    '123-9876543210': {
        'authors': ('Author Three', 'Author One'),
        'pages': 1563,
        'year': 2008
    }
}

authors = {
    'Author Three': ['978-2290094495', '123-9876543210'],
    'Author One': ['000-0000000000', '123-9876543210'],
    'Author Two': ['000-0000000000']
}

for author in authors:
    for book in authors[author]:
        if not os.path.exists('ex1'):
            os.mkdir('ex1')
        if not os.path.exists('ex1/' + author):
            os.mkdir('ex1/' + author)
        file_name = 'ex1/' + author + '/' + book + '.book'
        fh = open(file_name, 'w')
        fh.write(str(books[book]['pages']) + '\n')
        fh.write(str(books[book]['year']) + '\n')
        fh.close()
