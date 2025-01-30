from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    """
    parent_category_id: int|None - так и другие подкатегории
     (ожидается до 10 уровней вложенности подкатегорий)
    """
    category_id: int
    parent_category_id: Optional[int] = None

