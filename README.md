## Pygame Connect 4

Built using pygame and featuring a vintage, hand-drawn motif, this gem relaxes and lulls - grab a cup of coffee and a buddy and while the morning away to the smooth sound and gentle rhythm of this chic take on the classic Connect 4.

### The logic of the game

I build the logic part of this game first because at first I build a python command line text-based Tic-tac-toe game first. However, I found the logic I used behind this game is not very universal. Because I only use a one-dimensional list to represent each "slot" on the Tic-tac-toe grid. After I learned Matrix Multiplication, I was thinking about using a two-dimensional matrix to represent the slots, that is, to build a 7x6 two-dimensional list. And here comes the connect 4 game.
```
game_record = [[" ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " "]]
```

The win check part is very interesting. I didn't have any difficulty to check the 4 gems connecting horizontally, vertically and diagonally up. But when I wanted to use the same logic to check whether one player have made 4 connecting gems diagonally down, the command line kept telling me "Index out of range". The reason is that at first, I tried to game_record[i][j] == game_record[i+1][j-1] == game_record[i+2][j-2] == game_record[i+3][j-3]". If I do that, the range of j will not be able to match the range I use for other win check. I reached an epiphany of having j+3, j+2, j+1 and j instead of the method I used above. Yay! Now the iterating index finally matched!

```
for i in range(4):
        for j in range(3):
            if game_record[i][j].name == game_record[i+1][j].name == game_record[i+2][j].name == game_record[i+3][j].name and game_record[i][j].name != "nothing":
                self.win_marker = 1
                self.winning_location = location_record[i][j]
                return True
                break
            elif game_record[i][j].name == game_record[i][j+1].name == game_record[i][j+2].name == game_record[i][j+3].name and game_record[i][j].name != "nothing":
                self.win_marker = 2
                self.winning_location = location_record[i][j+3]
                return True
                break
            elif game_record[i][j].name == game_record[i+1][j+1].name == game_record[i+2][j+2].name == game_record[i+3][j+3].name and game_record[i][j].name != "nothing":
                self.win_marker = 4
                self.winning_location = location_record[i][j+3]
                return True
                break
            elif game_record[i][j+3].name == game_record[i+1][j+2].name == game_record[i+2][j+1].name == game_record[i+3][j].name and game_record[i][j+3].name != "nothing":
                self.win_marker = 3
                self.winning_location = location_record[i][j+3]
                return True
                break
            else:
                continue
```

### Made it real!
I made the game in the command line first. And I can't wait to make it real (with pictures and music). Pygame is a great platform to make this dream come true.

The procedure of the game is three loops: the first loop is player 1 making a move; the second one is player 2 making a move. Within each loop, there are two little loops: the first little loop is movement detection, while the second little loop is the actual move and the win check. Since Pygame keep looping through and rendering the pictures (at a frequency of 60 times per second!), it doesn't wait for me to make a move. So I have to use separate little loops. I was thinking about whether there would be a better solution. Maybe I can use a if statement to pause the move and make the computer wait for me to make a move. After I successfully made the first gem rendered, everything went much more smoothly.
