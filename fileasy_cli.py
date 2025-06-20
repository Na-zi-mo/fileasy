import converter
import merger
import sys
import argparse

class FileEasy:

    def setup(self):

        self.parser.add_argument('-c', '--convert', action='store_true', help='Convert the input file')
        self.parser.add_argument('-m', '--merge', action='store_true', help='Merge the input files')
        self.parser.add_argument('-i', '--input', type=str, help='Input file for conversion')
        self.parser.add_argument('-o', '--output', type=str, help='Output file for conversion')
        self.parser.add_argument('-f', '--files', help='List of files to merge', nargs='+')


        self.args = self.parser.parse_args()
        print(f'Args: {self.args}')

        if self.args.convert:
            print('Convertor')
            converter.jpg_to_pdf(self.args.input_file, self.args.output_file)
        elif self.args.merge:
            print('Merger')
            merger.merge(self.args.files)


    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='fileasy',
            description='script'
        )

        self.setup()

fileEasy = FileEasy()