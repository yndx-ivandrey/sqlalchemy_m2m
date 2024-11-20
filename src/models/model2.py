from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.db import CreatedModifiedMixin, Base, CommonMixin

if TYPE_CHECKING:
    from models.model1 import Model1ToModel2


class Model2(CommonMixin, CreatedModifiedMixin, Base):
    name: Mapped[str]
    m2m_links: Mapped[list["Model1ToModel2"]] = relationship(
        back_populates="model2", lazy="joined"
    )

    def __repr__(self):
        return f"{self.id=} {self.name=}"
