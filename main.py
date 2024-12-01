from collections import defaultdict, Counter
from HuffmanCoding import HuffmanCoding



# Exemple d'utilisation
if __name__ == "__main__":
    huffman = HuffmanCoding()

    # Compresser un fichier
    input_file = "atelier4.pdf"  # Fichier source
    compressed_file = "atelier4_com.pdf"  # Fichier compressé
    huffman.compress(input_file, compressed_file)

   

    # Décompresser un fichier
    decompressed_file = "atelier4_decompress.pdf"  # Fichier décompressé
    huffman.decompress(compressed_file, decompressed_file)
    # Vérification du contenu du fichier décompressé
    with open(decompressed_file, 'r') as f:
        decompressed_content = f.read()
        print("\nContenu du fichier décompressé :")
        print(decompressed_content)
