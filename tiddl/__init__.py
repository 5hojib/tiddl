import argparse
import time

from .api import TidalApi
from .auth import getDeviceAuth, getToken, refreshToken
from .config import Config
from .utils import decodeManifest, parseTrackManifest, downloadTrack


def main():
    parser = argparse.ArgumentParser(description="TIDDL, the Tidal Downloader")
    config = Config()

    if not config["token"]:
        auth = getDeviceAuth()
        input(
            f"⚙️ Go to https://{auth['verificationUriComplete']} and add device!\nHit enter when you are ready..."
        )
        token = getToken(auth["deviceCode"])
        config.update(
            {
                "token": token["access_token"],
                "refresh_token": token["refresh_token"],
                "token_expires_at": int(time.time()) + token["expires_in"],
                "user": {
                    "user_id": str(token["user"]["userId"]),
                    "country_code": token["user"]["countryCode"],
                },
            }
        )
        print("✅ Got token!")

    t_now = int(time.time())
    token_expired = t_now > config["token_expires_at"]
    if token_expired:
        token = refreshToken(config["refresh_token"])
        config.update(
            {
                "token": token["access_token"],
                "token_expires_at": int(time.time()) + token["expires_in"],
            }
        )
        print("✅ Refreshed token!")

    # TODO: format time to days and hours ✨
    time_to_expire = config["token_expires_at"] - t_now
    print(f"✅ Token good for {time_to_expire}s")

    api = TidalApi(
        config["token"], config["user"]["user_id"], config["user"]["country_code"]
    )

    playlists = api.getPlaylists()
    print(f"You have got {playlists['totalNumberOfItems']} playlists.")

    track_id = int(input("Enter track id to download: "))

    track = api.getTrack(track_id, config["settings"]["track_quality"])
    decoded_manifest = decodeManifest(track["manifest"])
    track_urls, codecs = parseTrackManifest(decoded_manifest)
    downloadTrack(track_id, track_urls)


if __name__ == "__main__":
    main()
