# Fulvo

Fulvo es un lenguaje de programacion orientado a la redonda. Como el lenguaje esta basado en futbol, funciona con terimnos plenamente futbolisticos.

## Como utilizarlo

Para utilizar el lenguaje segui los siguientes pasos:

Primero, clona el repositorio en una carpeta
  ```bash
  git clone https://github.com/igorriti/Fulvo.git .
  ```
Segundo, abri tu consola e ingresa alguno de los siguientes comandos:
  ```bash
      python shell.py
  ```
Con el comando abriras la consola y podras codear sobre la misma, si queres usar
  ```bash
      python shell.py ./NombreDeArchivo.gol
  ```
 
 ## Sintaxis
 
 En fulvo vos no declaras variables, declaras Jugadores
 
  ```bash
     Jugador (Aca va el nombre de tu Jugador) = (valor)
     
     Ejemplo:
     Jugador Diego = 10
     Jugador Messi = "El mejor del mundo"
  ```
 
Para jugar a la pelotita en fulvo podes usar las siguientes operaciones
 
  ```bash
     +
     -
     *
     /
     ^
     ""
     []
     
     Ejemplos
     
     9 + 12 ---> 21
     7 - 0 ---> 7
     
     "DIOS" * 10 ---> "D10SD10SD10SD10SD10SD10SD10SD10SD10SD10S"
     
     Si tenes a los jugadores Messi, Ronaldo y Neymar declarados podes hacer una lista de ellos asi
     [Messi,Ronaldo,Neymar]
     Queres sumar a Suarez?
     [Messi,Ronaldo,Neymar] + Suarez ---> [Messi,Ronaldo,Neymar,Suarez]
   ```
 
Las condiciones en fulvo son las siguientes
   ```bash
     == ---> si dos Jugadores son iguales
     != ---> si dos Jugadores no son iguales
     < ---> si un Jugador es menos que otro
     <= ---> si un Jugador es menos o igual que otro
     > ---> si un jugador es mas que otro
     >= ---> si un jugador es mas o igual que otro
   ```

