from pathlib import Path
from podgen import Podcast, Episode, Person, Media
import xml.etree.ElementTree as ET

from flask import Response
from app import app

from . import models

file = Path('app/templates/feed_template.xml')


class RssResponse(Response):
    def __init__(self, response, **kwargs):
        if 'mimetype' not in kwargs and 'contenttype' not in kwargs:
            if response.startswith('<?xml'):
                kwargs['mimetype'] = 'application/xml'
        return super().__init__(response, **kwargs)


class RssPodcast(Podcast):
    """
    Custom class for comfortable work with the Podcast
    """

    def __init__(self):
        super().__init__()
        self.name = "Eriwan_Podcast"
        self.explicit = True
        self.description = 'Eriwan_Podcast'
        self.website = app.config.get('HOST', 'localhost')
        self.file = file

        if not self.file.exists():
            self.rss_file(self.file.as_posix())

    def are_not_equal(self):
        all_eps = models.Episode.query.count()
        file_entries = self.get_number_file_entries()
        return all_eps != file_entries

    def get_number_file_entries(self):
        if self.file.exists():
            tree = ET.parse(self.file.absolute())
            root = tree.getroot()
            return len([i.tag for i in root.iter('item')])

    def sync_episodes(self):
        [self.episodes.remove(ep) for ep in self.episodes]
        query = models.Episode.query.all()
        for ep in query:
            user = models.User.query.filter_by(id=ep.user_id).first()
            email = user.email
            pdg_ep = Episode()
            pdg_ep.title = ep.name
            pdg_ep.link = str(ep.get_link())
            pdg_ep.media = Media(url=pdg_ep.link,  type='mp3')
            pdg_ep.authors = [
                Person(name=user, email=email)] if not user.is_admin else []
            self.add_episode(pdg_ep)
