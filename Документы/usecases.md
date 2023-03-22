# Сценарии использования

1. Одиночная игра
```py
game = load.Load()
game_menu = menu.Menu()
game_settings = settings.Settings()
game_currency = currency.Currency()
game_inventory = inventory.Inventory()
game_deal = deal.Deal()
game_power = power.Power()
game_hint = hint.Hint()
game_shuffle = shuffle.Shuffle()
game_pause = pause.Pause()
```
2. Одиночная игра на время
```py
game = load.Load()
game_menu = menu.Menu()
game_settings = settings.Settings()
game_currency = currency.Currency()
game_inventory = inventory.Inventory()
game_deal = deal.Deal()
game_power = power.Power()
game_hint = hint.Hint()
game_shuffle = shuffle.Shuffle()
game_win = win.Win()
game_lose = lose.Lose()
```
3. Многопользовательская игра против других игроков
```py
game = load.Load()
game_menu = menu.Menu()
game_settings = settings.Settings()
game_currency = currency.Currency()
game_inventory = inventory.Inventory()
game_deal = deal.Deal()
game_power = power.Power()
game_hint = hint.Hint()
game_shuffle = shuffle.Shuffle()
game_win = win.Win()
game_lose = lose.Lose()
game_friends = friends.Friends()
game_chat = chat.Chat()
game_reports = reports.Reports()
```