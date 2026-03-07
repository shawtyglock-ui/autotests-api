import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import function_user, UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentification_user)

@pytest.fixture
def function_exercise(exercises_client: ExercisesClient,
                      function_course: CoursesClient
                      ) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.response.cours.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)