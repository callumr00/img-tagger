import argparse
import os

from tag import get_images, process_images
from search import find_matches, display_matches

DEFAULT_TAGS_FILE = os.path.join(os.path.expanduser('~'), 'tags.csv')

def cli():
    parser = argparse.ArgumentParser(
        prog='img-tagger',
        description='A CLI tool for image tagging and searching.'
    )

    parser.add_argument(
        '-t', '--tag',
        type=str,
        help='Directory containing images to tag.'
    )
    parser.add_argument(
        '-s', '--search',
        type=str,
        help='Search for query matches.',
    )
    parser.add_argument(
        '-f', '--file',
        type=str,
        default=DEFAULT_TAGS_FILE,
        help='Output file containing tags.'
    )
    parser.add_argument(
        '-m', '--matches',
        type=int,
        default=12,
        help='Max number of matches to return in search.'
    )
    parser.add_argument(
        '-c', '--columns',
        type=int,
        default=4,
        help='Number of columns to display in search.'
    )

    args = parser.parse_args()

    if args.file == DEFAULT_TAGS_FILE:
        print('Note that you are using the default output file:')
        print(f'\t{DEFAULT_TAGS_FILE}')
        print('You can change this using the -f or --file flag.\n')

    if not os.path.isfile(args.file):
        try:
            with open(args.file, 'a'):
              pass
        except IOError:
            raise

    if args.tag:
        if not os.path.exists(args.tag):
            raise FileNotFoundError

        img_list = get_images(img_dir=args.tag, tags_file=args.file)

        if not img_list:
            print('Up to date!')
        else:
            process_images(img_dir=args.tag,
                           tags_file=args.file,
                           img_list=img_list)

    if args.search:
        matches = find_matches(tags_file=args.file,
                               query=args.search,
                               max_matches=args.matches)

        display_matches(matches=matches, num_cols=args.columns)

if __name__ == '__main__':
    cli()
