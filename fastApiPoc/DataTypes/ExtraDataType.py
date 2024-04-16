from typing import Optional, Union
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
    item_id:UUID,
start_date:Optional[datetime]=Body(None),
end_date:Optional[datetime]=Body(None),
repeat_at:Optional[time]=Body(None),
process_after:Optional[timedelta]=Body( None)):



    start_process=start_date+process_after
    duration=end_date-start_date
    return {"item-id":item_id,"start_date":start_date,"end_date":end_date,
    "repeat_at":repeat_at,
    "process_after":process_after,
    "start_process":start_process,
    "process_after":process_after,
    "duration":duration
    }