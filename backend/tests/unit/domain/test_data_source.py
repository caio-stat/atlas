from uuid import UUID

import pytest

from app.domain.entities.data_source import (
    DataSource,
    DataSourceStatus,
    DataSourceType,
)

from app.domain.errors import InvalidDataSourceError

def test_create_valid_data_source():
    data_source = DataSource.create(
        name="IBGE API",
        type="api",
        location="https://servicodados.ibge.gov.br/api/v1",
    )

    assert isinstance(data_source.id, UUID)
    assert data_source.name == "IBGE API"
    assert data_source.type == DataSourceType.API
    assert data_source.status == DataSourceStatus.ACTIVE
    assert data_source.location == "https://servicodados.ibge.gov.br/api/v1"

def test_create_data_source_with_enum_type():
    data_source = DataSource.create(
        name="Local CSV",
        type=DataSourceType.FILE,
        location="datasets/raw/source.csv",
    )

    assert data_source.type == DataSourceType.FILE

def test_create_data_source_strips_name_and_location():
    data_source = DataSource.create(
        name="  DATASUS  ",
        type="api",
        location="  https://datasus.saude.gov.br  ",
    )

    assert data_source.name == "DATASUS"
    assert data_source.location == "https://datasus.saude.gov.br"

def test_create_data_source_rejects_empty_name():
    with pytest.raises(InvalidDataSourceError, match="name cannot be empty"):
        DataSource.create(
            name="  ",
            type="api",
            location="https://example.com",
        )

def test_create_data_source_rejects_empty_location():
    with pytest.raises(InvalidDataSourceError, match="location cannot be empty"):
        DataSource.create(
            name="Example Source",
            type="api",
            location="  ",
        )

def test_create_data_source_rejects_invalid_type():
    with pytest.raises(InvalidDataSourceError, match="Invalid data source type"):
        DataSource.create(
            name="Invalid Source",
            type="spreadsheet",
            location="https://example.com",
        )

def test_create_data_sources_have_different_ids():
    first = DataSource.create(
        name="Source One",
        type="api",
        location="https://example.com/one",
    )
    second = DataSource.create(
        name="Source Two",
        type="api",
        location="https://example.com/two",
    )  
    assert first.id != second.id