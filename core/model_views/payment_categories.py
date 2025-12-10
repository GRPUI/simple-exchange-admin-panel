from sqladmin import ModelView

from core.db.tables import PaymentCategory


class PaymentCategoryAdmin(ModelView, model=PaymentCategory):
    column_list = [
        PaymentCategory.unique_name,
        PaymentCategory.name,
        PaymentCategory.language,
        PaymentCategory.is_active,
    ]
    name_plural = "Payment Categories"
    name = "Payment Category"
    icon = "fa-solid fa-list"
