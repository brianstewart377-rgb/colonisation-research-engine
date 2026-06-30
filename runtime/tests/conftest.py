import sqlite3

import pytest

from runtime.build_runtime import build
from runtime.config import DEFAULT_EXPORTS_DIR
from runtime.projection import project


@pytest.fixture(scope="session")
def exports_dir():
    return DEFAULT_EXPORTS_DIR


@pytest.fixture(scope="session")
def projection_result(exports_dir):
    return project(exports_dir)


@pytest.fixture(scope="session")
def runtime_db(tmp_path_factory, exports_dir):
    out = tmp_path_factory.mktemp("runtime") / "cre_runtime.db"
    report = build(exports_dir, out, run_validation=True)
    return out, report


@pytest.fixture()
def conn(runtime_db):
    db_path, _ = runtime_db
    connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        yield connection
    finally:
        connection.close()
