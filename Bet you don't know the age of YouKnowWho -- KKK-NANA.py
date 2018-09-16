
# coding: utf-8

# In[ ]:


age_of_youknowwho = 91 
count = 0
while count <3:
    guess_age=int(input('Please guess the age of YouKnowWho: '))
    if guess_age == age_of_youknowwho:
        print('\033[1;33mYou are the boy who lived!\033[0m')
        break
    elif guess_age > age_of_youknowwho:
        print('Think smaller...')
    else:
        print('Think bigger...')
    count += 1
    #-----------------------------
    while count == 3:
        continue_confirm = input('Do you want to keep trying?(y/n): ')
        if continue_confirm == 'y':
            count = 0
        elif continue_confirm == 'n':
            print("Well,such a fun time we had! I'll see you next time then (hat tipping).")
        else:
            print('Pardon?')
            count == 3
    else:
        continue

