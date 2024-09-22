from __future__ import annotations

from typing import Literal, TypedDict

TrackQuality = Literal["LOW", "HIGH", "LOSSLESS", "HI_RES_LOSSLESS"]
ManifestMimeType = Literal["application/dash+xml", "application/vnd.tidal.bts"]


class TrackStream(TypedDict):
    trackId: int
    assetPresentation: Literal["FULL"]
    audioMode: Literal["STEREO"]
    audioQuality: TrackQuality
    manifestMimeType: ManifestMimeType
    manifestHash: str
    manifest: str
    albumReplayGain: float
    albumPeakAmplitude: float
    trackReplayGain: float
    trackPeakAmplitude: float
    bitDepth: int | None
    sampleRate: int | None


class _Artist(TypedDict):
    id: int
    name: str
    type: str
    picture: str | None


class _Album(TypedDict):
    id: int
    title: str
    cover: str
    vibrantColor: str
    videoCover: str | None


class Track(TypedDict):
    id: int
    title: str
    duration: int
    replayGain: float
    peak: float
    allowStreaming: bool
    streamReady: bool
    adSupportedStreamReady: bool
    djReady: bool
    stemReady: bool
    streamStartDate: str
    premiumStreamingOnly: bool
    trackNumber: int
    volumeNumber: int
    version: str | None
    popularity: int
    copyright: str
    bpm: int | None
    url: str
    isrc: str
    editable: bool
    explicit: bool
    audioQuality: str
    audioModes: list[str]
    mediaMetadata: dict[str, list[str]]
    artist: _Artist
    artists: list[_Artist]
    album: _Album
    mixes: dict[str, str]
