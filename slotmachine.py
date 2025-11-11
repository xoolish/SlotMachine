import random

class Slotmachine:
    def __init__(self):
        self.symbols=["🍉","🍊","🍋","🍓","🍒","🍍"]
        self.payouts={"🍉":10,
                      "🍊":7,
                      "🍋":6,
                      "🍓":5,
                      "🍒":4,
                      "🍍":3
                      }


    def spin(self,rows=3,cols=3):

         return [[random.choice(self.symbols) for i in range(rows)] for i in range(cols)]

    def printgrid(self,grid):
           for i in grid:
              print("|".join(i))

    def cashout_row(self,row,bet):
               if not row:
                   return 0
               if all(s==row[0] for s in row):
                   symbol=row[0]
                   multiplier=self.payouts.get(symbol)
                   return bet * multiplier
               return 0



    def cashout_grid(self, grid, bet):
        total = 0
        for row in grid:
            win = self.cashout_row(row, bet)
            if win > 0:
                total += win
        return total

def player():
    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    print("WELCOME TO MY SLOTMACHINE GAME")
    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    balance=int(input("deposit an amount: "))
    print(f"balance:${balance}")
    print("symbols:🍉 🍊 🍋 🍓 🍒 🍍")
    machine=Slotmachine()
    spin_again=True
    while spin_again:
        try:
           bet=int(input("enter amount to bet: "))
        except ValueError:
            print("please enter a valid amount")
            continue

        if bet > balance:
            print("OOPS😪 INSUFFICIENT AMOUNT")
            continue
        else:
             balance-=bet
             print(f"current_balance:${balance}")
             grid=machine.spin(rows=3,cols=3)
             machine.printgrid(grid)
             total_win=machine.cashout_grid(grid,bet)

             if total_win > 0:
                  print(f"you won ${total_win} naira.😍")
                  balance+=total_win
                  print(f"current_balance:${balance}")
             else:
                  print("you lose😢")
                  balance-=total_win
                  print(f"current balance:${balance}")
                  print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
             while True:
              spin_again=input("do you want to spin again? y/n :").lower()
              if spin_again=="y":
                  print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                  print("WELCOME BACK!🤩")
                  print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
                  break
              elif  spin_again=="n":
                  spin_again=False

                  break
              else:
                  print("Please Select a valid option (y/n)")
    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    print("THANKS FOR PLAYING❤")
    print(f"you can take your balance of: ${balance}")
    print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")

player()






