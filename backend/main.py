from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import time
from backend.evaluator import evaluate_full
app = FastAPI(
    title="Elite LLM Evaluation Platform",
    version="1.0"
)
@app.get("/")
def root():
    return {"status": "API running"}
class EvalRequest(BaseModel):
    inputs: List[str] = Field(..., min_items=1, max_items=20)
    prompts: List[str] = Field(..., min_items=1, max_items=10)
@app.post("/evaluate")
def evaluate(req: EvalRequest):
    if not any(p.strip() for p in req.prompts):
        raise HTTPException(status_code=400, detail="Prompts cannot be empty")
    if not any(i.strip() for i in req.inputs):
        raise HTTPException(status_code=400, detail="Inputs cannot be empty")
    try:
        start = time.time()
        result = evaluate_full(req.inputs, req.prompts)
        duration = round(time.time() - start, 2)
        return {
            "status": "success",
            "time_taken": duration,
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))