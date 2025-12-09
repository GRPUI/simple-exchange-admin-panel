import uvicorn
from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from config import DB_URL
from core.db.database_handler import DatabaseHandler
from core.model_views.currencies import CurrencyAdmin
from core.model_views.payment_categories import PaymentCategoryAdmin
from core.model_views.texts import TextAdmin
from core.model_views.users import UserAdmin

db = DatabaseHandler(DB_URL)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
admin = Admin(app, db.engine)


admin.add_view(UserAdmin)
admin.add_view(TextAdmin)
admin.add_view(CurrencyAdmin)
admin.add_view(PaymentCategoryAdmin)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
