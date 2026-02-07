from pydantic import BaseModel, HttpUrl, Field, ConfigDict


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """
    Описание структуры запроса на создание файла.
    """
    file_name: str = Field(alias="filename")
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema
