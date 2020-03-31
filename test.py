# coding: utf-8
from __future__ import unicode_literals


def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_forms(cldf_dataset, cldf_logger):
    assert len(list(cldf_dataset["FormTable"])) == 169


def test_languages(cldf_dataset, cldf_logger):
    assert len(list(cldf_dataset["LanguageTable"])) == 10


def test_sources(cldf_dataset, cldf_logger):
    assert len(cldf_dataset.sources) == 1


def test_parameters(cldf_dataset, cldf_logger):
    assert len(list(cldf_dataset["ParameterTable"])) == 18


def test_cognates(cldf_dataset, cldf_logger):
    cogsets = {c["Cognateset_ID"] for c in cldf_dataset["CognateTable"]}
    assert len(cogsets) == 7
