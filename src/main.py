import asyncio

from sqlalchemy import select

from core.db import engine, Base, AsyncSessionLocal
from models.model1 import Model1, Model1ToModel2
from models.model2 import Model2


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as async_session:
        m1_1 = Model1(name="model 1 test 1")
        m2_link_1 = Model1ToModel2()
        m2_link_1.model2 = Model2(name="model 2 test 1")
        m2_link_2 = Model1ToModel2()
        m2_link_2.model2 = Model2(name="model 2 test 2")
        m1_1.m2m_links.append(m2_link_1)
        m1_1.m2m_links.append(m2_link_2)
        async_session.add_all([m1_1, m2_link_1, m2_link_2])
        await async_session.commit()
        r = await async_session.execute(select(Model1).where(Model1.id == 1))
        model1 = r.scalars().first()
        print("saved model 1: ", model1)
        for m2m_link in model1.m2m_links:
            print("\tsaved link for model 1: ", m2m_link)
            print("\t\tlinked model 2: ", m2m_link.model2)


if __name__ == "__main__":
    asyncio.run(main())
