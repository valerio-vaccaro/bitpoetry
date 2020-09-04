#!/usr/bin/env pyhton3
#
# .oPYo.  o   o   .oPYo.                 o
# 8   `8      8   8    8                 8
#o8YooP' o8  o8P o8YooP' .oPYo. .oPYo.  o8P oPYo. o    o
# 8   `b  8   8   8      8    8 8oooo8   8  8  `' 8    8
# 8    8  8   8   8      8    8 8.       8  8     8    8
# 8oooP'  8   8   8      `YooP' `Yooo'   8  8     `YooP8
#:......::..::..::..::::::.....::.....:::..:..:::::....8
#:::::::::::::::::::::::::::::::::::::::::::::::::::ooP'.
#:::::::::::::::::::::::::::::::::::::::::::::::::::...::
#
import argparse
import hashlib
import os
banner = """
 .oPYo.  o   o   .oPYo.                 o
 8   `8      8   8    8                 8
o8YooP' o8  o8P o8YooP' .oPYo. .oPYo.  o8P oPYo. o    o
 8   `b  8   8   8      8    8 8oooo8   8  8  `' 8    8
 8    8  8   8   8      8    8 8.       8  8     8    8
 8oooP'  8   8   8      `YooP' `Yooo'   8  8     `YooP8
:......::..::..::..::::::.....::.....:::..:..:::::....8
:::::::::::::::::::::::::::::::::::::::::::::::::::ooP'.
:::::::::::::::::::::::::::::::::::::::::::::::::::...::
"""
def main():
    print(banner)
    parser = argparse.ArgumentParser(description='Create sonnets, ballads and poems for bitcoiners.')
    parser.add_argument('-s', '--stanzas', type=int, help='Number of stanzas (default 1)', default=1)
    parser.add_argument('-n', '--nibbles', type=int, help='Number of nibbles to consider for the rhyme (default 2)', default=2)

    subparsers = parser.add_subparsers(dest='kind')
    subparsers.required = True

    action_parser = subparsers.add_parser('AA')
    action_parser = subparsers.add_parser('AAAA')
    action_parser = subparsers.add_parser('AABB')
    action_parser = subparsers.add_parser('ABAB')
    action_parser = subparsers.add_parser('ABBA')
    action_parser = subparsers.add_parser('ABABB')
    action_parser = subparsers.add_parser('AABBA')
    action_parser = subparsers.add_parser('ABABCBC')
    action_parser = subparsers.add_parser('ABABABCC')

    args = parser.parse_args()

    for i in range(0, args.stanzas):
        A = hashlib.sha256(os.urandom(32)).hexdigest()
        print(A)

        if (args.kind == 'AA'):
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'AAAA'):
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'AABB'):
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            B = hashlib.sha256(os.urandom(32)).hexdigest()
            print(B)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'ABAB'):
            B = hashlib.sha256(os.urandom(32)).hexdigest()
            print(B)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'ABAB'):
            B = hashlib.sha256(os.urandom(32)).hexdigest()
            print(B)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'ABBA'):
            B = hashlib.sha256(os.urandom(32)).hexdigest()
            print(B)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'ABABB'):
            B = hashlib.sha256(os.urandom(32)).hexdigest()
            print(B)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'AABBA'):
            B = hashlib.sha256(os.urandom(32)).hexdigest()
            print(B)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'ABABCBC'):
            B = hashlib.sha256(os.urandom(32)).hexdigest()
            print(B)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            C = hashlib.sha256(os.urandom(32)).hexdigest()
            print(C)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if C[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        elif (args.kind == 'ABABABCC'):
            B = hashlib.sha256(os.urandom(32)).hexdigest()
            print(B)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if A[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if B[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break
            C = hashlib.sha256(os.urandom(32)).hexdigest()
            print(C)
            while(True):
                candidate = hashlib.sha256(os.urandom(32)).hexdigest()
                if C[-args.nibbles:] == candidate[-args.nibbles:]:
                    print(candidate)
                    break

        # next round
        print()

if __name__ == '__main__':
    main()
