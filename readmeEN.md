# fulvo

Fulvo is a round-oriented programming language. As the language is based on football, it works with fully football terms.

## How to use

To use the language follow these steps:

First, clone the repository to a folder
  ```bash
  git clone https://github.com/igorriti/Fulvo.git .
  ```
Second, open your console and enter one of the following commands:
  ```bash
  python shell.py
  ```
With the command you will open the console and you can code on it, if you want to use
  ```bash
  python shell.py ./FileName.gol
  ```
 
 ## Syntax
 
 In fulvo you don't declare variables, you declare Players
 
  ```bash
 Jugador (Here goes the name of your Player) = (value)

 Example:
 Jugador Diego = 10
 Jugador Messi = "The best in the world"
  ```
 
To play the ball in fulvo you can use the following operations
 
  ```bash
 +
 -
 *
 /
 ^
 ""
 []

 examples

 9 + 12 ---> 21
 7 - 0 ---> 7

 "GOD" * 10 ---> "D10SD10SD10SD10SD10SD10SD10SD10SD10SD10S"

 If you have the players Messi, Ronaldo and Neymar declared, you can make a list of them like this
 [Messi, Ronaldo, Neymar]
 Do you want to add Suarez?
 [Messi,Ronaldo,Neymar] + Suarez ---> [Messi,Ronaldo,Neymar,Suarez]
   ```
 
The conditions and combination of Players in fulvo are the following
```bash
 == ---> if two Players are equal
 != ---> if two Players are not equal
 < ---> if a Player is less than another
 <= ---> if a Player is less than or equal to another
 > ---> if one player is more than another
 >= ---> if a player is more or equal to another
 and ---> &&
 or ---> ||
 not ---> !
 ```
 
 The IF statement, the loops in fulvo are as follows
  ```bash
 si ---> IF
 patea ---> THEN
 palo ---> ELSE
 rebote ---> ELIF
 ArrancaPorLaDerecha --> FOR
 hasta ---> TO
 pasala ---> STEP
 mientras ---> WHILE
   ```
 
The conditions and combination of Players in fulvo are the following
   ```bash
 == ---> if two Players are equal
 != ---> if two Players are not equal
 < ---> if a Player is less than another
 <= ---> if a Player is less than or equal to another
 > ---> if one player is more than another
 >= ---> if a player is more or equal to another
 and ---> &&
 or ---> ||
 not ---> !
   ```
 There are no functions, here in Fulvo we tell you plays
```bash
jugada ---> Function
gol ---> End (It is essential that all plays end in a goal)
devuelve ---> return
gambetea ---> Continue
falta ---> break
```
 
 So that each game goes in the best way, we provide you with a couple of functions and constants for you to use:
  ```bash
//FUNCTIONS
   Relatar() ---> Print to screen
   Relatar_ret() ---> Print the return to the screen
   Poner() ---> Input
   Poner_numero() ---> Input number
   Despejar() ---> Clear console
   Salimoss() ---> Clear console
   Es_Numero(a) --->  Check if 'a' is a number
   Es_String(a) ---> Check if 'a' is a String
   Es_Lista(a) ---> Check if 'a' is a list
   Es_Jugada(a) ---> Check if 'a' is a function
   Agregar(a,b) ---> Add item 'b' to list 'a'
   Sacar(a,b) ---> Get element from index 'b' to list a
   Extender(a,b) --->  Extends one list to another
   Longitud(a) ---> Tells you the length of 'a'
   Arrancar_Partido() ---> The game is started
   Historico() ---> My favorite, try it.
   Hacer_Tiempo(a) ---> Mourinho's, makes time by seconds
   Cabezaso() ---> Dont!
   Ankara() ---> Try it.
   Bicho() ---> Try it.
   Esto_Es_Boca(a) --->  Try it.
   River() --->  Try it.


//CONSTANTS
  NULL ---> 0
  FALSE ---> 0
  TRUE ---> 0
  MATH_PI ---> PI
  ROJA ---> 0
  D10S ---> Maradona
  GOAT ---> Messi
  LA_PLATA --->  Try it.
  MADRID ---> Try it.
  QATAR --->  Try it.
  Gano_San_Marino --->  Try it.
  Dias_Sin_Quilombo_En_Boca --->  Try it.
  SELECCION_ARGENTINA --->  Try it.
  ```
## Caveat

I'm not looking to generate bard or football debate, don't take everything to heart. The only thing that is indisputable is that Maradona is bigger than Pele.

## About development
I developed this language to deepen my understanding of Python and have fun in the process. Any suggestion, help or comment is more than welcome!

## Credits
Fulvo development was thanks to CodePulse and his excellent [tutorial](https://www.youtube.com/watch?v=Eythq9848Fg&list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD)
