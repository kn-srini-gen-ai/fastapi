from fastapi import FastAPI
from app.api.endpoints.endpoint import router as calculator_router
import uvicorn

app = FastAPI()

# Include API routers
app.include_router(calculator_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI calculator!"}


if __name__ == "__main__":
    
     uvicorn.run(app)

# added in main
# added in feature/f1
# added in feature/f2
#added in feature/f2/main
# added in feature/f3/main

# added new line in feature/f3
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, validator
# import uvicorn



# # Pydantic model for input validation
# class NumbersInput(BaseModel):
#     num1: float
#     num2: float

#     # Validator to ensure num2 is not zero for division (though not used here)
#     @validator('num2')
#     def check_num2(cls, value):
#         if value == 0:
#             raise ValueError("num2 cannot be zero for division operations")
#         return value
    
# app = FastAPI()

# # Endpoint to add two numbers
# @app.post("/add")
# async def add_numbers(numbers: NumbersInput):
#     result = numbers.num1 + numbers.num2
#     return {"result": result}

# # Endpoint to multiply two numbers
# @app.post("/multiply")
# async def multiply_numbers(numbers: NumbersInput):
#     result = numbers.num1 * numbers.num2
#     return {"result": result}

# # Root endpoint
# @app.get("/")
# async def root():
#     return {"message": "Welcome to the FastAPI calculator!"}


# if __name__ == "__main__":
    
#     uvicorn.run(app)
