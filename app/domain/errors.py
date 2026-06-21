class DomainError(Exception):
    """Base error for Atlas domain rules."""

class InvalidDataSourceError(DomainError):
    """Raised when an invalid data source is provided."""
class DuplicateDataSourceError(DomainError):
    """Raised when trying to register a duplicated data source."""