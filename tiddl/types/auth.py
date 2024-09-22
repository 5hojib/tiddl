from __future__ import annotations

from typing import TypedDict


class _User(TypedDict):
    userId: int
    email: str
    countryCode: str
    fullName: str | None
    firstName: str | None
    lastName: str | None
    nickname: str | None
    username: str
    address: str | None
    city: str | None
    postalcode: str | None
    usState: str | None
    phoneNumber: str | None
    birthday: str | None
    channelId: int
    parentId: int
    acceptedEULA: bool
    created: int
    updated: int
    facebookUid: int
    appleUid: str | None
    googleUid: str | None
    accountLinkCreated: bool
    emailVerified: bool
    newUser: bool


class AuthResponse(TypedDict):
    user: _User
    scope: str
    clientName: str
    token_type: str
    access_token: str
    expires_in: int
    user_id: int


class AuthResponseWithRefresh(AuthResponse):
    refresh_token: str


class AuthDeviceResponse(TypedDict):
    deviceCode: str
    userCode: str
    verificationUri: str
    verificationUriComplete: str
    expiresIn: int
    interval: int
