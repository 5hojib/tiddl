from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from requests import Session

if TYPE_CHECKING:
    from .types import (
        Album,
        Track,
        Playlist,
        AlbumItems,
        TrackStream,
        TrackQuality,
        PlaylistItems,
        SessionResponse,
        AristAlbumsItems,
    )

API_URL = "https://api.tidal.com/v1"


class TidalApi:
    def __init__(self, token: str, user_id: str, country_code: str) -> None:
        self.token = token
        self.user_id = user_id
        self.country_code = country_code

        self._session = Session()
        self._session.headers = {"authorization": f"Bearer {token}"}
        self._logger = logging.getLogger("TidalApi")

    def _request(self, endpoint: str, params=None):
        if params is None:
            params = {}
        self._logger.debug(f"{endpoint} {params}")
        req = self._session.request(
            method="GET", url=f"{API_URL}/{endpoint}", params=params
        )

        # TODO: endpoints error handling ✨

        return req.json()

    def getSession(self) -> SessionResponse:
        return self._request(
            "sessions",
        )

    def getTrackStream(self, id: str | int, quality: TrackQuality) -> TrackStream:
        return self._request(
            f"tracks/{id}/playbackinfo",
            {
                "audioquality": quality,
                "playbackmode": "STREAM",
                "assetpresentation": "FULL",
            },
        )

    def getTrack(self, id: str | int) -> Track:
        return self._request(f"tracks/{id}", {"countryCode": self.country_code})

    def getArtistAlbums(
        self, id: str | int, limit=50, offset=0, onlyNonAlbum=False
    ) -> AristAlbumsItems:
        params = {"countryCode": self.country_code, "limit": limit, "offset": offset}

        if onlyNonAlbum:
            params.update({"filter": "EPSANDSINGLES"})

        return self._request(
            f"artists/{id}/albums",
            params,
        )

    def getAlbum(self, id: str | int) -> Album:
        return self._request(f"albums/{id}", {"countryCode": self.country_code})

    def getAlbumItems(self, id: str | int, limit=10, offset=0) -> AlbumItems:
        return self._request(
            f"albums/{id}/items",
            {"countryCode": self.country_code, "limit": limit, "offset": offset},
        )

    def getPlaylist(self, uuid: str) -> Playlist:
        return self._request(
            f"playlists/{uuid}",
            {"countryCode": self.country_code},
        )

    def getPlaylistItems(self, uuid: str, limit=50, offset=0) -> PlaylistItems:
        return self._request(
            f"playlists/{uuid}/items",
            {"countryCode": self.country_code, "limit": limit, "offset": offset},
        )
