from unittest.mock import Mock
from src.usecases.school_usecase import CreateSchool


def test_create_school_usecase(mocker):
    mock_school_repo = mocker.Mock()
    mock_school_repo.create.return_value = "new_id"

    data = {"name": "Pandas School", "city": "Santos"}

    create_school = CreateSchool(mock_school_repo)
    result = create_school.execute(data)

    assert result == {"id": "new_id"}
    mock_school_repo.create.assert_called_once_with(data)
