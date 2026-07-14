import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)


@pytest.fixture
def db():
    with engine.connect() as connection:
        yield connection
        connection.rollback()


def test_add_student(db):
    # Добавляем студента
    db.execute(text(
        "INSERT INTO student (user_id, subject_id, level, education_form) "
        "VALUES (9999, 9999, 'test_level', 'test_form')"
    ))
    db.commit()

    # Проверяем что студент добавлен
    result = db.execute(text(
        "SELECT * FROM student WHERE user_id = 9999 AND subject_id = 9999"
    )).fetchone()
    assert result is not None
    assert result.level == "test_level"

    # Удаляем после теста
    db.execute(text(
        "DELETE FROM student WHERE user_id = 9999 AND subject_id = 9999"
    ))
    db.commit()


def test_update_student(db):
    # Добавляем студента
    db.execute(text(
        "INSERT INTO student (user_id, subject_id, level, education_form) "
        "VALUES (9998, 9998, 'old_level', 'test_form')"
    ))
    db.commit()

    # Обновляем
    db.execute(text(
        "UPDATE student SET level = 'new_level' "
        "WHERE user_id = 9998 AND subject_id = 9998"
    ))
    db.commit()

    # Проверяем
    result = db.execute(text(
        "SELECT * FROM student WHERE user_id = 9998 AND subject_id = 9998"
    )).fetchone()
    assert result.level == "new_level"

    # Удаляем после теста
    db.execute(text(
        "DELETE FROM student WHERE user_id = 9998 AND subject_id = 9998"
    ))
    db.commit()


def test_delete_student(db):
    # Добавляем студента
    db.execute(text(
        "INSERT INTO student (user_id, subject_id, level, education_form) "
        "VALUES (9997, 9997, 'test_level', 'test_form')"
    ))
    db.commit()

    # Удаляем
    db.execute(text(
        "DELETE FROM student WHERE user_id = 9997 AND subject_id = 9997"
    ))
    db.commit()

    # Проверяем что удалён
    result = db.execute(text(
        "SELECT * FROM student WHERE user_id = 9997 AND subject_id = 9997"
    )).fetchone()
    assert result is None
