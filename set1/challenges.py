import base64
from rich import print
import binascii


def hex_to_base(string: str) -> str:
    """
    Convert hex to base64
    The string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
    Should produce: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

    Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

    The return type str is only for printing. Inside the function we will operate on byte level.

    Irá chegar uma string qualquer. Deve mudar o tipo de str para bytes, mesmo que a string esteja em hexadecimal, o tipo dela é string. Desta forma,
        fica díficil operar.
    1. De str para bytes
    2. De bytes para hexadecimal
    3. De hexadecimal para base64
    4. Como o método b64encode retorna um tipo byte, precisamos mudar para string (em outras linguagens, casting)
    """

    print(
        f"Received string: [green]{string}[/green] of type [green]{type(string)}[/green]"
    )

    byte_string = string.encode()
    print(
        f"Content and type of byte_string: [purple]{byte_string}[/purple] of type [purple][u]{type(byte_string)}[/purple][/u]"
    )

    hex_string = binascii.unhexlify(byte_string)
    print(
        f"Content of the hex_string decodified (from hex to str human readable): {hex_string}"
    )

    b64_string = base64.b64encode(hex_string)
    print(f'From hex to base64 and type: {b64_string} of type {(type(b64_string))}')

    return b64_string.decode('utf-8')
