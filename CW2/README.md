Z1. Napisz program, w który generuje 5 liczb pseudolosowych z przedziału od 1 do 100.

Z2. Napisz program, ktory wczytuje trzy liczby. Wydrukować wartość najwiekszą i
najmniejszą.

Z3. Napisz program, który dla trzech liczb a, b i c wprowadzonych z klawiatury sprawdza,
czy są to trójki pitagorejskie. Dodatkowo należy założyć, że a > 0, b > 0 i c > 0.

Z4. Napisz program, który oblicza pierwiastki równania kwadratowego $ax^2+bx+c=0$,
gdzie zmienne a, b, c to liczby rzeczywiste wprowadzane z klawiatury. Dla zmiennych
a, b, c, x1 oraz x2 należy przyjąć format wyswietlania ich na ekranie z dokładnością do
dwóch miejsc po kropce.

Z5. Napisz program, który za pomocą instrukcji while dla danych wartości x rosnacych od
0 do 10 oblicza wartość funkcji $y=3x$

Z6. Napisz program wyswietlajacy tabliczke mnożenia dla liczb od 1 do 100 z 
wykorzystaniem podwójnej pętli for.

Z7. Wiedząc, ze $1233=12^2+33^2$, napisz program, który znajduje wszystkie 
liczby z przedziału od 1000 do 9999 spełniające taką ciekawą zależność. 
Program dodatkowo liczy, ile ich jest.

Z8. Dla ciągu: $a_0=1,a_1=2,a_n=3a_{n-1}+a_{n-2}$, znaleźć i wydrukować najmniejszy wyraz większy od wczytanej wartości k.

Z9. Dla danego x drukować kolejne przybliżenia $\sin(x)$, aż wyznaczany wyraz 
szeregu co do modułu będzie mniejszy od danej dokładności eps.
$$\sin(x)=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots=\sum_{i=0}^\infty(-1)^i\frac{x^{2i+2}}{(2i+1)!}$$

Z10. Liczby Catalana to ciąg, który można wyrazić wzorem rekurencyjnym
$$C_0=1$$
$$C_{n+1}=\frac{4n+2}{n+2}C_n$$
Napisz program, który wypisuje wszystkie liczby Catalana mniejsze od miliona i podaje ile jest wśród nich 
liczb parzystych i nieparzystych.

ZD2. Dla $x=\\{0.1,0.2,\ldots,1\\}$ i wczytanych z klawiatury $k$ wartości $y$ drukować argumenty i wartości funkcji:

$$f(x,y)=\begin{cases}\begin{array}{lr}
\displaystyle\sum_{i=1}^{10}\frac{(x+y)^i}{i!},&\mbox{gdy}\sin(x)>\cos(y)\\
x^5+x^3y^2+y^4,& \mbox{w}\ p.p
\end{array}
\end{cases}$$
