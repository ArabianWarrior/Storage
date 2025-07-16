from src.connectors.redis_connectors import RedisManager
from src.config import settings

redis_manager = RedisManager(
    host=settings.RDS_HOST,
    port=settings.RDS_PORT,
)