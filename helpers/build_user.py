from uuid import uuid4

from faker import Faker

fake = Faker("ru_RU")

class BuildUser:

    @staticmethod
    def build_user(*, email: str | None = None, password: str | None = None, name: str | None = None) -> dict:
        """Если не заполнить именованные аргументы, то поля заполнятся фейковыми данными"""

        return {
            # uuid вместе faker-а, т.к. при параллельном запуске может создаться один и тот же email
            "email": email if email else f"{uuid4().hex[:8]}@test.com",
            "password": password if password else fake.password(length=8, special_chars=False),
            "name": name if name else fake.first_name()
        }