service.pausespotify
====================

This simple Kodi-Addon is intended for environments where Kodi and Spotify run on the sam system.
The addon pauses the Spotify-Client when Kodi starts playing a file.
When Kodis playback is stopped within 30 seconds or less, the Spotifiy playback is resumed automatically.

The addon needs DBus to work since it uses Spotifys MPRIS-Interface.

The addon only controls Spotify when Kodi playback is detected, it does not pause Kodi when Spotify starts playing.
