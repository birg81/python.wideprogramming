import sys

if __name__ == "__main__":
	if len(sys.argv[1:]) > 0:
		for arg in sys.argv[1:]:
			print arg
	else:
		print "NO ARGs Found!"