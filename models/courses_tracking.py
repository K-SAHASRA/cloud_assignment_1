from pydantic import BaseModel, Field
from typing import Optional

class Coursework(BaseModel):
    course_name : str = Field(description = "write the full course name")
    course_code : str = Field(description = " write the full course  code")
    course_instructor : str = Field(description = "write both the first and last names")
    course_timing : str = Field(description = "example: monday 2pm to 4pm")
    requiremnt_satisfied : str = Field(description= "specify the credit requiremnt it is satisfying")
    goal_grade : str = Field(description = "Specify the grade u intend to get in this course")

    model_config = {
        "json_schema_extra": {
            "example" : {
                "course_name" : "cloud computing",
                "course_code" : "COMSW4153",
                "course_instructor" : "Donald Ferguson",
                "course_timing" : "1.10 pm to 3.40 pm " ,
                "requiremnt_satisfied" : "systems requirement satisfied",
                "goal_grade" : "A"

            }
        }

    }

    
