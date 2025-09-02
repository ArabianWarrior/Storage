from fastapi import Query ,APIRouter
from fastapi_cache.decorator import cache


router = APIRouter(prefix="/products", tags=["Первый отдел"])


products = [
    {"id": 1, "title": "Солдатик", "name": "soldier"},
    {"id": 2, "title": "Мишка", "name": "bear"},
]


@router.get("")
@cache(expire=10)
async def get_products(
        id: int | None = Query(None, description="Айдишник"),
        title: str | None = Query(None, description="Название товара"),
):
    print("Иду в базу данных")
    products_ = []
    for product in products:
        if id and product["id"] != id:
            continue
        if title and product["title"] != title:
            continue
        products_.append(product)
    return products_
 


@router.delete("/{product_id}")
@cache(expire=10)
async def delete_product(product_id: int):
    global products
    products = [product for product in products if product["id"] != product_id]
    test_task.delay()
    return {"status": "OK"}