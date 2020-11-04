from datetime import datetime, date
from typing import List
from pydantic import BaseModel


class CrossCheckReport(BaseModel):
    start_datetime: date
    end_datetime: date
    merchants: List = [str]
