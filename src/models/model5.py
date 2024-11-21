from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.db import Base, CreatedModifiedMixin, CommonMixin

if TYPE_CHECKING:
    from models.model4 import Model4

    pass


class Model5(CommonMixin, CreatedModifiedMixin, Base):
    name: Mapped[str]
    # связь с Model4 через таблицу m2m_link_table
    # в модели сразу обращаемся к связанным записям через .sub_models
    sub_models: Mapped[list["Model4"]] = relationship(
        secondary="m2m_link_table", back_populates="sub_models", lazy="joined"
    )

    def __repr__(self):
        return f"{self.id=} {self.name=}"
