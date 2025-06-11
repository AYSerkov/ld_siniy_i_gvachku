def decrypt_file(input_path, output_path):
    with open(input_path, 'rb') as file:
        key = file.read(32)
        if len(key) != 32:
            raise ValueError("Invalid file format: Key not found or is too short.")

        encrypted_data = file.read()

    decrypted_data = bytearray(
        encrypted_data[i] ^ key[i % len(key)] for i in range(len(encrypted_data))
    )

    with open(output_path, 'wb') as output_file:
        output_file.write(decrypted_data)

    print(f"Decrypted dump saved to {output_path}")


if __name__ == "__main__":
    decrypt_file("output.bin", "dump.dmp")
