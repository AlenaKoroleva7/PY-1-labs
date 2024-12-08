# TODO Напишите функцию для поиска индекса товара
def find_item_index(items, item_find):
    for index, current_item in enumerate(items):
        if current_item == item_find:
            return index
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find}' не найден в списке.")
