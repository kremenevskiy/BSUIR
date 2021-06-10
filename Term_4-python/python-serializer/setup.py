from setuptools import setup

setup(
    name="serializer",
    packages=[
        "serializer",
        "serializer/serializer",
        "serializer/parser",
        "serializer/parser/parsers",
        "serializer/parser/parsers/json",
        "serializer/parser/parsers/yaml",
        "serializer/parser/parsers/toml",
    ],
    version="1.0.0",
    author="kremenevskiy",
    scripts=["bin/serializer"]
)