# 💰 Money Tracking Bot

* With this bot, you can record how you have spent your money. 

* There are currently eight different categories: 

    🍞 grocery

    👗 clothes

    💄 makeup

    ✈️ travel

    🍴 dining out

    💸 tuition

    🏠 rent and fees

    💍 jewlery

# Basic Functions



## * Store


Use `!store` to enable storing mode to record your purchases.

<img width="549" alt="Screen Shot 2021-07-13 at 2 49 14 PM" src="https://user-images.githubusercontent.com/75393672/125515833-56fb9b28-980c-4b2d-8d78-69e0272bde25.png">

After the prompt, you should enter purchases with `#`

For example, `#grocery, 140.93 #makeup, 57.98`

If you entered a category that is not included in the default, you will receive an error message and you need to type again. This will be updated in the future with the function to add your own categories. 

<img width="654" alt="Screen Shot 2021-07-13 at 2 52 39 PM" src="https://user-images.githubusercontent.com/75393672/125516252-6433362e-5493-4356-b53d-f66dba615696.png">


After entering the purchases, it will return a list of information ready to be stored.

<img width="675" alt="Screen Shot 2021-07-13 at 2 54 18 PM" src="https://user-images.githubusercontent.com/75393672/125516450-dfb5939c-021c-457d-82e0-20012ad569fe.png">

Then, the prompt will keep asking if you want to store more purchases. 

<img width="654" alt="Screen Shot 2021-07-13 at 2 55 23 PM" src="https://user-images.githubusercontent.com/75393672/125516553-30828377-2c53-41e4-88bc-0d2cee854527.png">

If you have entered all transactions, you can type `%` to exit storing mode. `%` is used to exit all other modes with money_tracking_bot.

<img width="612" alt="Screen Shot 2021-07-13 at 2 56 56 PM" src="https://user-images.githubusercontent.com/75393672/125516740-e923b343-d913-49a2-9947-a6a9a5f4f048.png">



## * Track


Use `!track` to track where you have spent your money.

You can type `all`, `max`, `min`, or a certain `category` to track the amount of money spent in all categories, where you have spent most money, least money, or how much you have spent on a certain category.

<img width="618" alt="Screen Shot 2021-07-13 at 3 06 34 PM" src="https://user-images.githubusercontent.com/75393672/125517789-22a7e844-091d-4b53-b4a7-1e27499e9c19.png">

If you type `all`:

<img width="465" alt="Screen Shot 2021-07-13 at 3 06 56 PM" src="https://user-images.githubusercontent.com/75393672/125517831-7e1805db-6611-470c-8c1e-46b653ab8e69.png">

If you type `min`:

<img width="502" alt="Screen Shot 2021-07-13 at 3 08 28 PM" src="https://user-images.githubusercontent.com/75393672/125517996-fec89be2-7812-47db-8157-3ce814e8bfd1.png">

If you type `max`:

<img width="450" alt="Screen Shot 2021-07-13 at 3 08 59 PM" src="https://user-images.githubusercontent.com/75393672/125518054-dbecf689-4559-4ad6-9127-90aec37a6fda.png">

Exit tracking mode with `%`:

<img width="529" alt="Screen Shot 2021-07-13 at 3 10 16 PM" src="https://user-images.githubusercontent.com/75393672/125518186-42c52062-4955-4a71-a8b3-54c4cc696e62.png">



## * Inspect


Use `!inspect` to inspect all the records we have stored.

After the prompt, you can type `y` to inspect the book or `n` to exit inspecting mode.

If you answered `y`:

<img width="671" alt="Screen Shot 2021-07-13 at 3 11 34 PM" src="https://user-images.githubusercontent.com/75393672/125518326-71b1e487-fa28-4ed1-aea6-c090357988f3.png">

If you answered `n`:

<img width="507" alt="Screen Shot 2021-07-13 at 3 11 59 PM" src="https://user-images.githubusercontent.com/75393672/125518383-f914b640-598b-4736-96e8-f47fd964d89e.png">

You don't need to exit inspection mode after getting the result.



## * Clear


Use `!clear` to clear a certain category or all records.

This is needed if you have used one category too often and want to set it back to zero, so that it does not end up being the category with the maximum amount every time. For example, the `grocery` category.

<img width="582" alt="Screen Shot 2021-07-13 at 3 14 54 PM" src="https://user-images.githubusercontent.com/75393672/125518694-b640784b-8119-4949-a1b3-029e12b7a14c.png">

Use `%` to exit clearing mode.

<img width="477" alt="Screen Shot 2021-07-13 at 3 15 24 PM" src="https://user-images.githubusercontent.com/75393672/125518741-c187dca2-1196-40d7-a1c8-3c2ac5078600.png">

To observer your result, use `!inspect`: Here all grocery transactions recorded have been set to zero.

<img width="630" alt="Screen Shot 2021-07-13 at 3 16 02 PM" src="https://user-images.githubusercontent.com/75393672/125518823-10735053-cd39-43da-8e57-bbdbec2a85c8.png">




# Potential Future Updates:

1. enable users to add their own categories
2. support Excel files as a mean to record transactions
3. support scraping uploaded bank statements to extract transactions to be purchase inputs


# License:

GPL. See file COPYING.txt




