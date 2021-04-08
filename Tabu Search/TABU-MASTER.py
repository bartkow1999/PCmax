import time
import math

def algorytm_poczatkowy(m, zadania):
    procesory = [[] for _ in range(m)]
    for zadanie in sorted(zadania, reverse=True):
        zsumowane = list(sum(proc) for proc in procesory)
        procesory[zsumowane.index(min(zsumowane))].append(zadanie)
    zsumowane = list(sum(proc) for proc in procesory)
    Cmax = max(zsumowane)
    return Cmax, procesory, zsumowane, sorted(zadania, reverse=True)

def znajdz_najlepsza_wymiane(proc1, proc2, proc1_zsumowany, proc2_zsumowany):
    '''
    Zwraca które zadanie najopłacalniej wymienić oraz indexy tych zadań na procesorach
    '''
    proc1 = proc1[:]
    proc2 = proc2[:]
    proc1_poczatkowy = proc1_zsumowany
    proc2_poczatkowy = proc2_zsumowany
    for i in range(len(proc1)):
        for j in range(len(proc2)):
            zadanie1 = proc1.pop(i)
            zadanie2 = proc2.pop(j)
            proc1.insert(i, zadanie2)
            proc2.insert(j, zadanie1)
            a = proc1_poczatkowy - zadanie1 + zadanie2
            b = proc2_poczatkowy - zadanie2 + zadanie1
            if abs(a - b) < abs(proc1_zsumowany - proc2_zsumowany):
                proc1_zsumowany = a
                proc2_zsumowany = b
                x = zadanie1
                y = zadanie2
                index_x = i
                index_y = j
            zadanie1 = proc1.pop(i)
            zadanie2 = proc2.pop(j)
            proc1.insert(i, zadanie2)
            proc2.insert(j, zadanie1)
    try:
        return x, y, index_x, index_y
    except UnboundLocalError:
        return -1

def najwieksza_roznica(zsumowane):
    '''
    Zwraca listę największych różnic między czasami na procesorach
    '''
    lista_par = []
    for i in range(len(zsumowane) - 1):
        for j in range(i + 1, len(zsumowane)):
            lista_par.append([i, j, abs(zsumowane[i] - zsumowane[j])])
    lista_par = sorted(lista_par, key=lambda t: t[2], reverse=True)
    lista_par = [para[:2] for para in lista_par]
    return lista_par

def znajdz_pare_do_wymiany(zsumowane, tabu_list):
    """
    Zwraca indeksy dwóch procesorów, które mają największą różnicę czasu zadań i nie są na liście tabu
    """
    lista_par = najwieksza_roznica(zsumowane)
    tabu_list2 = [tabu[:2] for tabu in tabu_list]
    first_index = lista_par[0][0]
    second_index = lista_par[0][1]
    c = 1
    while ([first_index, second_index] in tabu_list2):
        try:
            first_index = lista_par[c][0]
            second_index = lista_par[c][1]
            c += 1
        except Exception:
            return -1
    return first_index, second_index

def zamien_elementy(procesory_first, index_first_elem, procesory_second, index_second_elem):
    """
    Zamienia elementy między dwoma procesorami i sortuje je malejąco
    """
    a = procesory_first.pop(index_first_elem)
    b = procesory_second.pop(index_second_elem)
    procesory_second.append(a)
    procesory_first.append(b)
    procesory_first.sort(reverse=True)
    procesory_second.sort(reverse=True)
    return procesory_first, procesory_second

def dodaj_do_listy_tabu(first_index, second_index, t, tabu_list):
    tabu_list.append([first_index, second_index, t])
    tabu_list.append([second_index, first_index, t])
    return tabu_list

def zmniejsz_i_usun_z_tabu(tabu_list, first_index, second_index):
    '''
    Usuwa z listy tabu wszystkie elementy zawierające procesory, które uległy właśnie wymianie oraz zmniejsza pozostałe
    o krok czasu = 1
    '''
    new_tabu_list = []
    for element in tabu_list[:]:
        if first_index in element[:2] or second_index in element[:2]:
            continue
        else:
            if element[2] > 1:
                new_tabu_list.append([element[0], element[1], element[2] - 1])
    return new_tabu_list

def tabu_search(procesory, zsumowane):
    '''
    Głowny algorytm tabu
    - funkcja korzysta ze zmiennej globalnej 'optimuum'
    '''
    tabu_list = []
    t = 3
    niemozliwe = False
    Cmax = max(zsumowane)
    while (Cmax > optimuum) and (not niemozliwe):
        try:
            first_index, second_index = znajdz_pare_do_wymiany(zsumowane, tabu_list)
        except Exception:
            niemozliwe = True
            continue
        try:
            first_elem, second_elem, index_first_elem, index_second_elem =\
                znajdz_najlepsza_wymiane(procesory[first_index], procesory[second_index], zsumowane[first_index], zsumowane[second_index])
            procesory[first_index], procesory[second_index] =\
                zamien_elementy(procesory[first_index], index_first_elem, procesory[second_index], index_second_elem)
            #procesory, zsumowane = lpt_dla_dwoch(procesory, first_index, second_index)
            tabu_list = zmniejsz_i_usun_z_tabu(tabu_list, first_index, second_index)
        except Exception:
            tabu_list = dodaj_do_listy_tabu(first_index, second_index, t, tabu_list)
        zsumowane = list(sum(proc) for proc in procesory)
        Cmax = max(zsumowane)
        #print(Cmax, optimuum, tabu_list)
    return procesory, zsumowane, Cmax

def wyjdz_z_minimum_lokalnego(procesory, przesuniecie):
    '''
    Przemieszanie zadań w dwóch największych i jednym najmniejszym procesorze w celu wyjścia z minimum lokalnego
    '''
    indeksy = sorted([przesuniecie%m, (przesuniecie+1)%m, (przesuniecie+m-1)%m])
    nowe_procesory = procesory[:]
    task_list = sorted(nowe_procesory.pop(indeksy[2]) + nowe_procesory.pop(indeksy[1]) + nowe_procesory.pop(indeksy[0]), reverse=True)
    temp_list = [[],[],[]]

    for i in range(len(task_list)):
        temp_list[i%3].append(task_list[i])
    for procesor in temp_list:
        nowe_procesory.insert(0, procesor)

    nowe_zsumowane = list(sum(proc) for proc in nowe_procesory)
    return nowe_procesory, nowe_zsumowane


def main(procesory, zsumowane, Cmax):
    '''
    Funkcja która kontroluje cały proces szukania optimuum
    - korzysta ze zmiennych globalnych 'm' i 'optimuum'
    '''
    cmax_optimuum = Cmax
    procesory = procesory[:]
    zsumowane = zsumowane[:]
    delta_i = 0
    while (cmax_optimuum > optimuum) and (time.time() - time1 < 180):
        var = tabu_search(procesory, zsumowane)
        print('Koniec {}. iteracji Tabu'.format(delta_i+1))
        if var[2] < cmax_optimuum:
            cmax_procesory = var[0]
            cmax_zsumowane = var[1]
            cmax_optimuum = var[2]
            print(cmax_procesory)
            print(cmax_zsumowane)
            time2 = time.time()
            print("Czas:",time2 - time1)
        print("Najlepszy wynik: {} | Optimuum: {}".format(cmax_optimuum, optimuum))

        procesory, zsumowane = wyjdz_z_minimum_lokalnego(procesory, delta_i)
        delta_i += 1

#-----------------------------------------------------------------------------------------------------------------------


zadania = []
with open('m10n200.txt') as plik:
    m = int(plik.readline())
    n = int(plik.readline())
    for i in range(n):
        zadania.append(int(plik.readline()))

optimuum = math.ceil(sum(zadania) / m)
#optimuum = sum(zadania) / m

wynik = algorytm_poczatkowy(m, zadania)
procesory = wynik[1]
zsumowane = wynik[2]
zadania = wynik[3]

print('ALGORYTM ZACHŁANNY\n'
      'Cmax: {}\n'
      'Optimuum: {}\n'
      'Procesory: {}\n'
      'Zsumowane: {}\n'.format(wynik[0], optimuum, procesory, zsumowane))

print('ALGORYTM TABU SEARCH\n')

time1 = time.time()
main(procesory[:], zsumowane[:], wynik[0])