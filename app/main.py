from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
app=FastAPI(title="Healthcare Appointments API",version="0.1.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])
class Appointment(BaseModel):
    patient: str = Field(min_length=2,max_length=120)
    scheduled_for: str = Field(min_length=1,max_length=120)
records=[]
@app.get("/health")
def health(): return {"status":"ok","service":"healthcare-appointment-management-system"}
@app.get("/api/appointments")
def list_records(): return records
@app.post("/api/appointments",status_code=201)
def create_record(record:Appointment): records.append(record.model_dump()); return record
