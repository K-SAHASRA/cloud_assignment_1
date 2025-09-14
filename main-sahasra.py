from fastapi import FastAPI
import uvicorn

from datetime import datetime
import socket
from typing import Optional
from fastapi import Query, Path

from models.courses_tracking import Coursework

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, I am sahasra, Welcome!"}


# budget tracking model



from models.budget_tracking import Budget_tracking
from models.budget_tracking import Budget_create
from models.budget_tracking import Budget_read
from models.budget_tracking import Budget_update

from typing import Dict
from uuid import UUID
budgets: Dict[UUID, Budget_read] = {}

def budget_tracker(echo: Optional[str], path_echo: Optional[str]=None) -> Budget_tracking:
    return Budget_tracking(
        budegt_month = "september",
        start_date = "2025-09-01",
        end_date = "2025-09-30",
        estimated_budget = "200$ " ,
        allowed_extension = "50$",
        money_saved = "100$"
)


@app.get("/budget_tracking", response_model=Budget_tracking)
def track_your_expenses(echo: str | None = Query(None, description="Optional echo string")):
    return budget_tracker(echo=echo, path_echo=None)

@app.post("/budget_tracking", response_model= Budget_read, status_code=201 )
def add_to_your_budget(budget :Budget_create ):
    if budget.id in budgets:
         raise HTTPException(status_code=400, detail="budget with this ID already exists")
    budgets[budget.id] = Budget_read(**budget.model_dump())

    return budgets[budget.id]

@app.get("/budget_tracking/{budget_id}", response_model=Budget_read)
def get_budget(budget_id: UUID):
    if budget_id not in budgets:
        raise HTTPException(status_code=404, detail="budget not found")
    return budgets[budget_id]


@app.patch("/budget_tracking/{budget_id}")
def update_budget(budget_id : UUID):
    return {"detail": "Not implemented"}, 501


@app.delete("/budget_tracking/{budget_id}")
def delete_budget(budget_id: UUID):
    raise HTTPException(status_code=501, detail=   "Not implemented yet")

@app.put("/budget_tracking/{budget_id}", response_model=Budget_read)
def update_budget(budget_id: UUID, budget: Budget_read):
    raise HTTPException( status_code=501, detail= "Not implemented yet")







#  course_Tracking model 




def coursework(echo: Optional[str], path_echo: Optional[str]=None) -> Coursework:
    return Coursework(
        course_name="Cloud Computing",
        course_code="COMSW4153",
        course_instructor="Donald Ferguson",
        course_timing="Monday 1:10pm to 3:40pm",
        requiremnt_satisfied="Systems requirement",
        goal_grade="A"
    )
@app.get("/courses_tracking", response_model=Coursework)
def track_your_courses(echo: str | None = Query(None, description="Optional echo string")):
    return coursework(echo=echo, path_echo=None)


@app.post("/courses_tracking", response_model=Coursework)
def create_course(course:    Coursework):
    raise HTTPException(status_code=501, detail ="Not implemented yet")

@app.get("/courses_tracking/{course_id}", response_model= Coursework)
def get_course(course_id: UUID):
    raise HTTPException(status_code= 501, detail=" Not implemented yet")

@app.put("/courses_tracking/{course_id}", response_model= Coursework)
def update_course(course_id: UUID, course: Coursework):
    raise HTTPException(status_code= 501, detail="Not implemented yet")

@app.delete("/courses_tracking/{course_id}")
def delete_course(course_id: UUID):
    raise HTTPException(status_code= 501, detail="Not implemented yet")








if __name__ == "__main__":
    uvicorn.run("main-sahasra:app", host="0.0.0.0", port=9000, reload=True)
