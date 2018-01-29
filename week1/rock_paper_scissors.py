print "Player 1, make your move: (rock/paper/scissors)"
player1 = raw_input()
print "Player 2, make your move: (rock/paper/scissors)"
player2 = raw_input()

if player1 == player2:
    print "Tie game."
elif  player1 == "rock" and player2 == "scissors" \
    or player1 == "paper" and player2 == "rock" \
    or player1 == "scissors" and player2 == "paper":
    print "Player 1 wins."
else:
    print "Player 2 wins."
