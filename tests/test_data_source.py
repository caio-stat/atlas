import pytest

from app.domain.entities.data_source import (
    DataSource,
    DataSourceStatus,
    DataSourceType,

 ) 
from app.domain.errors import InvalidDataSourceError

def test_create_data_source_with_valid_data():
    data_source = DataSource.create(
        name="IBGE API",
        source_type="api",
        location="https://servicodados.ibge.gov.br/api/v1",
    )

    assert data_source.name == "IBGE API"
    assert data_source.source_type == DataSourceType.API
    assert data_source.status == DataSourceStatus.ACTIVE
    assert data_source.location == "https://servicodados.ibge.gov.br/api/v1"

def test_create_data_source_strips_name_and_location():
    data_source = DataSource.create(
            name="  DATASUS  ",
            source_type="api",
            location="  https://datasus.saude.gov.br  ",
    )

    assert data_source.name == "DATASUS"
    assert data_source.location == "https://datasus.saude.gov.br"

def test_create_data_source_rejects_empty_name():
    with pytest.raises(InvalidDataSourceError):
        DataSource.create(
            name="",
            source_type="api",
            location="https://example.com",
        )

    