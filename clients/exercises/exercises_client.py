from typing import TypedDict

from clients.api_client import APIClient
from httpx import Response


class GetExercisesQueryDict(TypedDict):
    """
        Описание структуры запроса на получение списка упражнений.
        """
    course_id: str


class CreateExercisesRequest(TypedDict):
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


class UpdateExercisesRequest(TypedDict):
    """
            Описание структуры запроса на обновление списка упражнений.
            """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


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

    def create_exercise_api(self, request: CreateExercisesRequest) -> Response:
        """
        Метод создания упражнения.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f'/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequest) -> Response:
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
