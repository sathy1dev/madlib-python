from stories import stories
def gravityfalls():
    pln1 = input("Enter a plural noun \t")
    pln2 = input("Enter a plural noun \t")
    adv1 = input("Enter an adverb \t")
    v1 = input("Enter an verb \t")
    n1 = input("Enter a noun \t")
    fe1 = input("Enter an facial expression \t")
    n2 = input("Enter an verb \t")
    print(stories['gravityfalls'].format(pln1,pln2,adv1,v1,n1,fe1,n2))

def news():
    adj1 = input("Enter an adjective \t")
    adj2 = input("Enter an adjective \t")
    adj3 = input("Enter an adjective \t")
    noun1 = input("Enter an noun \t ")
    noun2 = input("Enter an noun \t")
    v1 = input("Enter past verb \t")
    print(stories["news"].format(adj1,adj2,adj3,noun1,noun2,v1))

print("Welcome to madlib........")

choice = input('''Enter your choice \n
                1. gravityfalls
                2. news 
                ''' )

if choice == 'gravityfalls':
    gravityfalls()
elif choice == 'news':
    news()
else:
    print("Bad choice")