# Search for Word

Given a 2-D grid of characters `board` and a string `word`, return `True` if the word is present in the grid, otherwise return `False`.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/7c1fcf82-71c8-4750-3ddd-4ab6a666a500/public)

```
Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: True
```

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/79721392-44b6-4de7-c571-d3d1640ac100/public)

```
Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: False
```

Constraints:

 * `board` will be between 1x1 and 5x5
 * `1 <= len(word) <= 10`
 * `board` and `word` consists of only lowercase and uppercase English letters.
