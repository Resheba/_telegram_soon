from sqlalchemy import Result, select, Select, Insert

from .models import manager, User


class UserRepository:
    @staticmethod
    async def is_registred(id: int|str) -> bool:
        stmt: Select = select(User).where(User.id==id)
        async with manager.get_session() as session:
            res: Result = await session.execute(statement=stmt)
            row: User | None = res.scalar()
        return bool(row)
    
    @staticmethod
    async def register(id: int|str) -> None:
        stmt: Insert = manager[User].insert.values(id=id)
        await manager.execute(statement=stmt, commit=True)
            