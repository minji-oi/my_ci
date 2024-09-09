from my_validation.datamodel import User, UserDict
from pydantic import ValidationError

def main():
    # 테스트할 사용자 데이터를 정의합니다.
    users_data = [
        {"id": 1, "name": "Alice", "is_active": True},  # 유효한 데이터
        # {"id": None, "name": "Bob", "is_active": False},  # 유효하지 않은 ID
        # {"id": 3, "name": "", "is_active": True},  # 유효하지 않은 이름
        # {"id": -4, "name": "Charlie", "is_active": True},  # 유효하지 않은 음수 ID
        {"id": 4, "name": "David", "is_active": True},  # 유효한 데이터
    ]

    for user_data in users_data:
        try:
            # Pydantic 모델을 사용하여 유효성 검사를 수행합니다.
            user = User(**user_data)
            print(f"Valid user: {user}")
        except ValidationError as e:
            print(f"Validation error: {e}")

if __name__ == "__main__":
    main()