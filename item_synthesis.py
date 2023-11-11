from item_synthesis_path import item_synthesis_path
def check_synthesis_item(ITEMS, item_bar):
    synthesizable_items = []
    current = ITEMS.head

    while current:
        item = current.data
        for item_name, components in item.items():
            required_components = list(components)
            is_synthesizable = True
            for component in required_components:
                if item_bar.count(component) < required_components.count(component):
                    is_synthesizable = False
                    break
            if is_synthesizable:
                synthesizable_items.append(item_name)
        current = current.next

    return synthesizable_items


def display_synthesizable_items(synthesizable_items):
    if synthesizable_items:
        #print("items:")
        for item_name in synthesizable_items:
            print(item_name)
    else:
        #print("No items")
        pass


item_bar = ['Lost_Chapter']
synthesizable_items = check_synthesis_item(item_synthesis_path, item_bar)
display_synthesizable_items(synthesizable_items)
