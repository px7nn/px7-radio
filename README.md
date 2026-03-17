# 🎧 PX7 Terminal Radio

![PX7 Terminal Radio](https://github.com/user-attachments/assets/d2737200-ebd8-4736-b460-c9af140e8137)

PX7 Terminal Radio is a lightweight, feature-rich **command-line internet radio player** built in Python.

It lets you **search, stream, and control thousands of radio stations directly from your terminal**, with added support for **streaming audio from YouTube search results**.

Powered by the **Radio Browser API** and **VLC**, PX7 delivers a fast and minimal listening experience without leaving your terminal.


## Features

* Search and stream internet radio stations
* Filter stations by **tag, country, language, bitrate, and more**
* Sort results using API parameters (votes, click count, etc.)
* Playback controls: **play, pause, resume, stop**
* Lightweight and fast CLI interface
* Stream audio directly from **YouTube search results**


## Requirements

* Python **3.9+**
* **VLC Media Player** (required for audio playback)


## 📦 Installation

### Install via pip (Recommended)

```
pip install px7-radio
```


## 🚀 Usage

Start the application:

```
px7-radio
```

You will see a prompt:

```
>>
```

---

## Radio Commands

| Command                              | Description                               |
| ------------------------------------ | ----------------------------------------- |
| `radio search <query>`               | Search radio stations by name             |
| `radio search --tag=<tag>`           | Filter by tag (e.g., jazz, lofi)          |
| `radio search --country=<country>`   | Filter by country                         |
| `radio search --language=<language>` | Filter by language                        |
| `radio search --limit=<number>`      | Limit number of results                   |
| `radio search --order=votes`         | Sort results (votes, clickcount, bitrate) |
| `play <index>`                       | Play selected station                     |
| `pause`                              | Pause playback                            |
| `resume`                             | Resume playback                           |
| `stop`                               | Stop playback                             |

---

### Advanced Filtering

PX7 supports full **Radio Browser API parameters**:

```
radio search lofi --limit=5
radio search --tag=jazz --country=US
radio search chill --order=clickcount
```

API Docs: https://www.radio-browser.info/


## YouTube Commands

Stream audio directly from YouTube search results:

| Command                          | Description               |
| -------------------------------- | ------------------------- |
| `yt search <query>`              | Search and stream audio   |
| `yt search <query> --limit=<n>`  | Limit results             |
| `yt search <query> --no-postfix` | Disable query enhancement |

---

### Smart Query Enhancement

By default:

```
yt search <query>
```

Automatically becomes:

```text
<query> original audio song
```

This improves audio-focused results (songs, mixes, etc.)

Disable it with:

```
yt search <query> --no-postfix
```

---

## 🧠 Example Usage

```
>> radio search lofi
>> play 1
>> yt search joji
>> yt search the weeknd lofi --no-postfix
```

---

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
