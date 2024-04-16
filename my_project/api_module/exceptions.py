from fastapi import HTTPException, status

class AuthorNotFoundException(HTTPException):
    def __init__(self, user_id: int):
        detail = f"Author with id {user_id} not found"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)



class BookIdNotFoundException(HTTPException):
    def __init__(self, item_id: int):
        details = f"Book not found for id : {item_id}"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, details=details)
