import asyncio

from sqlalchemy import select

from core.db import engine, Base, AsyncSessionLocal
from models.model4 import Model4
from models.model5 import Model5


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as async_session:
        m4_1 = Model4(name="model 4 test 1")
        m4_1.sub_models.append(Model5(name="model 5 test 1"))
        m4_1.sub_models.append(Model5(name="model 5 test 2"))
        async_session.add_all([m4_1])
        await async_session.commit()
        r = await async_session.execute(select(Model4).where(Model4.id == 1))
        model4 = r.scalars().first()
        print("saved model 4: ", model4)
        for sub_model in model4.sub_models:
            print("\tlinked model 5: ", sub_model)


if __name__ == "__main__":
    asyncio.run(main())
