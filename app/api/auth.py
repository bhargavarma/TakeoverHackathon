from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.models.user import User

from app.schemas.auth import (
    LoginRequest,
    LoginResponse,
    UserResponse,
)

from app.auth.security import (
    verify_password,
    hash_password,
)

from app.auth.token import (
    create_access_token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password.",
        )

    if not verify_password(
        request.password,
        user.password,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password.",
        )

    token = create_access_token(
        {
            "sub": str(user.id),
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@router.get(
    "/me",
    response_model=UserResponse,
)
def me(
    db: Session = Depends(get_db),
):

    user = db.query(User).first()

    return user


@router.post("/seed-owner")
def seed_owner(
    db: Session = Depends(get_db),
):

    owner = (
        db.query(User)
        .filter(User.email == "owner@aicoo.com")
        .first()
    )

    if owner:
        return {
            "message": "Owner already exists."
        }

    owner = User(
        full_name="Bhargav Varma",
        business_name="AI COO Demo",
        email="owner@aicoo.com",
        password=hash_password("admin123"),
    )

    db.add(owner)

    db.commit()

    return {
        "message": "Owner created."
    }

@router.delete("/delete-owner")
def delete_owner(
    db: Session = Depends(get_db),
):
    db.query(User).delete()
    db.commit()

    return {
        "message": "Owner deleted."
    }