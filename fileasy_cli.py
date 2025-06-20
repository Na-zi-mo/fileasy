import converter as converter
import sys
import argparse



parser = argparse.ArgumentParser(
    prog='fileasy',
    description='script')

parser.add_argument('mode', '-m', type='str', default='convert')

args = parser.parse_args()

print(f'yo {args}')

# converter.jpg_to_pdf()