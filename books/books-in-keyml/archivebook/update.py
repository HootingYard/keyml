from glob import glob
from sys import argv
from os.path import import join

DATA = argv[1]
POSTS = join(DATA, 'posts')

def main():
    for path in glob(join(POSTS, '*[0-9][0-9].htm')):
        print(path)

if __name__ == '__main__':
    main()