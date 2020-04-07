import os, sys
from time import sleep

def boost():
    ip = str(input("\033[1;32m[\033[1;33m+\033[1;32m]\033[1;35m your IP\033[1;31m (\033[1;37mifconfig\033[1;31m): \033[1;36m"))
    print ("\033[1;32m[\033[1;33m+\033[1;32m]\033[1;35m wait ...")
    sleep(2)
    response = os.system('ping -c 1 '+ip)
    if response == 0:
       print ("\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;38mConnections is UP!")
    else:
       sys.exit("\033[1;32m[\033[1;31mx\033[1;32m]\033[1;38mConnections is Down!")

def logo():
  print ("""\033[1;36m
                                                  
                 `...--------...`                 
             `.--------------------.`             
          `.--------------------------.`          
\033[1;37m         .------------------------------.         
       `-----:s:-----..````..------s:-----`       
      .------+m+:-.` `..--..` `.--/mo:-----.      
     .-------+m+::..:-.````.-:..:-/mo:::----`     
    `--------+m+::::-`.-::-.`-::::/mo:::::---`    
    .--------+m+:::::::-  -:::::::+mo:::::::-.    
    ---------+m+::::::::--::::::::+mo:::::::::    
    ------+++oyooooooooooooooooooooysooo::::::    
    -----:mmmmmysydmmmmmmmmmmmmmmmmmmmmm/:::::    
    .----:mmmmyood/mmmssddssmhshmysdmmmm/::::-    
    `----:mmmmmyssmmmmmmmmmmmmmmmmmmmmmm/::::`    
     `----ooyyyyyooooooooooooooooyyyyyoo::::.     
\033[1;33m      .-----/+++/::::::::::::::::/+++/:::::.      
       `------::::::::::::::::::::::::::::.       
         .------::::::::::::::::::::::::-         
           .------::::::::::::::::::::.`          
             `.-----:::::::::::::::-`             
          \033[1;32m       `...-:::::::--.``                

         \033[1;30mTingkatkan koneksimu sekarang juga
\t\t  \033[1;32mCode \033[1;36mby \033[1;31mK\033[1;32mh\033[1;33ma\033[1;34mz\033[1;35mu\033[1;36ml
                                              """)


if __name__=="__main__":
   os.system('clear')
   logo();boost()
