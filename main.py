# main.py
import random
import time
input("Welcome to the game of War! In this game, the deck will be cut in half and each player will receive one. Your goal is to get the most hands! The values of the Jack, Queen, and King are each worth 10, and the Ace is worth 1.\n\nEach player will put their cards faced down and flip one card at the same time. The player that has the higher card gets theirs and the opponent's card. If both players flip a card worth the same amount each player will lay 3 cards from their deck faced down on the table and flip the fourth card up. When they flip the fourth card they will say WAR and the player with the highest card will take all of the cards on the table. Whoever ends up with the most hands by the end of the rounds wins!\n\nPress Enter to start playing.\n")
cards = {11:"Jack", 12:"Queen", 13:"King", 1:"Ace"}

player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")

numrounds = 10
score1 = 0
score2 = 0

for i in range(1, numrounds+1):
  print("Round " + str(i) + ":")

  card1 = random.randint(1,13)
  card2 = random.randint(1,13)

  time.sleep(0.5)
  if card1 < 11 and card1 != 1:
    print(player1 + "'s card: " + str(card1))
  else:
    print(player1 + "'s card: " + cards[card1])
  time.sleep(0.5)
  if card2 < 11 and card2 != 1:
    print(player2 + "'s card: " + str(card2))
  else:
    print(player2 + "'s card: " + cards[card2])
  time.sleep(1)

  if card1 > card2:
    print(player1 + " wins this hand!\n")
    score1 += 1
  elif card2 > card1:
    print(player2 + " wins this hand!\n")
    score2 += 1
  else:
    print("3...")
    time.sleep(0.5)
    print("2...")
    time.sleep(0.5)
    print("1...")
    time.sleep(0.5)
    print("WAR!")
    time.sleep(0.5)
    print(card1)
    print(card2)
    time.sleep(1)
    if card1 > card2:
      print(player1 + " wins WAR.")
      score1 += 1
    elif card1 < card2:
      print(player2 + " wins WAR.")
      score2 += 1
    else:
      print("This round was a tie!")

print("Final scores:")
print(player1 + ": " + str(score1))
print(player2 + ": " + str(score2))

if score1 > score2:
  print(player1 + " wins this game!")
elif score1 < score2:
  print(player2 + " wins this game!")
else:
 print("The game was a tie!")
