HELP_PAGE = """
════════════════════════════════════════════════════════════════════════
                         PX7 TERMINAL RADIO
════════════════════════════════════════════════════════════════════════

Stream internet radio directly from your terminal.

────────────────────────────────────────────────────────────────────────
SEARCH STATIONS
────────────────────────────────────────────────────────────────────────

Basic Search
    >> radio search <name>
    (Example: >> radio search lofi)

Filtered Search
    >> radio search [OPTIONS] <name>
    (Example: >> radio search --tag=jazz --limit=10)

Common Search Options:
    --tag=TAG           Filter by genre (rock, techno, etc)
    --country=NAME      Filter by country name
    --limit=N           Limit number of results (Default: 100)
    --reverse=true      Reverse the sorting order
    --order=ORDER       Sort by: name, votes, clickcount, bitrate

Advanced Filters:
    For more options like --codec, --bitrate, or --language, see:
    https://api.radio-browser.info

────────────────────────────────────────────────────────────────────────
PLAYBACK CONTROLS
────────────────────────────────────────────────────────────────────────

Start Playing
    >> play <number>
    (Example: >> play 1)

Adjust Timeout
    >> play <number> --timeout=10
    (Use for slow connections; default is 5s)

Playback Management
    >> pause            Pause the current stream
    >> resume           Resume the current stream
    >> stop             Stop playback entirely

────────────────────────────────────────────────────────────────────────
STATION INFO
────────────────────────────────────────────────────────────────────────

View Status
    >> show cur             Display Name, Country, and Bitrate
    >> show cur --expose    Show all info including Stream URL

────────────────────────────────────────────────────────────────────────
UTILITY & SYSTEM
────────────────────────────────────────────────────────────────────────

Network Check
    >> ping             Check your connection latency

Exit Application
    >> exit | quit | logout

────────────────────────────────────────────────────────────────────────
EXAMPLE SESSION
────────────────────────────────────────────────────────────────────────

    >> radio search --tag=lofi --limit=5
    >> play 1
    >> show cur --expose
    >> stop
"""
