# An inspired code from @codewithharry KBC exercise
que = [
    ["Who is the main character in the 'Iron Man' movies?", "Tony Stark", "Steve Rogers", "Bruce Wayne", "Clark Kent", 1],
    ["Which video game features the character Mario?", "Minecraft", "Call of Duty", "Super Mario Bros.", "Fortnite", 3],
    ["What is the name of Harry Potter's pet owl?", "Scabbers", "Hedwig", "Fawkes", "Crookshanks", 2],
    ["Which superhero is known as the 'Dark Knight'?", "Iron Man", "Spider-Man", "Batman", "Superman", 3],
    ["Which game popularized the battle royale genre?", "Valorant", "Minecraft", "Overwatch", "PUBG", 4],
    ["What movie is the quote 'I'll be back' from?", "The Terminator", "Die Hard", "Rambo", "Predator", 1],
    ["Which game studio created 'The Legend of Zelda'?", "Ubisoft", "Rockstar Games", "Nintendo", "EA", 3],
    ["In which movie does the character Jack Dawson appear?", "Titanic", "Inception", "The Notebook", "Twilight", 1],
    ["Which series features a floating city called Columbia?", "Half-Life", "Bioshock Infinite", "Mass Effect", "Fallout", 2],
    ["Which Marvel movie was the first to earn over $2 billion?", "Iron Man", "Avengers: Endgame", "Black Panther", "Avengers: Infinity War", 2],
    ["What is the name of the AI in the 'Portal' video game series?", "Cortana", "GLaDOS", "EVA", "Siri", 2],
    ["In 'The Matrix', what color is the pill Neo takes?", "Blue", "Red", "Green", "White", 2],
    ["Who directed 'Pulp Fiction'?", "Steven Spielberg", "Christopher Nolan", "Martin Scorsese", "Quentin Tarantino", 4],
    ["Which game holds the record for highest-grossing media franchise?", "Call of Duty", "FIFA", "Mario", "Pokémon", 4]
]

lvl = [5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 70000000]
safe = [40000, 320000, 5000000]

money_won = 0
safe_money = 0

for i in range(len(que)):
    q = que[i]
    print(f"\nQuestion {i+1} for ₹{lvl[i]:,}")
    print(q[0])
    print(f"1. {q[1]}     2. {q[2]}")
    print(f"3. {q[3]}     4. {q[4]}")
    ans = input("Your answer (1-4): ")

    if ans == ("1" or "2" or "3" or "4"):
        ans_num = int(ans)
        if ans_num == q[5]:
            print(" Correct!")
            money_won = lvl[i]
            if money_won == safe[0] or money_won == safe[1] or money_won == safe[2]:
                safe_money = money_won
        else:
            print(" Wrong answer!")
            break
    else:
        print(" Invalid input! Exiting.")
        break

print(f"\n You won ₹{safe_money:,} (guaranteed, lol)!")
