from sqladmin import ModelView

from core.db.tables import Currency


class CurrencyAdmin(ModelView, model=Currency):
    column_list = [Currency.name, Currency.symbol, Currency.rate, Currency.is_active]
    can_delete = False
    name_plural = "Currencies"
    icon = "fa-solid fa-dollar-sign"