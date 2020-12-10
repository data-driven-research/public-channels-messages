# -*- coding: utf-8 -*-
import json
import pandas as pd
from pathlib import Path
from collections import namedtuple


PATH = Path(__file__).resolve().parent / "data"
Channel = namedtuple("Channel", "channel_id channel_name channel_type posts")


def _is_str(text):
    """Checks whether `text` is a non-empty str. """
    return isinstance(text, str) and text != ""


def _text_parser(text):
    """Processes message["text"] content. """
    if isinstance(text, list):
        return "; ".join(chunk for chunk in text if _is_str(chunk))
    elif isinstance(text, str) and text != "":
        return text


def message_parser(message):
    """Processes message's content - both metadata and text. """
    txt = _text_parser(message["text"])
    if txt:
        yield {
            "id": message["id"],
            "type": message["type"],
            "date": message["date"],
            "text": _text_parser(message["text"]),
        }


def json_to_dataframe(data):
    """Creates an instance of Channel from `data`. """
    df = pd.concat(
        [pd.DataFrame(message_parser(item)) for item in data["messages"]],
        ignore_index=True,
    )
    return Channel(
        channel_id=data["id"],
        channel_name=data["name"],
        channel_type=data["type"],
        posts=df,
    )


def main():
    with open(PATH / "raw" / "result.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    result = json_to_dataframe(data)
    content = result.posts
    file_name = result.channel_id

    content.to_csv(PATH / "interim" / f"result_{file_name}.csv", index=False)


if __name__ == "__main__":
    main()
