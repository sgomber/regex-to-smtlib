import sys

from src.reg_parser import parser

if __name__ == "__main__":
    result = parser.parse(sys.argv[1])
    print(result)
