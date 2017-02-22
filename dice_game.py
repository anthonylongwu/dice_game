from random import randint

def dice_1():
  x = randint(1,6)
  return x

def dice_2():
  y = randint(1,6)
  return y

game = 0

while game < 5:
  print "Please type roll to roll the die"
  ans = raw_input()

  if ans == "roll":
    first_dice = dice_1()
    second_dice = dice_2()

    total = first_dice + second_dice
    game += 1

    print "dice 1 rolled %s" % first_dice
    print "dice 2 rolled %s" % second_dice
    print "your total is {}".format(total)

    if total == 7:
      print "lucky 7!"
    elif total == 2:
      print "snake eyes!"
    elif first_dice == 4 and second_dice == 5:
      print ".45 to the chest!"
    elif first_dice == 4 and second_dice == 4:
      print "My .44 make sure all yo kids don't grow!"
    elif first_dice == 2 and second_dice == 2:
      print "Deuce Deuce! Pew! Pew!"
    elif first_dice == 2 and second_dice == 3:
      print "Jordan!"

    else:
      print "Please type roll"

    if game == 5:
      print "thank you for playing"










