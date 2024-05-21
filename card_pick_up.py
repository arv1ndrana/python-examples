def pick_em_up(piles):
    deck = []

    for pile in piles:
        if isinstance(pile,list):
            for card in pile:
                if card == "N" or card == "GB" or not card.isupper():
                    continue
                else:
                    deck.append(card)

    if not len(deck) < 52:
        return True
    else:
        return False
