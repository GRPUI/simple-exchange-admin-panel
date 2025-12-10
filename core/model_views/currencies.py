from sqladmin import ModelView

from core.db.tables import Currency, CurrencyPair


class CurrencyAdmin(ModelView, model=Currency):
    column_list = [Currency.name, Currency.symbol, Currency.rate, Currency.is_active]
    can_delete = False
    name_plural = "Currencies"

    category = "Currency Management"
    category_icon = "fa-solid fa-dollar-sign"


class CurrencyPairsAdmin(ModelView, model=CurrencyPair):
    column_list = ["from_currency", "to_currency", "rate", "is_active"]
    column_labels = {
        "to_currency": "To Currency",
        "from_currency": "From Currency",
        "rate": "Rate",
        "is_active": "Active",
    }
    column_formatters = {
        "to_currency": lambda m, a: m.to_currency.name if m.to_currency else "Unknown",
        "from_currency": lambda m, a: (
            m.from_currency.name if m.from_currency else "Unknown"
        ),
    }

    column_details_list = ["from_currency", "to_currency", "rate", "is_active"]
    column_formatters_detail = {
        "to_currency": lambda m, a: m.to_currency.name if m.to_currency else "Unknown",
        "from_currency": lambda m, a: (
            m.from_currency.name if m.from_currency else "Unknown"
        ),
    }

    can_delete = False
    name_plural = "Currency Pairs"

    category = "Currency Management"
    category_icon = "fa-solid fa-dollar-sign"
