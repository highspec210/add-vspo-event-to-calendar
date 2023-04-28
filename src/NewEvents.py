from CalendarManager import CalendarManager
from ItemListModel import ItemListModel
from ItemListScrapingManager import ItemListScrapingManager
from ItemModel import ItemModel
from ItemScrapingManager import ItemScrapingManager


def add_all_events(item_list: ItemListModel):
    for item in item_list.get_items():
        item_model: ItemModel = ItemScrapingManager.scrap_item(
            item.get("name"), item.get("url")
        )

        if item_model is None:
            continue

        if item_model.is_started():
            item_list.set_next_page("")
            break

        calendar_model = item_model.get_calendar_model()
        calendar_manager = CalendarManager()
        calendar_manager.add_event(calendar_model)


item_list: ItemListModel = ItemListScrapingManager.get_item_list()
add_all_events(item_list)
has_next = item_list.has_next_page()
while has_next:
    next_page = item_list.get_next_page()
    item_list = ItemListScrapingManager.get_item_list(next_page)
    add_all_events(item_list)
    has_next = item_list.has_next_page()
