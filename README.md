<div align="center"><h1>Telegram Reaction Bot</h1>
<b>An open-source Python Telegram bot that reacts to every message.</b>

<a href="https://t.me/DrReactBot"><b>Demo Bot</b></a>
</div>

## **📑 INDEX**

* [**⚙️ Installation**](#installation)
  * [Python & Git](#i-1)
  * [Download](#i-2)
  * [Requirements](#i-3)
* [**📝 Variables**](#variables)
* [**🕹 Deployment**](#deployment)
  * [Locally](#d-1)
  * [Docker](#d-2)
* [**⛑️ Need help!**](#help)
* [**❤️ Credits & Thanks**](#credits)

<a name="installation"></a>

## ⚙️ Installation

<a name="i-1"></a>

**1.Install Python & Git:**

For Windows:
```
winget install Python.Python.3.12
winget install Git.Git
```
For Linux:
```
sudo apt-get update && sudo apt-get install -y python3.11 git pip
```
For macOS:
```
brew install python@3.12 git
```
For Termux:
```
pkg install python -y
pkg install git -y
```

<a name="i-2"></a>

**2.Download repository:**
```
git clone https://github.com/TheCaduceus/TG-ReactionBot.git
```

**3.Change Directory:**

```
cd TG-ReactionBot
```

<a name="i-3"></a>

**4.Install requirements:**

```
pip install -r requirements.txt
```

<a name="variables"></a>

## 📝 Variables
**The variables provided below should either be completed within the [config.py](https://github.com/TheCaduceus/TG-ReactionBot/blob/main/bot/config.py) file or configured as environment variables.**
* `API_ID`|`TG_API_ID`: API ID of your Telegram account, can be obtained from [My Telegram](https://my.telegram.org). `int`
* `API_HASH`|`TG_API_HASH`: API hash of your Telegram account, can be obtained from [My Telegram](https://my.telegram.org). `str`
* `BOT_TOKEN`|`TG_BOT_TOKEN`: Telegram API token of your bot, can be obtained from [@BotFather](https://t.me/BotFather). `str`
* `BOT_USERNAME`|`TG_BOT_USERNAME`: Username of your Telegram bot without '@'.
* `EMOJIS`: List of emojis that you'd like bot to use.

<a name="deployment"></a>

## 🕹 Deployment

<a name="d-1"></a>

**1.Running locally:**
```
python -m bot
```

<a name="d-2"></a>

**2.Using Docker:** *(Recommended)*
* Build own Docker image:
```
docker build -t reaction-bot .
```
* Run the Docker container:
```
docker run reaction-bot
```

<a name="help"></a>

## ⛑️ Need help!
- Ask questions or doubts [here](https://t.me/DrDiscussion).

<a name="credits"></a>

## ❤️ Credits & Thanks

[**Dr.Caduceus**](https://github.com/TheCaduceus): Owner & developer of TG Reaction Bot.
