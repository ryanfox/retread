# retread
Detect reused frames in video with Python.

Retread works by computing a hash for each frame in a video (dhash, [described here](http://www.hackerfactor.com/blog/?/archives/529-Kind-of-Like-That.html) if you're interested).
It then counts how many times in the video that frame is reused.  Once the duplicates are calculated, the data is output in JSON format, suitable for use in e.g. [D3.js](https://d3js.org/).

A video with low reuse across the board doesn't repeat many frames - not many duplicated shots, and not very long static images either.  For example, _Mad Max Fury Road_, a fast-moving film with short shots and quick cuts:

![mad max fury road](https://i.imgur.com/ZUIVTWh.png)

A video with high spikes reuses a lot of short shots or single images.  For example, _Memento_, a film notable for its nonlinear story, cutting forward and backward across the same scenes:

![memento](https://i.imgur.com/YZ6vORD.png)

## Installation
Clone the repository:

    $ git clone git@github.com:ryanfox/retread.git

Install dependencies:

    $ cd retread
    $ pip install -r requirements.txt

## Usage

### Quickstart

    $ python retread.py my_video.mp4 > scores.json

Open `bar.html` in a browser to see the data plotted.

### Advanced usage
Process a video file:

    $ python retread.py my_video.mp4 > scores.json

`scores.json` will contain a list of integers, where each element is the number of duplicates that frame had in the original.

Processing a video can take a while - several minutes for a feature-length file.  There are a lot of frames to analyze!  If you want to reprocess the same video without waiting, you can use the flag `-s` (for "save") to save the hashes for later:

    $ python retread.py -s my_video.mp4 > scores.json

The hashes will be saved in `my_video.mp4.json`.  retread will overwrite the file if it already exists.

To reuse saved hashes, use the flag `-u` (for "use"):

    $ python retread.py -u my_video.mp4.json > scores.json

This will read the saved hashes (much faster than re-processing the whole video), do the duplicate analysis, and write the duplicate counts to standard out as usual.

To see what the most-duplicated frames are, you can save a jpeg image of the N most common frames.  Use the flag `-c` (for "common"):

    $ python retread.py -c 5 my_video.mp4 > scores.json
    $ ls
    0.jpg
    1.jpg
    2.jpg
    3.jpg
    4.jpg
    my_video.mp4
    [etc...]

This can be combined with `-u`, but you still need to specify the video file):

    $ python retread.py -u my_video.mp4.json -c 5 my_video.mp4 > scores.json
    $ ls
    0.jpg
    1.jpg
    2.jpg
    3.jpg
    4.jpg
    my_video.mp4
    my_video.mp4.json
    [etc...]
