from sqladmin import ModelView

from core.db.tables import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.first_name, User.last_name, User.username, User.is_admin, User.is_banned]
    can_create = False
    can_delete = False
    icon = "fa-solid fa-user"