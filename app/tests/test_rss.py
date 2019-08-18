import pytest

from unittest import mock

pytestmark = pytest.mark.django_db


def test_obj():
    assert 1 == 1
