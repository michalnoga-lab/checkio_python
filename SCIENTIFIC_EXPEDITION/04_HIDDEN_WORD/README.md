
JABBERWOCKY

'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

'Beware the Jabberwock, my son!
The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
The frumious Bandersnatch!'

He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.

And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!

One, two! One, two! And through and through
The vorpal blade went snicker-snack!
He left it dead, and with its head
He went galumphing back.

'And hast thou slain the Jabberwock?
Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!'
He chortled in his joy.

'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

"Through the Looking-Glass." Lewis Carroll

DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?

"Puzzles from Wonderland." Lewis Carroll

Nicola has solved this puzzle (and I am sure that you will do equally well). To be prepared for more such puzzles, Nicola wants to invent a method to search for words inside poetry. You can help him create a function to search for certain words.

You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n). Casing does not matter for your search, but whitespaces should be removed before your search. You should find the word inside the rhyme in the horizontal (from left to right) or vertical (from up to down) lines. For this you need envision the rhyme as a matrix (2D array). Find the coordinates of the word in the cut rhyme (without whitespaces).

The result must be represented as a list -- [row_start,column_start,row_end,column_end] , where

    row_start is the line number for the first letter of the word.
    column_start is the column number for the first letter of the word.
    row_end is the line number for the last letter of the word.
    column_end is the column number for the last letter of the word.
    Counting of the rows and columns start from 1.

rhymes

Input: Two arguments. A rhyme as a string and a word as a string (lowercase).

Output: The coordinates of the word.

Example:
checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
    
1
2
3
4
5
6
7
8
9
10
11
12
13

How it is used: This task shows the variance of the positional ciphers. With this cipher you can hide a message within a book which allows you and receiver to send these coded messages.

Precondition: The word is given in lowercase
0 < |word| < 10
0 < |rhyme| < 300 