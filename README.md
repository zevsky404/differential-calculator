# differential-calculator
### Note: This is a wip and I might make it more accessible and modular in the future.
A python script to calculate the probabilities of 1-bit-differentials in a 16-bit block cipher.
It generates 16-bit numbers, which contain one of four certain number patterns, puts them through an S-box layer and a transposition layer and finally finds 
one of the four patterns again to count how many times a certain pattern results in another one (the differentials).
For now everything within the script is fixed, but might be set up for a more general use in the future.
