# BitPoetry
Create sonnets, ballads and poems for bitcoiners using entropy of your computer
and sha256.

## Prerequisites
Install a Bitcoin full node following instructions at
[https://bitcoin.org/en/full-node](https://bitcoin.org/en/full-node).

Backup your wallet.

Buy and hodl Bitcoin.

Without these prerequisites the software may not work ... and if it works you
still have to install a full node sooner or later ... DO IT NOW! ;)

## Usage
Just call the `bitpoetry.py` with python3.

```
python3 bitpoetry.py -h
usage: bitpoetry.py [-h] [-s STANZAS] [-n NIBBLES]
                    {AA,AAAA,AABB,ABAB,ABBA,ABABB,AABBA,ABABCBC,ABABABCC} ...

Create sonnets, ballads and poems for bitcoiners.

positional arguments:
  {AA,AAAA,AABB,ABAB,ABBA,ABABB,AABBA,ABABCBC,ABABABCC}

optional arguments:
  -h, --help            show this help message and exit
  -s STANZAS, --stanzas STANZAS
                        Number of stanzas (default 1)

  -n NIBBLES, --nibbles NIBBLES
                        Number of nibbles to consider for the rhyme (default 2)
```



## Examples
A simple execution with 1 stanza with an AA rhyme.

```
python3 bitpoetry.py AA | lolcat

 .oPYo.  o   o   .oPYo.                 o
 8   `8      8   8    8                 8
o8YooP' o8  o8P o8YooP' .oPYo. .oPYo.  o8P oPYo. o    o
 8   `b  8   8   8      8    8 8oooo8   8  8  `' 8    8
 8    8  8   8   8      8    8 8.       8  8     8    8
 8oooP'  8   8   8      `YooP' `Yooo'   8  8     `YooP8
:......::..::..::..::::::.....::.....:::..:..:::::....8
:::::::::::::::::::::::::::::::::::::::::::::::::::ooP'.
:::::::::::::::::::::::::::::::::::::::::::::::::::...::


ce9481a0480956cba0339c14735e28f405fef04cffb2f86c56e54992352ea27e
6f34a1bf19e25582f45bd48c73dcadf4a53d1b6efb85ff2088ee7bddff18c57e
```

Create 3 stanzas with rhyme schema ABABCBC considering last 4 nibbles
(hehadecimal chars).

```
python3 bitpoetry.py -s 3 -n 4 ABABCBC | lolcat

 .oPYo.  o   o   .oPYo.                 o
 8   `8      8   8    8                 8
o8YooP' o8  o8P o8YooP' .oPYo. .oPYo.  o8P oPYo. o    o
 8   `b  8   8   8      8    8 8oooo8   8  8  `' 8    8
 8    8  8   8   8      8    8 8.       8  8     8    8
 8oooP'  8   8   8      `YooP' `Yooo'   8  8     `YooP8
:......::..::..::..::::::.....::.....:::..:..:::::....8
:::::::::::::::::::::::::::::::::::::::::::::::::::ooP'.
:::::::::::::::::::::::::::::::::::::::::::::::::::...::


8f7144f3754075c89276431b206473736ac0cd44d591d191687eb42e3a11cbf4
5f78cfaf3f668d5dfa0862358f381198c85ca8ad15ea0926cc40bfb72663012e
34c6249249d3ae447d1019f28329bfa06ba3f1a4cecf086c3bb03f956a0ecbf4
71c24b125750693a9ce0b42460a5892f5696d40945f3479e8f30c3e90ae0012e
7334d0dd49bc06db588112e1244f1ae1d321a0a67e057cdd5a2d342a27a9c0f8
157c8e64fdcf8c28622621ef13ed7d65ddb98725a2bd577a2982ed071479012e
581bd8d1901b2abc30c814cac850458e673b0fa4d32b9f51f04d0343fc7ac0f8


85baef2540b250e92e6843a50a9bb83b5003ba744b46968d4fb35b4a5fbc9cfd
087bc14607602beb128e04abaf138455782eda006476dd3fed248c6291332822
2b03436fddc2b555b9198464895a23f61928325cb22dd7c9edc957945f219cfd
93f5ece98bc424bbbe6d9094e6794607ca1c957954415e63e55510d0034e2822
a33ea6ab643f658c409da771ac02dfd51c38e9d5386d962984a9f2434a5fc22a
66b203d717de1c80e4aabb9355fd04d1c11e59a241637790b1b07e5ab1f52822
a41b6a74cee016f533e28e1fafd1f5ca95e23c0c16e82733b45236518a52c22a

c4eed21e1e409ccd89f02b0d2a74777cad6d7d9598dad2e6db246c338c465edf
d1e2b05475ad65ed9bab8262b890fe692e22f6126815dc9343604d6bae0a9a7d
dc2602542c907cfbae346312ded521b1d8d80be3dc5318f6ca0f9f18fa255edf
a0a9f69b41b98ee65b30844646e6e3c5db16699ec591f421646209db44749a7d
732d8fcde8fdc2157eeadb58741b3f33c9d392daa3bc246924f535515a204fa5
69f979e1c7a295b880fc6ca67ca1c2e56f9077098bb7eecf710f6616b5d49a7d
19db88605441d37549b32d2213122d531795a69088f9c3615f652e99262f4fa5
```

The use of lolcat is strongly recommended!
