# Caesar Cipher

This repository contains a Python implementation of the **Caesar Cipher**, a simple encryption technique that shifts the letters of the alphabet by a specified number of positions. This project allows users to both encrypt and decrypt messages.

## Features

- **Encryption**: Converts plaintext messages into ciphertext by shifting letters forward in the alphabet.
- **Decryption**: Converts ciphertext back into plaintext by reversing the shift.
- **Customizable Shift**: Users can specify the shift amount for encryption and decryption.
- **User-Friendly Interface**: Provides a command-line interface for entering messages and selecting options.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/masood2004/Caesar_Cipher.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Caesar_Cipher
   ```

3. **Ensure Python is installed**:

   - This project requires Python 3.x. You can download it from the [official Python website](https://www.python.org/downloads/).

## Usage

1. **Run the program**:
   ```bash
   python main.py
   ```

2. **Follow the prompts**:
   - Choose whether to encrypt or decrypt a message.
   - Enter the message and the shift amount as instructed.
   - View the resulting encrypted or decrypted message.

## Example

Here’s an example interaction:

```
Welcome to the Caesar Cipher!
Type 'encrypt' to encode a message, or 'decrypt' to decode a message: encrypt
Enter your message: hello
Enter the shift amount: 5
Here's the encoded message: mjqqt
```

## Project Structure

```
Caesar_Cipher/
├── main.py
├── README.md
└── LICENSE
```

- **main.py**: The main script containing the Caesar Cipher implementation and interactive interface.
- **README.md**: Documentation for the project.
- **LICENSE**: License file for the project.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/masood2004/Caesar_Cipher/blob/main/LICENSE) file for details.

## Acknowledgments

This project is an educational implementation of the Caesar Cipher, demonstrating string manipulation and modular arithmetic in Python.

Encrypt your messages and explore the basics of cryptography with this Caesar Cipher tool! 🔐✨
