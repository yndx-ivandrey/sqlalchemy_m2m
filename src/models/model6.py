from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base, CreatedModifiedMixin, CommonMixin

if TYPE_CHECKING:
    from models.model7 import Model7


class Model6(CommonMixin, CreatedModifiedMixin, Base):
    name: Mapped[str]
    # в модели сразу обращаемся к связанным записям через .sub_models
    sub_models: Mapped[list["Model7"]] = relationship(
        secondary="model6_to_model7", back_populates="sub_models"
    )
    # можем обратиться к записям связывающей таблицы,
    # но через поле m2m_links не можем создавать новые связи
    m2m_links: Mapped[list["Model6ToModel7"]] = relationship(
        back_populates="model6", viewonly=True
    )

    def __repr__(self):
        return f"{self.id=} {self.name=}"


class Model6ToModel7(CreatedModifiedMixin, Base):
    model6_id: Mapped[int] = mapped_column(ForeignKey("model6.id"), primary_key=True)
    model7_id: Mapped[int] = mapped_column(ForeignKey("model7.id"), primary_key=True)
    model6: Mapped["Model6"] = relationship(back_populates="m2m_links", viewonly=True)
    model7: Mapped["Model7"] = relationship(back_populates="m2m_links", viewonly=True)

    def __repr__(self):
        return f"{self.model6_id=} {self.model7_id=}"
