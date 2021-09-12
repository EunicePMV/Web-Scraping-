# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class QuotesDataclassesItem:
    txt : Optional[str] = field(default=None)
    author: Optional[str] = field(default=None)
    tags: Optional[str] = field(default=None)
