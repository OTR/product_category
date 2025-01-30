from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    """

    """
    category_id: int
    parent_category_id: Optional[int] = None
    
