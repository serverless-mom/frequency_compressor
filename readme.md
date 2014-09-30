Compressing English with a frequency table

This Python tool attempts to compress a large english text (in this example Moby Dick) with a frequency table of the most common english words. 

To Use:
1) save a .txt file in the root directory
2) set the textFileName and compressFileName in compressor.py
3) run compressor.py

-credits-

This ended up re-inventing Huffman Coding, with some ineffciencies when compared to that technique.

http://en.wikipedia.org/wiki/Huffman_coding

-status-

Currently the compression/decompression process is non-harmful, but the reduction in filesize is small. Due to a behavior around changing some double-spaced sentence endings, the checksum of the de-compressed file isn't identical to the source, but the readable text block should be identical.

-to do-
A few changes to bring us closer to generalized Huffman Coding for English should improve the compression rate vastly