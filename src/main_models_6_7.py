import asyncio

from sqlalchemy import select

from core.db import engine, Base, AsyncSessionLocal
from models.model6 import Model6
from models.model7 import Model7


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as async_session:
        m6_1 = Model6(name="model 6 test 1")
        m6_1.sub_models.append(Model7(name="model 7 test 1"))
        m6_1.sub_models.append(Model7(name="model 7 test 2"))
        # Закомментированный код ниже работать не будет - поле только для чтения!
        # from models.model6 import Model6ToModel7
        # m2m = Model6ToModel7()
        # m2m.model7 = Model7(name="model 7 test 2")
        # m6_1.m2m_links.append(m2m)
        # async_session.add_all([m6_1, m2m])
        async_session.add_all([m6_1])
        await async_session.commit()
        r = await async_session.execute(select(Model6).where(Model6.id == 1))
        model6 = r.scalars().first()
        print("saved model 6: ", model6)
        for m2m_link in await model6.awaitable_attrs.m2m_links:
            print("\tsaved link for model 1: ", m2m_link, m2m_link.created_at)
        for sub_model in await model6.awaitable_attrs.sub_models:
            print("\tlinked model 7: ", sub_model)


if __name__ == "__main__":
    asyncio.run(main())
