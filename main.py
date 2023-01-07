"""
Stwórz program. który na podstawie

tabeli  wartości inflacji
oprocentowania kredytu.
kwoty początkowej kredytu
stałej wartości raty

wyliczy wartość zadłużenia w każdym miesiącu przez 2 nadchodzące lata.

Niech program wydrukuje dla każdego miesiąca następującą linię:
Twoja pozostała kwota kredytu to X. to Y mniej niż w poprzednim miesiącu.

Napisz program tak. by wysokość początkowego kredytu. oprocentowanie kredytu
(ponad inflację) i kwota raty były pobierane ze
standardowego wejścia (terminal).

Przykładowe wartości kredytu i formułę do jego wyliczenia znajdziesz w
załączniku powyżej. Skopiuj z niego wartości inflacji dla każdego miesiąca.

Wyślij link do swojego repozytorium (nie spakowany kod). Repozytorium
powinno zawierać więcej. niż jeden commit.

Notes
  -wypisać wartości dla kolejnych 24 miesięcy
  -pobierac z input :  -Oprocentowanie .
                       -Kwotę początkową .
                       -Stałą wartość raty
  -(1+((B3+3)/1200))*C2-200
  -(1+((aktualna inflacja+oprocentowanie)/1200))*poprzednia wartość pożyczki-Kwota raty


  1. Wprowadzenie danych z input
   -oporcentowanie
   -kwota początkowa
   -kwota raty
  2. Zrzutowanie danych z inputu za pomocą float
  3. Pierwszy miesiąc
    -wez kwotę początkową pożyczki do zmiennej poprzednia wartość pożyczki
    -wez aktualną inflacje do zmiennej aktualna inflacja
    -wylicz i zapisz wartośc kredytu do spłaty do zmiennej pozostała wartośc kredytu

  4. Kolejne miesiące
    -wez poprzednią wartośc pożyczki do zmiennej poprzednia wartość pożyczki
    -wez aktualna inflacje do zmiennej aktualna inflacja
    -wylicz i zapisz wartośc kredytu do spłaty do zmiennej pozostała wartośc kredytu
    -wylicz i zapisz rożnicę pomiędzy
                      pozostała wartośc kredytu
                      a
                      poprzednia wartosć pożyczki
"""
szablon_podsumowania = "{} Twoja pozostała kwota kredytu to {}." \
                       " to {} mniej niż w poprzednim miesiącu."
oprocentowanie = float(input('Podaj Oprocentowanie Kredytu: '))
kwota_poczatkowa = float(input('Podaj Kwotę Początkową Kredytu: '))
kwota_raty = float(input('Podaj Kwotę Raty Kredytu: '))

szablon = "Kredyt na {} PLN. Oprocentowany {}%.Kwota Raty {} PLN"
informacje_o_kredycie = f"Kredyt na {kwota_poczatkowa} PLN. " \
                        f"Oprocentowany {oprocentowanie} %. " \
                        f"Kwota Raty {kwota_raty} PLN. "
print(informacje_o_kredycie)

# Styczeń 2022
miesiac = "W Styczniu 2022"
poprzednia_wartość_pozyczki = kwota_poczatkowa
aktualna_inflacja = 1.5928244844
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))

# Luty 2022
miesiac = "W Lutym 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = -0.4535091012
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Marzec 2022

miesiac = "W Marcu 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 2.3246717171
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Kwieceiń 2022

miesiac = "W Kwietniu 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.2612544072
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Maj 2022

miesiac = "W Maju 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.7825262857
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Czerwiec 2022

miesiac = "W Czerwcu 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 2.3293845415
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Lipiec 2022

miesiac = "W Lipcu 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.5022298422
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Sierpień 2022

miesiac = "W Sierpniu 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.7825262857
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Wrzesień 2022

miesiac = "We Wrzesniu 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 2.3288489941
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Pażdziernik 2022

miesiac = "W Pazdzierniku 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 0.6169213482
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Listopad 2022

miesiac = "W Listopadzie 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 2.3522958864
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Grudzień 2022

miesiac = "W Grudniu 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 0.3377795452
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
#-------------------
# Styczeń 2023

miesiac = "W Styczniu 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.5770352473
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))

# Luty 2023

miesiac = "W Lutym 2022"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = -0.2927814426
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Marzec 2023

miesiac = "W Marcu 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 2.4861965902
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Kwieceiń 2023

miesiac = "W Kwietniu 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 0.2671103178
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Maj 2023

miesiac = "W Maju 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.4179526723
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Czerwiec 2023

miesiac = "W Czerwcu 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.0542432673
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Lipiec 2023

miesiac = "W Lipcu 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.4805201045
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Sierpień 2023

miesiac = "W Sierpniu 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.5770352473
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Wrzesień 2023

miesiac = "We Wrzesniu 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = -0.0774206903
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Pażdziernik 2023

miesiac = "W Pazdzierniku 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.1657333987
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Listopad 2023

miesiac = "W Listopadzie 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = -0.4041867176
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
# Grudzień 2023

miesiac = "W Grudniu 2023"
poprzednia_wartość_pozyczki = nowa_wartosc_pozyczki
aktualna_inflacja = 1.4997085208
nowa_wartosc_pozyczki = (1 +((aktualna_inflacja + oprocentowanie) / 1200)) \
                        * poprzednia_wartość_pozyczki - kwota_raty
nowa_wartosc_pozyczki = round(nowa_wartosc_pozyczki, 5)
roznica_w_kredycie = poprzednia_wartość_pozyczki - nowa_wartosc_pozyczki
print(szablon_podsumowania.format(miesiac, nowa_wartosc_pozyczki, roznica_w_kredycie))
























