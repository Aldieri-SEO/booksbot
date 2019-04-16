import csv, itertools

items = csv.DictReader(open('items.csv'))
for page, links in itertools.groupby(items, lambda item: item['prev_page']):
    if page:
        print('PAGE:', page)
        for line in links:
            print('     LINK TEXT:', line['prev_link_text'])
            print('     LINK URL:', line['prev_link_url'])
            print()
        print()