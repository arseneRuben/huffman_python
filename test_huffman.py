from HuffmanCoding import HuffmanCoding

def testA():   # Compresser un fichier
    huffman = HuffmanCoding()
    input_file = "exemple.txt"  # Fichier source
    compressed_file = "exemple_com.txt"  # Fichier compressé
    huffman.compress(input_file, compressed_file)
    assert huffman.frequency_table['a']==5

def testB():   # Compresser un fichier
    huffman = HuffmanCoding()
    input_file = "exemple.txt"  # Fichier source
    compressed_file = "exemple_com.txt"  # Fichier compressé
    huffman.compress(input_file, compressed_file)
    assert huffman.frequency_table['b']==1

