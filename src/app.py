from CalendarManager import CalendarManager
from ItemListModel import ItemListModel
from ItemListScrapingManager import ItemListScrapingManager
from ItemModel import ItemModel
from ItemScrapingManager import ItemScrapingManager

item_list: ItemListModel = ItemListScrapingManager.get_item_list()
for item in item_list.get_items():
    item_model: ItemModel = ItemScrapingManager.scrap_item(
        item.get("name"), item.get("url")
    )

    if item_model is None:
        continue

    calendar_model = item_model.get_calendar_model()
    calendar_manager = CalendarManager()
    calendar_manager.add_event(calendar_model)
