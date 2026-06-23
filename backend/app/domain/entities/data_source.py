from dataclasses import dataclass
from enum import Enum
from uuid import UUID, uuid4

from app.domain.errors import InvalidDataSourceError

class DataSourceType(str,Enum):
    API = "api"
    WEBSITE = "website"
    FILE = "file"
    DATABASE = "database"
    MANUAL = "manual"

class DataSourceStatus(str,Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

@dataclass(frozen=True)
class DataSource:
    id: UUID
    name: str
    type: DataSourceType
    location: str
    status: DataSourceStatus = DataSourceStatus.ACTIVE

    @classmethod
    def create(
        cls,
        name: str,
        type: str | DataSourceType,
        location: str,
    ) -> "DataSource":
        normalized_name = name.strip()
        normalized_location = location.strip()

        if not normalized_name:
            raise InvalidDataSourceError("Data source name cannot be empty.")
        if not normalized_location:
            raise InvalidDataSourceError("Data source location cannot be empty.")
        
        try:
            normalized_type = DataSourceType(type)
        except ValueError as exc:
            valid_types = ",".join(item.value for item in DataSourceType)
            raise InvalidDataSourceError(
                f"Invalid data source type. Valid types are: {valid_types}"
                ) from exc
        
        return cls(
            id=uuid4(),
            name=normalized_name,
            type=normalized_type,
            location=normalized_location,
        )
