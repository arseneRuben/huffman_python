from collections import defaultdict, Counter
from HuffmanCoding import HuffmanCoding



     

# Exemple d'utilisation
if __name__ == "__main__":
    huffman = HuffmanCoding()

    # Compresser un fichier
    input_file = "exemple.txt"  # Fichier source
    compressed_file = "exemple_com.txt"  # Fichier compressé
    huffman.compress(input_file, compressed_file)
    print(huffman.frequency_table)


    # Décompresser un fichier
    decompressed_file = "exemple_decompress.txt"  # Fichier décompressé
    huffman.decompress(compressed_file, decompressed_file)
    # Vérification du contenu du fichier décompressé
    with open(decompressed_file, 'r') as f:
        decompressed_content = f.read()
        print("\nContenu du fichier décompressé :")
        print(decompressed_content)
