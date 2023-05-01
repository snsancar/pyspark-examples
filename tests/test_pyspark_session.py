from pyspark.sql import SparkSession, DataFrame

import pytest


# Get one spark session for the whole test session
@pytest.fixture(scope="session")
def spark_session():
    return SparkSession.builder.getOrCreate()