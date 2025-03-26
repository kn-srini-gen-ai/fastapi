from pydantic import BaseModel, validator

# Pydantic model for input validation
class NumbersInput(BaseModel):
    num1: float
    num2: float

    # Validator to ensure num2 is not zero for division (though not used here)
    @validator('num2')
    def check_num2(cls, value):
        if value == 0:
            raise ValueError("num2 cannot be zero for division operations")
        return value
    # added in feature/f2/main
<<<<<<< HEAD
    #added in feature/f3

=======
    # added in feature/f3/main
>>>>>>> origin
>>>>>>> 4ce29f6881983293be1405c622696073e3e89fe1
