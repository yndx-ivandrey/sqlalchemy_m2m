from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.db import CreatedModifiedMixin, Base, CommonMixin

if TYPE_CHECKING:
    from models.model6 import Model6ToModel7, Model6


class Model7(CommonMixin, CreatedModifiedMixin, Base):
    name: Mapped[str]
    # в модели сразу обращаемся к связанным записям через .sub_models
    sub_models: Mapped[list["Model6"]] = relationship(
        secondary="model6_to_model7", back_populates="sub_models"
    )
    # можем обратиться к записям связывающей таблицы,
    # но через поле m2m_links не можем создавать новые связи
    m2m_links: Mapped[list["Model6ToModel7"]] = relationship(
        back_populates="model7", viewonly=True
    )

    def __repr__(self):
        return f"{self.id=} {self.name=}"
