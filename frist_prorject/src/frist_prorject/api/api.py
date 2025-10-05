from fastapi import FastAPI
from pydantic import BaseModel
from frist_prorject.crew import FristProrject
from datetime import datetime
app = FastAPI()
class CrewInput(BaseModel):
    topic: str
    
class CrewOutput(BaseModel):
    report: str
    
@app.post("/run_crew", response_model=CrewOutput)
async def run_crew(request: CrewInput):
    inputs = {
'topic': request.topic,
-
        'current_year': str(datetime.now().year)
    }
    return CrewOutput(
        
        report=FristProrject().crew().kickoff(inputs=inputs).raw
    )
          