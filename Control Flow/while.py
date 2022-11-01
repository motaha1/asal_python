card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())


## Please use this space to test and run your code


############### break and continue
        

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
count = -1
news_ticker = ""

# write your loop here
for i in headlines:
    news_ticker+=' '
    count+=1
    for x in i:
        if (count==140):
            break
        else:
            news_ticker+=x
            count+=1
        

print(news_ticker[3:])
