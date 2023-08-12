import pytest


SCHOOL_INFO = {
    "name": "Pandas School",
    "location": "Santos",
    "fake info": "should not return",
}


@pytest.fixture
def mock_usecase(mocker):
    mock = mocker.patch("src.controllers.school_controller.CreateSchool")
    mock_obj = mock.return_value
    mock_obj.execute.return_value = SCHOOL_INFO

    return mock_obj


def test_create_school_return(client, mock_usecase):
    response = client.post("/backoffice/school/", json=SCHOOL_INFO)

    assert response.status_code == 201
    assert response.json == SCHOOL_INFO
