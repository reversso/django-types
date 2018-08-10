from datetime import datetime
from sqlite3 import Connection
from sqlite3 import dbapi2 as Database
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, Union

from django.db.backends.base.base import BaseDatabaseWrapper

from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor


def decoder(conv_func: Callable) -> Callable: ...

class DatabaseWrapper(BaseDatabaseWrapper):
    alias: str
    allow_thread_sharing: bool
    autocommit: bool
    client: django.db.backends.sqlite3.client.DatabaseClient
    close_at: None
    closed_in_transaction: bool
    commit_on_exit: bool
    connection: None
    creation: django.db.backends.sqlite3.creation.DatabaseCreation
    errors_occurred: bool
    execute_wrappers: List[Any]
    features: django.db.backends.sqlite3.features.DatabaseFeatures
    force_debug_cursor: bool
    in_atomic_block: bool
    introspection: django.db.backends.sqlite3.introspection.DatabaseIntrospection
    needs_rollback: bool
    ops: django.db.backends.sqlite3.operations.DatabaseOperations
    queries_log: collections.deque
    run_commit_hooks_on_set_autocommit_on: bool
    run_on_commit: List[Any]
    savepoint_ids: List[Any]
    savepoint_state: int
    settings_dict: Dict[str, Optional[Union[Dict[str, None], int, str]]]
    validation: django.db.backends.base.validation.BaseDatabaseValidation
    vendor: str = ...
    display_name: str = ...
    data_types: Any = ...
    data_types_suffix: Any = ...
    operators: Any = ...
    pattern_esc: str = ...
    pattern_ops: Any = ...
    Database: Any = ...
    SchemaEditorClass: Any = ...
    client_class: Any = ...
    creation_class: Any = ...
    features_class: Any = ...
    introspection_class: Any = ...
    ops_class: Any = ...
    def get_connection_params(self) -> Dict[str, Union[int, str]]: ...
    def get_new_connection(
        self, conn_params: Dict[str, Union[int, str]]
    ) -> Connection: ...
    def init_connection_state(self) -> None: ...
    def create_cursor(self, name: None = ...) -> SQLiteCursorWrapper: ...
    def close(self) -> None: ...
    def disable_constraint_checking(self) -> bool: ...
    def enable_constraint_checking(self) -> None: ...
    def check_constraints(
        self, table_names: Optional[List[str]] = ...
    ) -> None: ...
    def is_usable(self): ...
    def is_in_memory_db(self) -> bool: ...

FORMAT_QMARK_REGEX: Any

class SQLiteCursorWrapper(Database.Cursor):
    def execute(
        self,
        query: str,
        params: Optional[
            Union[
                List[Optional[Union[float, str]]],
                List[Optional[Union[int, memoryview, str]]],
                List[datetime],
                Tuple,
            ]
        ] = ...,
    ) -> SQLiteCursorWrapper: ...
    def executemany(
        self, query: str, param_list: Union[Iterator[Any], List[Tuple[int]]]
    ) -> SQLiteCursorWrapper: ...
    def convert_query(self, query: str) -> str: ...
