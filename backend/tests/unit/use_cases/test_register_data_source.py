import pytest

from app.domain.entities.data_source import DataSourceType
from app.domain.errors import DuplicateDataSourceError
from app.use_cases.register_data_source import (
    RegisterDataSource,
    RegisterDataSourceInput,
)

class FakeDataSourceRepository:
    def __init__(self) -> None:
        self.data_sources = {}
        self.saved_data_sources = None
    def exists_by_name(self, name: str) -> bool:
        return name in self.data_sources
    def save(self, data_source):
        self.data_sources[data_source.name] = data_source
        self.saved_data_sources = data_source
        return data_source
    

def test_register_data_source_successfully():
    repository = FakeDataSourceRepository()
    use_case = RegisterDataSource(repository)

    input_data = RegisterDataSourceInput(
        name="IBGE API",
        type="api",
        location="https://servicodados.ibge.gov.br/api/v1",
    )

    data_source = use_case.execute(input_data)

    assert data_source.name == "IBGE API"
    assert data_source.type == DataSourceType.API
    assert data_source.location == "https://servicodados.ibge.gov.br/api/v1"
    assert repository.saved_data_sources == data_source 
    assert repository.exists_by_name("IBGE API") 


def test_register_data_source_accepts_enum_type():
    repository = FakeDataSourceRepository()
    use_case = RegisterDataSource(repository)

    input_data = RegisterDataSourceInput(
        name="Local CSV",
        type=DataSourceType.FILE,
        location="datasets/raw/source.csv",
    )

    data_source = use_case.execute(input_data)

    assert data_source.type == DataSourceType.FILE


def test_register_data_source_rejects_duplicated_name():
    repository = FakeDataSourceRepository()
    use_case = RegisterDataSource(repository)

    input_data = RegisterDataSourceInput(
        name="DATASUS",
        type="api",
        location="https://datasus.saude.gov.br",
    )

    # First registration should succeed
    use_case.execute(input_data)

    # Second registration with the same name should raise an error
    with pytest.raises(DuplicateDataSourceError, match="Data source already exists"):
        use_case.execute(input_data)
    
def test_register_data_source_normalizes_name_before_saving():
    repository = FakeDataSourceRepository()
    use_case = RegisterDataSource(repository)

    input_data = RegisterDataSourceInput(
        name="  DATASUS  ",
        type="api",
        location="https://datasus.saude.gov.br",
    )

    data_source = use_case.execute(input_data)

    assert data_source.name == "DATASUS"
    assert data_source.location == "https://datasus.saude.gov.br"
    assert repository.exists_by_name("DATASUS")