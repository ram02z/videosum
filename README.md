# vidsum

VidSum is an online video summarisation tool that allows you to import videos and recieve a full transcript and summarisation of the video. 

Never again will you watch that boring lecturer. You can now summarise the whole video in just a few clicks.


## Requirements

- Python 3.9+
- FFmpeg

## Setup

### Clone the git repository

```commandline
$> git clone https://github.com/ram02z/videosum.git
```

### Create a virtual enviorenment

```commandline
$> python3 -m venv /path/to/virtualenvs/VidSum
```

### Activate the virtual environment

On Windows:
```commandline
X:\> /path/to/virtualenvs/VidSum/Scripts/activate.bat
```

On Linux:
```commandline
$ . /path/to/virtualenvs/VidSum/bin/activate
```

### Update pip and related packages

```commandline
$> python3 -m pip install -U pip setuptools wheel
```

### Install the dependencies

```commandline
$> python3 -m pip install -r requirements.txt
```

## How to run the web application

```commandline
$> cd backend
```

```commandline
$> python3 -m app.server
```