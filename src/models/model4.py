from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Column, Table, DateTime, func
from sqlalchemy.orm import Mapped, relationship

from core.db import Base, CreatedModifiedMixin, CommonMixin

if TYPE_CHECKING:
    from models.model5 import Model5


m2m_link_table = Table(
    "m2m_link_table",
    Base.metadata,
    Column("model4_id", ForeignKey("model4.id"), primary_key=True),
    Column("model5_id", ForeignKey("model5.id"), primary_key=True),
    # непосредственного доступа к этому полю через модели нет
    Column("created_at", DateTime, server_default=func.now()),
)


class Model4(CommonMixin, CreatedModifiedMixin, Base):
    name: Mapped[str]
    # связь с Model5 через таблицу m2m_link_table
    # в модели сразу обращаемся к связанным записям через .sub_models
    sub_models: Mapped[list["Model5"]] = relationship(
        secondary=m2m_link_table, back_populates="sub_models", lazy="joined"
    )

    def __repr__(self):
        return f"{self.id=} {self.name=}"
