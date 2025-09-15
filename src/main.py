from fastapi.openapi.docs import get_swagger_ui_html
import uvicorn
from fastapi import FastAPI

from src.api.application_payments import router as router_application_payments
from src.api.auth import router as router_auth
from src.api.manual_replenishments import router as router_manual_replenishments
from src.api.mov_funds import router as router_mov_funds
from src.api.positions_shipping_certificates import router as router_positions_shipping_certificates
from src.api.shipping_certificates import router as router_shipping_certificates
from src.api.topping_cashiers import router as router_topping_cashiers
from src.api.transfers_of_materials_btw_whs import router as router_transfers_of_materials_btw_whs


from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from contextlib import asynccontextmanager
from src.init import redis_manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await redis_manager.connect()
        FastAPICache.init(RedisBackend(redis_manager.redis), prefix="fastapi-cache")
        yield
    finally:
        await redis_manager.close()

app = FastAPI(docs_url=None, lifespan=lifespan)
app.include_router(router_application_payments, prefix="/applications", tags=["Applications"])
app.include_router(router_auth, prefix="/auth", tags=["Авторазиция и аутентефикация"])
app.include_router(router_manual_replenishments, prefix="/replenishments", tags=["Manual Replenishments"])
app.include_router(router_mov_funds, prefix="/transfers", tags=["Transfers"])
app.include_router(router_positions_shipping_certificates, prefix="/shipping-positions", tags=["Shipping Positions"])
app.include_router(router_shipping_certificates, prefix="/shipping-certificates", tags=["Shipping Certificates"])
app.include_router(router_topping_cashiers, prefix="/top-cashiers", tags=["Top cashiers"])
app.include_router(router_transfers_of_materials_btw_whs, prefix="/material-transfers", tags=["Material Transfers"])


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
