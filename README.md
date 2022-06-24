# Fulvo

Fulvo es un lenguaje de programacion orientado a la redonda. Como el lenguaje esta basado en futbol, funciona con terminos plenamente futbolisticos.

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
 
Las condiciones y combinacion de Jugadores en fulvo son las siguientes
```bash
 == ---> si dos Jugadores son iguales
 != ---> si dos Jugadores no son iguales
 < ---> si un Jugador es menos que otro
 <= ---> si un Jugador es menos o igual que otro
 > ---> si un jugador es mas que otro
 >= ---> si un jugador es mas o igual que otro
 y ---> &&
 o ---> ||
 no ---> !
 ``` 
 
 La sentencia IF, los bucles en fulvo son los siguientes
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
 
Las condiciones y combinacion de Jugadores en fulvo son las siguientes
   ```bash
 == ---> si dos Jugadores son iguales
 != ---> si dos Jugadores no son iguales
 < ---> si un Jugador es menos que otro
 <= ---> si un Jugador es menos o igual que otro
 > ---> si un jugador es mas que otro
 >= ---> si un jugador es mas o igual que otro
 y ---> &&
 o ---> ||
 no ---> !
   ```
 No exiten funciones, aca en Fulvo le decimos jugadas
```bash
jugada ---> Function
gol ---> End (Fundamental que todas las jugadas terminen en gol)
devuelve ---> Return
gambetea ---> Continue
falta ---> Break
```
 
 Para que cada partido salga de la mejor forma te facilitamos un par de funciones y constantes para que uses:
  ```bash
//FUNCIONES
   Relatar() ---> Imprimir por pantalla
   Relatar_ret() ---> Imprimir por pantalla el retorno
   Poner() ---> Input
   Poner_numero() ---> Input number
   Despejar() ---> Clear consola
   Salimoss() ---> Clear consola
   Es_Numero(a) ---> Chequea si 'a' es numero
   Es_String(a) ---> Chequea si 'a' es String
   Es_Lista(a) ---> Chequea si  'a' es lista
   Es_Jugada(a) ---> Chequea si 'a' es jugada
   Agregar(a,b) ---> Agrega el elemento 'b' a la lista 'a'
   Sacar(a,b) ---> Saca elemento del indice 'b' a la lista a
   Extender(a,b) --->  Le extiende una lista a otra
   Longitud(a) ---> Te dice la longitud de 'a'
   Arrancar_Partido() ---> Se arranca el partido papaaa
   Historico() ---> Mi favorito, probalo.
   Hacer_Tiempo(a) ---> La de Mourinho, hace tiempo por a segundos
   Cabezaso() ---> No lo hagas.
   Ankara() ---> Probalo
   Bicho() ---> Probalo
   Esto_Es_Boca(a) ---> Probalo, ojo con lo que pones.
   River() ---> Probalo.
   Lesionar(a) ---> Intenta lesionar un jugador /Esta en desarrollo
   Boca() ---> //Esta en desarrollo

//CONSTANTES
  NULL ---> 0
  FALSE ---> 0
  TRUE ---> 0
  MATH_PI ---> PI
  ROJA ---> 0
  D10S ---> Maradona
  GOAT ---> Messi
  LA_PLATA ---> Probala.
  MADRID ---> Probala.
  QATAR ---> Probala.
  Gano_San_Marino ---> Ya sabes el resultado.
  Dias_Sin_Quilombo_En_Boca ---> Fijate vos...
  SELECCION_ARGENTINA ---> Probala.
  ```
## Advertencia

No busco generar bardo ni debate futbolistico, no se tomen a pecho todo. Lo unico que es indiscutible es que Maradona es mas grande que Pele.

##Sobre el desarrollo
Desarrolle este lenguaje para profundizar mi conocimiento en Python y divertime en el proceso. Cualquier sugerencia, ayuda o comentario es mas que bienvenido!

## Creditos
El desarrollo de Fulvo fue gracias a CodePulse y su excelente [tutorial](https://www.youtube.com/watch?v=Eythq9848Fg&list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD)

