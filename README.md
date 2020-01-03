# mkwii-presence
Mario Kart Wii (Wiimmfi) Rich Presence for Discord
## Features
- Updates every 15 seconds (Discord minimum)
- Displays your **friend code** (if desired) or any other message, 
- Displays whether you're playing **Worldwide, Regional or Friends**
- Displays **current track** with image
- Displays whether it is a **VS race or a Battle match**
- Displays **number of players** in the lobby
- Loads from a configuration file
- [Precompiled binaries](https://github.com/dotcomboom/mkwii-presence/releases)
## Screenshots
**VS race:**

![VS race](https://github.com/dotcomboom/mkwii-presence/blob/master/screenshots/vs.gif?raw=true)

**Battle:**

![Battle](https://github.com/dotcomboom/mkwii-presence/blob/master/screenshots/battle.png?raw=true)

**Offline/not in a room:**

![Offline/no room](https://github.com/dotcomboom/mkwii-presence/blob/master/screenshots/offline.png?raw=true)
## Configuration
When you run the program for the first time, it will write a skeleton configuration to `config.json`, like this:
```json
{
  "friendCode": null,
  "watchURL": "https://wiimmfi.de/mkw/room/p[YOUR ID]"
}
```
**`friendCode`** can be your friend code or other message surrounded by quotes. Leave it as `null` if you don't want to show it.
**`watchURL`** is the important bit: it's the page to scrape. To find this, go the [Wiimmfi MKW Stats page](https://wiimmfi.de/mkw/) *while you are in an online match* and find your friend code or Mii name. Put the URL the *eye icon* ![Watch icon](https://wiimmfi.de/images/watch-pid-24x16.png) next to your friend code links to here.

Advanced users might want to use their own Discord application for the Rich Presence. For that, you can add a **`client_id`** key, with your Discord-given Client ID. You'll need to upload [the art assets](https://github.com/dotcomboom/mkwii-presence/tree/master/discord-assets) yourself.
