import argparse
import json
from collections import defaultdict

import imagehash
from PIL import Image
from moviepy.video.io.VideoFileClip import VideoFileClip


def main(args):

    if args.use:
        frames = []
        for filename in sorted(args.use):
            with open(filename) as f:
                frames.extend(imagehash.hex_to_hash(frame) for frame in json.load(f))
    else:
        clip = VideoFileClip(args.file)
        frames = [imagehash.dhash(Image.fromarray(frame)) for frame in clip.iter_frames()]

    if args.save:
        with open(args.file + '.json', 'w') as f:
            json.dump([str(frame) for frame in frames], f)

    counts = defaultdict(int)
    for frame in frames:
        counts[str(frame)] += 1

    scores = [counts[str(frame)] for frame in frames]
    print(json.dumps(scores))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze video for reused frames.')
    parser.add_argument('-s', '--save', help='save the calculated hashes', action='store_true')
    parser.add_argument('-u', '--use', help='use file as saved hashes instead of video', action='append')
    parser.add_argument('file', help='input file to process', nargs='?')

    args = parser.parse_args()
    main(args)
