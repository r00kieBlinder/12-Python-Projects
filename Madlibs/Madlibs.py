# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____ "
# youtuber = 'Clever Programmer' # some string variable 

# # a few ways to do this 
# print ('subscirbe to' + youtuber)
# print ('subscribe to {}'.format(youtuber))
# print (f'subscribe to {youtuber}')


adj1 = input('Adjective : ')
superhero = input('Superhero : ')
youtuber = input('Youtuber : ')
adj2 = input('Adjective : ')
adj3 = input('Adjective : ')

madlib = f'Computer Programming is so {adj1}! I feel like I am {superhero} doing it. \
I really appreciate {youtuber} for your {adj2} Python tutorial. I {adj3} you!'

print(madlib)

# I learned GitHub