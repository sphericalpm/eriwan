from podgen import Podcast, Media, Episode, Person
from flask import Response

from app import app
from app.models import get_random_jokes_from_db, get_all_episodes
from . import models


class RssResponse(Response):
    def __init__(self, response, **kwargs):
        if 'mimetype' not in kwargs and 'contenttype' not in kwargs:
            if response.startswith('<?xml'):
                kwargs['mimetype'] = 'application/xml'
        return super().__init__(response, **kwargs)


podcast = Podcast(name="Eriwan_Podcast",
                  description='Eriwan_Podcast',
                  website=app.config.get('HOST', 'localhost'),
                  explicit=True)


def get_rss_feed():
    episodes = get_episodes()
    length = len(episodes)
    jokes = get_jokes_episodes(length)
    podcast.episodes = []
    for i in range(length):
        podcast.episodes.append(jokes[i % len(jokes)])
        podcast.episodes.append(episodes[i])
    return podcast.rss_str()


def convert_episode(episode):
    podcast_episode = Episode()
    podcast_episode.title = episode.name
    podcast_episode.link = str(episode.get_link())
    podcast_episode.media = Media(url=podcast_episode.link, type='mp3')
    user = models.User.query.filter_by(id=episode.user_id).first()
    podcast_episode.authors = [Person(name=user.username, email=user.email)]
    return podcast_episode


def get_episodes():
    episodes = get_all_episodes()
    return list(map(convert_episode, episodes))


def convert_joke_to_podcast_episode(joke):
    podcast_joke = Episode()
    podcast_joke.title = str(joke.id)
    podcast_joke.link = str(joke.get_link())
    podcast_joke.media = Media(url=podcast_joke.link, type='mp3')
    return podcast_joke


def get_jokes_episodes(limit):
    jokes = get_random_jokes_from_db(limit)
    return list(map(convert_joke_to_podcast_episode, jokes))
