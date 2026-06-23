from dataclasses import dataclass
from typing import Protocol

from app.domain.entities.data_source import DataSource, DataSourceType
from app.domain.errors import DuplicateDataSourceError

class DataSourceRepository(Protocol):
    def exists_by_name(self, name: str) -> bool:
        ...

    def save(self, data_source: DataSource) -> DataSource:
        ...

@dataclass(frozen=True)
class RegisterDataSourceInput:
        name: str
        type: str | DataSourceType
        location: str

class RegisterDataSource:
        def __init__(self,repository: DataSourceRepository) -> None:
            self.repository = repository
        
        def execute(self, input_data: RegisterDataSourceInput) -> DataSource:
            if self.repository.exists_by_name(input_data.name):
                raise DuplicateDataSourceError(f"Data source already exists: {input_data.name}"
                )
            
            data_source = DataSource.create(
                name=input_data.name,
                type=input_data.type,
                location=input_data.location,
            )
            return self.repository.save(data_source)
