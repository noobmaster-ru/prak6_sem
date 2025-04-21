plot:
	clang++ -std=c++11 -isystem /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1 compute.cpp -o main
	./main
	python make_plot.py