from alchemynger import AsyncManager

from config import Settings


manager: AsyncManager = AsyncManager(path=Settings.DB_DSN)
