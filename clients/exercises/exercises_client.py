from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercises(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseResponseDict(TypedDict):
    exercise: Exercises


class GetExercisesQueryDict(TypedDict):
    """
        Описание структуры запроса на получение списка упражнений.
        """
    course_id: str


class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercises]


class CreateExercisesRequestDict(TypedDict):
    """
            Описание структуры запроса на создание списка упражнений.
            """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExercisesResponseDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """
            Описание структуры запроса на обновление списка упражнений.
            """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExercisesQueryDict(TypedDict):
    exersice_id: str


class UpdateExercisesResponseDict(TypedDict):
    exercise: Exercises


class ExercisesClient(APIClient):
    """
      Клиент для работы с /api/v1/exercises
      """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
                Метод получения списка упражнений.

                :param query: Словарь с userId.
                :return: Ответ от сервера в виде объекта httpx.Response
                """
        return self.get(f'/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f'/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления упражнения.
        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExercisesResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercises(self, exercise_id: str, request: UpdateExercisesRequestDict) -> UpdateExercisesResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))