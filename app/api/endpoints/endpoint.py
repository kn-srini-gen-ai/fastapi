from fastapi import APIRouter, HTTPException
from app.api.models.model import NumbersInput

router = APIRouter()

@router.post("/add")
def add_numbers(numbers: NumbersInput):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@router.post("/multiply")
def multiply_numbers(numbers: NumbersInput):
    result = numbers.num1 * numbers.num2
    return {"result": result}