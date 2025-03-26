from fastapi import APIRouter, HTTPException
from app.api.models.model import NumbersInput

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

router = APIRouter()

@router.post("/add")
def add_numbers(numbers: NumbersInput):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@router.post("/multiply")
def multiply_numbers(numbers: NumbersInput):
    result = numbers.num1 * numbers.num2
    return {"result": result}
# added in main@f4
