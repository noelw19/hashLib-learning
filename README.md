# hashLib-learning
This repo will contain one or more py scripts that i will use to help understand the hash lib library in python, formerly known as md5 in python 2.7 but since python3 md5 has been depricated.


--------------------- hashlib1 --------------------------

This scipt is me trying to understand how gobuster works, building a password cracker that uses a text file with a list of passwords, initially built the password cracker but wanted to test it dynamically each time i ran the script. 

Use: Run script enter a password for the script to crack, enter the password list filename or leave empty to use the password list in the directory and wait for it to be cracked or not.

I added an input that takes a password to crack, the script takes this input string and uses the codec library encode method to encode the string as utf-8.

The result of the above is then hashed using the md5 cryptographic hashing algorithm with hashlibs md5 method.

Then the script proceeds to check each value in the password list encoding it as utf-8 and hashing the value and then comparing the hashes to find a match if any.

If a match is found the password is printed to the console with the amount of attempts, because I like to see how many attempts were tried and how fast the script runs through attempts.

There is an outer try catch because for another password list I was using I would get this error:

        UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 923: invalid continuation byte

I couldnt find a fix for this and the amount of attempts it would stop at was 60137 even though there was alot more passwords in the list, i tried reading the txt file as bytes and decoding the bytes before i encoded it as utf-8, tried using the chardet library to find the file encoding which was a fail, as it told me it was ascii encoded, but changing the pass list seemed to work fine and print no password found when the file was ran through.
    

