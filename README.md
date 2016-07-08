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
The simplest way - just process a video file:

    $ python retread.py my_video.mp4 > scores.json

Processing a video can take a while - several minutes for a feature-length file.  There are a lot of frames to analyze!  Once it's done, open `bar.html` in a web browser to view the results.  It will look for a file named `scores.json` to populate data.

Save hashes for faster re-use later:

    $ python retread.py -s my_video.mp4 > scores.json

Reuse saved hashes:

    $ python retread.py -u my_video.mp4.json > scores.json

Save the N most common frames (can be combined with `-u`, but still need to specify file):

    $ python retread.py -u my_video.mp4.json -c 5 my_video.mp4 > scores.json
    $ ls
    0.jpg
    1.jpg
    2.jpg
    3.jpg
    4.jpg
    my_video.mpy
    [etc...]
