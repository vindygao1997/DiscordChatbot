

from discord.ext import commands
import random
import csv
import pandas as pd
from time import sleep
import basics


cluster = MongoClient("mongodb+srv://sharongao1997:Findajob2021!@discordbot.bfkle.mongodb.net/test")

db = cluster["UserData"]

collection = db["UserData"]



bot = commands.Bot(command_prefix='!')
categories = ['grocery', 'clothes', 'makeup', 'travel', 'dining out', 'tuition', 'rent and fees', 'jewlery']
filename = "money_tracking.csv"
fields = categories

def get_track_result(msg):
    to_be_track = msg.content.lower()
    df = pd.read_csv('money_tracking.csv')

    if to_be_track in categories:
        sum_column = df[to_be_track].sum(axis=0)
        return sum_column
        
    elif to_be_track == 'max':
        max_sum = df.sum(axis=0).max()
        return max_sum

    elif to_be_track == 'min':
        min_sum = df.sum(axis=0).min()
        return min_sum
    
    elif to_be_track == 'all':
        all_sum = df.sum(axis=0)
        return all_sum

    else:
        return "fail"

def clear_all():
    #truncates the csv file
    f = open(filename, "w+")
    f.close()
    #recreate a new file with appropriate headers
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()

def delete_column(col):
    df = pd.read_csv(filename)
    #set all values in that column to be zero
    df[col] = 0
    df.to_csv(filename, encoding='utf8', index=False)
    

@bot.command(name="track", help="type 'enter'to store where you spent your money and type '!track' to get the specified category where you are spending most money")
async def money_tracking(ctx):
    first_time = True
    while True:
        # this message pops up right after user starts tracking
        if first_time == True:
            print(first_time)
            await ctx.send("Enter the category you want to check or type 'all', 'max' or 'min")
        # after the first round, the following message will pop up for conciseness
        else: 
            sleep(2)
            await ctx.send("What else do you want to track?")
            
        first_time = False
        # collect user input
        msg = await bot.wait_for("message")
        # end tracking 
        if msg.content.lower() == '%':
            await ctx.send("You have finished tracking your money!")
            break
        # if user types 'max','min','all', or specific category names, the get_track_result function will get the total amount of money spent on that category
        if msg.content.lower() == 'max' or msg.content.lower() == 'min' or msg.content.lower() == 'all' or msg.content.lower() in categories:
            await ctx.send(get_track_result(msg))
        # invalid inputs
        else:
            await ctx.send("This category doesn't exist!")
            await ctx.send("Available categories are: grocery, clothes, makeup, travel, dining out, tuition, rent and fees, and jewlery")
        
    

@bot.command(name="store", help="store all new materials you bought by typing them one by one")
async def money_entry(ctx):
    #enable the bot to keep asking for entries until I asked it to stop
    while True:
        await ctx.send("start entering your purchases! Use # to separate each category. The format should be #grocery, 23.1 #clothes, 25.0")
        #collect input received
        msg = await bot.wait_for("message")
        #if entered '%', the bot stopped asking for transactions
        if msg.content.lower() == '%':
            break
        #clean input by categories
        info = msg.content.lower().split('#')

        #remove the empty string at into[0]
        info = info[1:]

        #all other categories should be filled with 0 if not mentioned in the input
        info_dict = {'grocery': 0,
                    'clothes': 0,
                    'makeup' : 0,
                    'travel' : 0,
                    'dining out': 0,
                    'tuition': 0,
                    'rent and fees': 0,
                    'jewlery': 0}
        #for each category item, split "category" and "amount"
        for i in info:
            element = i.split(',')
            element = [x.strip() for x in element]
            if element[0] not in categories:
                await ctx.send("You have entered an invalid category.")
                await ctx.send("Available categories are : grocery, clothes, makeup, travel, dining out, tuition, rent and fees, and jewlery")
            else:
            #record them as key : value in info_dict
                if info_dict.get(element[0]) is not None:
                    info_dict.update({element[0] : element[1]})

                    #store to mongodb
                    collection.insert_one(info_dict)

                await ctx.send(info_dict)

        
        # display amounts for all categories
        
    
    #exiting the bot
    await ctx.send("You have finished entering all transactions!")

@bot.command(name="clear")
async def clear(ctx):
    while True:
        await ctx.send("What do you want to clear? You can say a category name or 'all'.")
        msg = await bot.wait_for("message")
        request = msg.content.lower()
        if request == '%':
            await ctx.send("You have exited clearing mode.")
            break
        if request == 'all':
            clear_all()
        elif request in categories:
            delete_column(request)
            await ctx.send("You have cleared all values in category " + request) 
        else:
            await ctx.send("This is not a valid request. You should type 'all' or the specified category you want to remove")

@bot.command(name="inspect")
async def inspect(ctx):
    while True:
        await ctx.send("Do you want to inspect the book? Y/n")
        msg = await bot.wait_for("message")
        answer = msg.content.lower()
        if answer == 'y':
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                data = list(reader)
                row = len(data)
            df = pd.read_csv(filename, skiprows=range(1, row - 20))
            df = df.to_string(index=False)
            await ctx.send(df)
            break
        elif answer == 'n':
            await ctx.send("You have exited inspection.")
            break
        else:
            await ctx.send("Invalid answer. Please answer Y/n.")

with open("bot_token.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read: ")
    bot.run(TOKEN)





