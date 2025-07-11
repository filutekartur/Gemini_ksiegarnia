## Zadanie: System Zarządzania Książkami
Tym razem zadanie, które sprawdzi Twoje umiejętności tworzenia i modyfikowania danych w bardziej złożonym scenariuszu. Będziesz musiał obsłużyć interakcję z użytkownikiem i warunki.

Napisz program w Pythonie, który symuluje prosty system zarządzania książkami. Program powinien oferować następujące funkcjonalności:

### 1. Struktura danych: 
Zdefiniuj sposób przechowywania książek. Każda książka powinna mieć:

Tytuł (string)

Autor (string)

Rok wydania (int)

Dostępność (boolean - True jeśli dostępna, False jeśli wypożyczona)

Użyj listy słowników do przechowywania wszystkich książek w systemie. Na początek, dodaj kilka przykładowych książek do listy.

```
Python
```

```Python
biblioteka = [
    {'tytuł': 'Wiedźmin: Ostatnie życzenie', 'autor': 'Andrzej Sapkowski', 'rok_wydania': 1993, 'dostępność': True},
    {'tytuł': 'Diuna', 'autor': 'Frank Herbert', 'rok_wydania': 1965, 'dostępność': False},
    # ... więcej książek
]
```
### 2.Wyświetl wszystkie książki: 
Funkcja, która iteruje przez listę biblioteka i wyświetla szczegóły każdej książki w czytelny sposób. Pamiętaj o statusie dostępności.

### 3.Dodaj nową książkę: 
Funkcja, która prosi użytkownika o podanie tytułu, autora i roku wydania nowej książki, a następnie dodaje ją do listy biblioteka. Nowo dodana książka powinna domyślnie mieć dostępność ustawioną na True.

### 4.Wyszukaj książkę po tytule: 
Funkcja, która prosi użytkownika o podanie tytułu książki do wyszukania. Jeśli znajdzie książkę (lub książki) o pasującym tytule, wyświetli jej (ich) szczegóły. Jeśli nie znajdzie, poinformuje o tym użytkownika. Pamiętaj o ignorowaniu wielkości liter podczas wyszukiwania.

### 5.Zmień status dostępności: 
Funkcja, która prosi użytkownika o podanie tytułu książki i nowy status dostępności (np. 'wypożycz' lub 'zwróć'). Następnie aktualizuje status dostępność dla znalezionej książki. Jeśli książka nie zostanie znaleziona, wyświetl odpowiedni komunikat. Ponownie, ignoruj wielkość liter przy wyszukiwaniu tytułu.

### 6.Menu interaktywne (opcjonalnie, ale bardzo zalecane):
Zbuduj prostą pętlę, która będzie wyświetlać menu z opcjami (np. 1. Wyświetl, 2. Dodaj, 3. Wyszukaj, 4. Zmień status, 5. Wyjście) i pozwalać użytkownikowi wybierać akcje, dopóki nie wybierze opcji wyjścia.

### Wskazówki:

Używaj funkcji input() do pobierania danych od użytkownika.

Pamiętaj o konwersji typów (int() dla roku wydania).

Przy wyszukiwaniu i zmianie statusu, pomyśl, co zrobić, jeśli wiele książek ma ten sam tytuł (możesz np. poprosić użytkownika o sprecyzowanie, którą książkę ma na myśli, lub po prostu zmienić status pierwszej znalezionej). Na początek możesz założyć, że tytuły są unikalne.

Użyj for item in lista: do iteracji i if warunek: do sprawdzania warunków.