from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class Budget_tracking(BaseModel):
    budegt_month : str = Field(description = "write the name of the month")
    start_date : date = Field(description = " write the date")
    end_date : date = Field(description = " write the date")
    estimated_budget : str = Field(description = "example: 300$")
    allowed_extension : str = Field(description= "example: an additional margin of 30 dollars")
    money_saved : str = Field(description = "Specify the amount")

    model_config = {
        "json_schema_extra": {
            "example" : {
                "budegt_month" : "september",
                "start_date" : "2025-09-01",
                "end_date" : "2025-09-30",
                "estimated_budget" : "200$ " ,
                "allowed_extension" : "50$",
                "money_saved" : "100$"

            }
        }

    }

# now for create
from uuid import UUID, uuid4
class Budget_create(Budget_tracking):
    id: UUID = Field(default_factory= uuid4, description = "Unique ID")



# now fpr update
class Budget_update(BaseModel):
    budegt_month : Optional[str] = Field(description = "write the name of the month")
    start_date : Optional[date] = Field(description = " write the date")
    end_date : Optional[date] = Field(description = " write the date")
    estimated_budget : Optional[str] = Field(description = "example: 300$")
    allowed_extension : Optional[str] = Field(description= "example: an additional margin of 30 dollars")
    money_saved : Optional[str] = Field(description = "Specify the amount")


# now for read
class Budget_read(Budget_tracking):
    id: UUID
    created_time: datetime = Field(default_factory = datetime.utcnow)
    updated_time: datetime = Field (default_factory=  datetime.utcnow)