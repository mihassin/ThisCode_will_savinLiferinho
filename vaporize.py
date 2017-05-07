import sys


def vaporize(romanji):
	__HALF2FULL__ = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
	__HALF2FULL__[0x20] = 0x3000
	print(str(romanji).translate(__HALF2FULL__))


if __name__ == '__main__':
	string = ' '.join(sys.argv[1:])
	vaporize(string)
