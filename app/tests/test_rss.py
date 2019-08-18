import pytest

from unittest import mock

from flask import Flask

from app import RssResponse
from app.rss import RssPodcast
from . import rss_fixtures

pytestmark = pytest.mark.app_db


@pytest.mark.parametrize('input_params, expected_params', [
    (rss_fixtures.rv_xml, 'application/xml'),
    (rss_fixtures.rv_html, 'text/html'),
])
def test_rss_resp(input_params, expected_params):
    flask = Flask(__name__)
    flask.response_class = RssResponse
    resp = flask.make_response(rv=input_params)
    assert resp.status_code == 200
    assert resp.mimetype == expected_params


@pytest.mark.parametrize('input_params', [12345])
def test_rss_res_negative(input_params):
    flask = Flask(__name__)
    flask.response_class = RssResponse
    with pytest.raises(TypeError):
        flask.make_response(rv=input_params)


def test_rss_podcast_init():
    with mock.patch('pathlib.Path.exists', side_effect=lambda: True):
        p = RssPodcast()
        assert p.name == 'Eriwan_Podcast'
        assert p.explicit == True
        assert p.description == 'Eriwan_Podcast'
        assert p.website == 'localhost'
        assert p.file.name == 'feed_template.xml'


@pytest.mark.parametrize(
    'all_eps, file_entries', [
        (2, 3), (0, 77777), (15987, 3), (2.789, 0.12), (-1, 1.5)
    ]
)
def test_are_not_equal_pos(all_eps, file_entries):
    with mock.patch('app.models.Episode.query.count', side_effect=lambda: all_eps):
        with mock.patch('pathlib.Path.exists', side_effect=lambda: True):
            with mock.patch('app.rss.RssPodcast.get_number_file_entries',
                            side_effect=lambda: file_entries):
                p = RssPodcast()
                assert p.are_not_equal()


@pytest.mark.parametrize(
    'all_eps, file_entries', [
        (1, -1), (15555, 15555), (0, 0), (-15, -15),
    ]
)
def test_are_not_equal_neg(all_eps, file_entries):
    with mock.patch('app.models.Episode.query.count', side_effect=lambda: all_eps):
        with mock.patch('pathlib.Path.exists', side_effect=lambda: True):
            with mock.patch('app.rss.RssPodcast.get_number_file_entries',
                            side_effect=lambda: file_entries):
                p = RssPodcast()
                assert p.are_not_equal()

