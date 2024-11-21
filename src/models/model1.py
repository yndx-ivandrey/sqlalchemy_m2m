from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base, CreatedModifiedMixin, CommonMixin

if TYPE_CHECKING:
    from models.model2 import Model2


class Model1(CommonMixin, CreatedModifiedMixin, Base):
    name: Mapped[str]
    # Связь только через модель Model1ToModel2
    m2m_links: Mapped[list["Model1ToModel2"]] = relationship(back_populates="model1")

    def __repr__(self):
        return f"{self.id=} {self.name=}"


class Model1ToModel2(CreatedModifiedMixin, Base):
    model1_id: Mapped[int] = mapped_column(ForeignKey("model1.id"), primary_key=True)
    model2_id: Mapped[int] = mapped_column(ForeignKey("model2.id"), primary_key=True)
    model1: Mapped["Model1"] = relationship(back_populates="m2m_links")
    model2: Mapped["Model2"] = relationship(back_populates="m2m_links")

    def __repr__(self):
        return f"{self.model1_id=} {self.model2_id=}"
