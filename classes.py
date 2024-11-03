import random


class Plant:    # Define class for plants
    def __init__(self, name, harvest_yield):
        self.name = name
        self.harvest_yield = harvest_yield
        self.growth_stages = ['seed', 'sprout', 'plant', 'flower', 'fruiting', 'harvest-ready']
        self.current_growth_stage = self.growth_stages[0]
        self.harvestable = False

    def grow(self):     # Define function to simulate grow of plant
        current_stage_index = self.growth_stages.index(self.current_growth_stage)
        if current_stage_index < len(self.growth_stages) - 1:
            self.current_growth_stage = self.growth_stages[current_stage_index + 1]
            print(f"The {self.name} has grown to the {self.current_growth_stage} stage.")
            if self.current_growth_stage == 'harvest-ready':
                self.harvestable = True
                print(f"The {self.name} is now harvestable!")
        else:
            print(f"The {self.name} is already at its final growth stage.")

    def harvest(self):      # Define function to harvest plant
        if self.harvestable:
            self.current_growth_stage = self.growth_stages[0]
            self.harvestable = False
            print(f"You have harvested the {self.name}.")
            return True
        else:
            print(f"The {self.name} is not ready for harvest.")
            return False


class Tomato(Plant):
    def __init__(self):
        super().__init__('Tomato', 10)
        self.growth_stages = ['seed', 'sprout', 'plant', 'fruiting', 'harvest-ready']


class Carrot(Plant):
    def __init__(self):
        super().__init__('Carrot', 1)
        self.growth_stages = ['seed', 'sprout', 'plant', 'harvest-ready']


class Lettuce(Plant):
    def __init__(self):
        super().__init__('Lettuce', 1)
        self.growth_stages = ['seed', 'sprout', 'plant', 'flower', 'harvest-ready']


class Apple(Plant):
    def __init__(self):
        super().__init__('Apple', 5)
        self.growth_stages = ['seed', 'sprout', 'plant', 'fruiting', 'harvest-ready']


class Bnana(Plant):
    def __init__(self):
        super().__init__('Bnana', 2)
        self.growth_stages = ['seed', 'sprout', 'plant', 'fruiting', 'harvest-ready']


class Cherry(Plant):
    def __init__(self):
        super().__init__('Cherry', 3)
        self.growth_stages = ['seed', 'sprout', 'plant', 'fruiting', 'harvest-ready']


class Herb(Plant):
    def __init__(self):
        super().__init__('Herb', 1)
        self.growth_stages = ['seed', 'sprout', 'plant', 'harvest-ready']


PLANT_CLASSES = {
    "Tomato": Tomato,
    "Carrot": Carrot,
    "Lettuce": Lettuce,
    "Apple": Apple,
    "Bnana": Bnana,
    "Cherry": Cherry,
    "Herb": Herb

}

PLANT_PRICE = {
    "Tomato": 5,
    "Carrot": 3,
    "Lettuce": 1,
    "Apple": 10,
    "Banana": 15,
    "Cherry": 20,
    "Herb": 1
}


class Gardener:     # define class for garden
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.planted_plants = []
        self.inventory = {
            'seed': {},
            'harvested': {}
        }

    def add_seeds(self, plant_type, quantity):      # function to increase seeds
        if plant_type in self.inventory['seed']:
            self.inventory['seed'][plant_type] += quantity
        else:
            self.inventory['seed'][plant_type] = quantity
        print(f"Added {quantity} {plant_type} seeds to inventory.")

    def plant_seed(self, plant_type):       # function to plant seed
        if plant_type in self.inventory['seed'] and self.inventory['seed'][plant_type] > 0:
            plant_class = PLANT_CLASSES[plant_type]
            plant = plant_class()
            self.planted_plants.append(plant)
            self.inventory["seed"][plant_type] -= 1
            print(f"Planted a {plant_type}.")
        else:
            print(f"No {plant_type} seeds available in inventory.")

    def tend_plants(self):      # function to grow plant in garden
        for plant in self.planted_plants:
            plant.grow()

    def harvest_plants(self):       # function to harvest plant in garden
        for plant in self.planted_plants:
            if plant.harvest():
                plant_type = plant.name
                if plant_type in self.inventory["harvested"]:
                    self.inventory["harvested"][plant_type] += plant.harvest_yield
                else:
                    self.inventory["harvested"][plant_type] = plant.harvest_yield
        self.planted_plants = [plant for plant in self.planted_plants if not plant.harvestable]

    def seed_value(self):       # function to count seeds
        seeds_value = self.inventory['seed']
        return seeds_value

    def harvested_value(self):
        harvesteds_value = self.inventory['harvested']
        return harvesteds_value

    def mountain(self):
        possible_seeds = ["Tomato", "Carrot", "Lettuce", "Herb"]
        found_seed = random.choice(possible_seeds)
        quantity = random.randint(1, 10)
        self.add_seeds(found_seed, quantity)
        print(f'While foraging in mountain, you found {quantity} {found_seed}!')

    def desert(self):
        possible_seeds = ["Carrot", "Lettuce", "Bnana", "Herb"]
        found_seed = random.choice(possible_seeds)
        quantity = random.randint(1, 10)
        self.add_seeds(found_seed, quantity)
        print(f'While foraging in desert, you found {quantity} {found_seed}!')

    def forest(self):
        possible_seeds = ["Tomato", "Carrot", "Lettuce", "Apple", "Cherry", "Herb"]
        found_seed = random.choice(possible_seeds)
        quantity = random.randint(1, 10)
        self.add_seeds(found_seed, quantity)
        print(f'While foraging in forest, you found {quantity} {found_seed}!')

    def beach(self):
        possible_seeds = ["Carrot", "Apple", "Bnana", "Herb"]
        found_seed = random.choice(possible_seeds)
        quantity = random.randint(1, 10)
        self.add_seeds(found_seed, quantity)
        print(f'While foraging in beach, you found {quantity} {found_seed}!')

    def sell(self, to_sell, number_to_sell):
        if to_sell in self.inventory['harvested']:
            if 0 < number_to_sell <= self.inventory['harvested'][to_sell]:
                sell_price = PLANT_PRICE.get(to_sell, 0)
                all_sell_price = number_to_sell * sell_price
                self.money += all_sell_price
                self.inventory['harvested'][to_sell] -= number_to_sell
                if self.inventory['seed'][to_sell] == 0:
                    del self.inventory['seed'][to_sell]
                print(f'You earn {all_sell_price}$ from the sell\nNow You have {self.money}$')
            else:
                print(f'You dont have that much {to_sell}!')
        else:
            print(f'Given item to sell is not valid!')


def select_item(inventory):
    if not inventory:
        print("Inventory is empty.")
        return None
    print('Select an item by number: ')
    key_items = list(inventory.keys())
    values_items = list(inventory.values())
    for index, item in enumerate(key_items):
        print(f'{index + 1}. {item}(Quantity: {inventory[item]})')
    try:
        choice = int(input('Enter the number of the item you wish to choose: ')) - 1
        if 0 <= choice < len(key_items):
            selected_item = key_items[choice]
            selected_values = values_items[choice]
            return selected_item, selected_values
        else:
            print('Invalid choise. Please select a valid number.')
    except ValueError:
        print('Invalid input. Please enter a number.')
