public-channels-messages
========================

About
-----

This repository contains basic script to process messages from telegram's public channels; 
extracts message's text and metadata and *potentially* assigns tags based on its category 
(whether original or forwarded message; whether contains photos/videos/polls etc.). 

Usage
-----

.. code-block:: console

    $ git clone https://github.com/data-driven-research/public-channels-messages.git 
    $ cd public-channels-messages
    $ python3 -m venv env
    $ . env/Scripts/activate
    (env)$ pip install -r requirements.txt
    (env)$ python main.py

The following code assumes that the input file is named ``result.json`` and is located at ``data/raw/``
