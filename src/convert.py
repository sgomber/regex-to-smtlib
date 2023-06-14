import sys

from src.reg_parser import parser

class RegexpToSmtLibConvertor():
    def convert(self, str):
        str = str + "$" # To mark the end
        return parser.parse(str)

if __name__ == "__main__":
    convertor = RegexpToSmtLibConvertor()
    print(convertor.convert(sys.argv[1]))
