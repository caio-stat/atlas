import pytest

from app.domain.entities.data_source import DataSource
from app.domain.errors import DuplicateDataSourceError
from app.use_cases.register_data_source import (
    DataSourceRepository,
    RegisterDataSource,
    RegisterDataSourceInput,
)

class InMemoryDataSourceRepository:
    def __init__(self) -> None:
        self.items: list[DataSource] = []

    def exists_by_name(self, name: str) -> bool:
        normalized_name = name.strip().lower()
        return any(item.name.lower() == normalized_name for item in self.items)
    
    def save(self, data_source: DataSource) -> DataSource:
        self.items.append(data_source)
        return data_source
    

def test_register_data_source_successfully():
    repository = InMemoryDataSourceRepository()
    use_case = RegisterDataSource(repository)

    input_data = RegisterDataSourceInput(
        name="IBGE API",
        type="api",
        location="https://servicodados.ibge.gov.br/api/v1",
    )

    result = use_case.execute(input_data)

    assert result.name == "IBGE API"
    assert len(repository.items) == 1


def test_register_data_source_duplicate_name():
    repository = InMemoryDataSourceRepository()
    use_case = RegisterDataSource(repository)

    # Register a data source with a specific name
    input_data = RegisterDataSourceInput(
        name="IBGE API",
        type="api",
        location="https://servicodados.ibge.gov.br/api/v1",
    )
    use_case.execute(input_data)

    # Try to register another data source with the same name
    with pytest.raises(DuplicateDataSourceError):
        use_case.execute(input_data)
