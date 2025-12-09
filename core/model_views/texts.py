from sqladmin import ModelView

from core.db.tables import TextItem


class TextAdmin(ModelView, model=TextItem):
    column_list = [TextItem.unique_name, TextItem.language_code, TextItem.content]
    can_delete = False
    icon = "fa-solid fa-text-height"