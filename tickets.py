
import os
# declare dictionary movie
moviename = {'movie1': 'Kubo And The Two Strings', 'movie2': 'Suicide Squad', 'movie3': 'Lights Out','movie4': 'Train To Busan', 'movie5': 'One Piece Film:Gold'}
movietime = {'time1': '2:00 pm', 'time2': '4:30 pm', 'time3': '7:00 pm', 'time4': '9:30 pm', 'time5': '12:00 am'}
movcode1 = ['movie1', 'movie2', 'movie3', 'movie4', 'movie5']
movcode2 = ['time1', 'time2', 'time3', 'time4', 'time5']
cont = 'y'
j = 0
ch = 'y'
list1 = []
list2 = []
tseat = 0
nseat = 0
while ch == 'y' or ch == 'Y':
  print "\n||||||||||||||||||||||||||||||||"
  print "||| WELCOME TO  CINEMA |||"
  print "||||||||||||||||||||||||||||||||"
  raw_input("\nPress ENTER to proceed...")
  name = raw_input("\nPlease enter your name: ")
  print "\n##############################"
  print "\n#          MAIN MENU         #"
  print "\n#----------------------------#"
  print "\n# List Movie & Buy Ticket #"
  print "\n##############################"
  o = 1
  if o == 1:
    print "\n---------------------------------------------------------------------------"
    raw_input("\nPress ENTER to continue. The program will open up movie selection list, please wait.")
    print"\n---------------------------------------------------------------------------"
    if tseat > 100:
      print 'No seats left '
      ch = 'n'
    for i, j in moviename.items():
      print i, '=', j
    for i, j in movietime.items():
      print i, '=', j
    movtitle = raw_input("Enter the movie no:")
    time = raw_input("Enter the time no:")
    print "\n\nMovie name: ", moviename[movtitle]
    print "\nScreening time : ", movietime[time]
    os.system('cls')
    print "\n---------------------------------------------------------------------------"
    print "Diamond Circle (Adult=20)(Children=15) \nGold Circle(Adult=12)(Children=10)"
    noadult = int(raw_input("\nPlease enter amount of tickets for adult: "))
    nochildren = int(raw_input("\nPlease enter amount of tickets for children: "))
    nseat = noadult + nochildren
    print 'Enter which seat(1-Diamond Circle,2-Gold Circle)(max seat 1 person can book is 20):'
    n = input()
    if (n == 1):
      for i in range(1, nseat + 1):
        print 'The seats are:', i
        j = i
    else:
      for i in range(1, nseat + 1):
        print 'The seats are:', i
        j = i
    for k in range(50):
      list1.append(k)
      list2.append(k)
    for i in range(j, nseat + 1):
      if n == 1:
        del (list1[i])
      else:
        del (list2[i])
    tseat += nseat
    print "\n---------------------------------------------------------------------------"
    raw_input("\n\nPress ENTER to continue, the program will display your Price")
    print "\n---------------------------------------------------------------------------"
    # calculate total price
    if (n == 1):
      totprice = (noadult * 20.00) + (nochildren * 15.00)
      gst = totprice * 0.06
      realprice = totprice * 1.06
      print "\n\nMovie name: ", moviename[movtitle]
      print "\nScreening time : ", movietime[time]
      print 'Name:', name, 'Price:', realprice, 'GST', gst
    else:
      totprice = (noadult * 12.00) + (nochildren * 10.00)
      gst = totprice * 0.06
      realprice = totprice * 1.06
      print "\n\nMovie name: ", moviename[movtitle]
      print "\nScreening time : ", movietime[time]
      print 'Name:', name, 'Price:', realprice, 'GST:', gst
    ch = raw_input("Enter y or Y to book another ticket:")
print "\n-----------------------------------------"
print "\nThank You! Enjoy Your movie!"
print "\n-----------------------------------------\n"
print "\n======================================"
print "\n== Thank you for using this system. =="
print "\n======================================"
raw_input('\n\nPress ENTER to exit program...')
