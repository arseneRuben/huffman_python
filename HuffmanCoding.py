import os
import heapq
from Node import Node
from collections import defaultdict, Counter

class HuffmanCoding:
    """Classe pour compresser et décompresser avec le code de Huffman."""
    def __init__(self):
        self.codes = {}
        self.reverse_mapping = {}
        self.frequency_table = {}

    def build_frequency_table(self, text):
        """Construit une table de fréquences à partir d'un texte."""
        self.frequency_table =  Counter(text)
        return Counter(text)

    def build_huffman_tree(self, frequency_table):
        """Construit l'arbre de Huffman à partir de la table de fréquences."""
        priority_queue = [Node(char, freq) for char, freq in frequency_table.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(priority_queue, merged)

        return priority_queue[0]

    def build_codes(self, root, current_code=""):
        """Construit les codes de Huffman à partir de l'arbre."""
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.build_codes(root.left, current_code + "0")
        self.build_codes(root.right, current_code + "1")

    def compress(self, input_path, output_path):
        """Compresse un fichier en utilisant le code de Huffman."""
        with open(input_path, 'r') as file:
            text = file.read()

        frequency_table = self.build_frequency_table(text)
        root = self.build_huffman_tree(frequency_table)
        self.build_codes(root)

        encoded_text = "".join(self.codes[char] for char in text)

        # Ajoute du padding pour compléter les bits
        extra_padding = 8 - len(encoded_text) % 8
        encoded_text += "0" * extra_padding
        padded_info = f"{extra_padding:08b}"
        encoded_text = padded_info + encoded_text

        # Sauvegarde dans un fichier binaire
        byte_array = bytearray()
        for i in range(0, len(encoded_text), 8):
            byte = encoded_text[i:i+8]
            byte_array.append(int(byte, 2))

        with open(output_path, 'wb') as output:
            output.write(byte_array)

        print(f"Fichier compressé : {output_path}")

    def decompress(self, input_path, output_path):
        """Décompresse un fichier en utilisant le code de Huffman."""
        with open(input_path, 'rb') as file:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bit_string += f"{byte:08b}"
                byte = file.read(1)

        # Supprimer le padding
        padded_info = bit_string[:8]
        extra_padding = int(padded_info, 2)
        bit_string = bit_string[8:-extra_padding]

        current_code = ""
        decoded_text = []

        for bit in bit_string:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text.append(character)
                current_code = ""

        decoded_text = "".join(decoded_text)

        with open(output_path, 'w') as output:
            output.write(decoded_text)

        print(f"Fichier décompressé : {output_path}")