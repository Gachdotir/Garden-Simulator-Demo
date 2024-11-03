import classes

# Main part of game
player_input = input('Please enter Gardener name: ')
player = classes.Gardener(player_input)
print(
    f"""
  Hello {player},

Welcome to our new farm! We just purchased this beautiful piece of land,
but there's a catch: we borrowed $1000 from the bank to make this dream come true.
Now, it's time to roll up our sleeves and start gathering money to repay the bank.
Bank: {player.money}$
Are you ready to begin your farming adventure and make this place thrive?
Let's get started!
"""
)
print(
    f"""
To get started, you need to go through a series of tutorials. Our goal here is to collect seeds,
plant them, nurture them until they grow into harvestable crops, and then sell them at the market.

We have an inventory that includes two parts. The first part is seeds; these are the seeds that we can plant.
The second part is harvested crops, which are the ready products to sell in the market.
{player.inventory}
as you see we dont have anything in our inventory.
    """
)
print(
    """
Our journey has three different parts:

Part 1: Our adventure begins with finding new seeds. -> to go to adventure write adventure

Part 2: Once we have the seeds, we need to plant them in our garden. -> to go to garden write garden

Part 3: Finally, when our products are ready, we will sell them at the market to earn money. -> to go to market write market
    """
)
while player.money < 1000:
    to_go = input('Where do you want to go?')
    if to_go == 'adventure':
        print('You are begin knew adventure!')
        area = input('Where do you want to go?select form the list[mountain,desert,forest,beach]: ')
        if area == 'mountain':
            player.mountain()
            print('You return from adventure successfully')
        elif area == 'desert':
            player.desert()
            print('You return from adventure successfully')
        elif area == 'forest':
            player.forest()
            print('You return from adventure successfully')
        elif area == 'beach':
            player.beach()
            print('You return from adventure successfully')
        else:
            print('Invalid input, Please select form the list')
        print(player.inventory)
        print(f'{player.money}$')
    elif to_go == 'garden':
        garden_action = 0
        while garden_action != 'leave':
            print('Welcom to Garden!')
            print(player.inventory)
            print(f'{player.money}$')
            print("""
if you want to plant seed write plant
if you want to tend seed write tend
if you want to harvest seed write harvest
    """)
            garden_action = input('What do you want to do? (type "leave" to exit)')
            if garden_action == 'plant':
                plant_type = input(f'What do you want to plant?: {player.seed_value()}')
                number_to_plant = int(input('How many seed do you want to palnt?'))
                for i in range(number_to_plant):
                    player.plant_seed(plant_type)
                print(player.inventory)
                print(f'{player.money}$')
            elif garden_action == 'tend':
                number_to_tend = int(input('How many periods do you want to pass?'))
                for i in range(number_to_tend):
                    player.tend_plants()
                print(player.inventory)
                print(f'{player.money}$')
            elif garden_action == 'harvest':
                player.harvest_plants()
                print(player.inventory)
                print(f'{player.money}$')
            elif garden_action == 'leave':
                print('You leave the Garden!')
                break
            else:
                print('Invalid input, Please select form the list')
    elif to_go == 'market':
        to_sell = 0
        while to_sell != 'leave':
            print("""
      Welcom to the market!
      Here we can sell our products.
      Here is the price of products:
      Tomato: 5$
      Carrot: 3$
      Lettuce: 1$
      Apple: 10$
      Bnana: 15$
      Cherry: 20$
      Herb: 1$
      """)
            print(player.inventory)
            print(f'{player.money}$')
            to_sell = input(f'What do you want to sell?{player.harvested_value()} (type "leave" to exit) ')
            if to_sell != 'leave':
                number_to_sell = int(input('How many do you want to sell?'))
                player.sell(to_sell, number_to_sell)
            else:
                print('You leave the market!')
                print(player.inventory)
                print(f'{player.money}$')
                break

    else:
        print('Invalid input, Please select form the list')

print(
    f"""
Congratulations, {player}!

You've successfully reached $1000 and repaid your loan to the bank.
Your hard work and dedication have transformed your farm into a thriving business.
This is just the beginning of your farming legacy. Well done on completing this incredible journey!
know we have {player.money - 1000}$
{player.inventory}
    """
)
