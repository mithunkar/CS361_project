import zmq
import random

verb_ing_array = [
    "Running", "Jumping", "Swimming", "Reading", "Writing",
    "Singing", "Dancing", "Climbing", "Laughing", "Sleeping",
    "Eating", "Drinking", "Thinking", "Dreaming", "Talking",
    "Walking", "Hiking", "Biking", "Painting", "Drawing",
    "Cooking", "Baking", "Crying", "Smiling", "Studying",
    "Teaching", "Learning", "Creating", "Exploring", "Searching",
    "Discovering", "Playing", "Hugging", "Kissing", "Whispering",
    "Surfing", "Fishing", "Rowing", "Running", "Flying",
    "Hopping", "Skipping", "Glowing", "Falling", "Rising",
    "Shining", "Growing", "Sinking", "Riding", "Guiding",
    "Solving", "Waiting", "Wishing", "Falling", "Crawling",
    "Flying", "Caring", "Sharing", "Skiing", "Snowboarding",
    "Laughing", "Hunting", "Gathering", "Building", "Blossoming",
    "Babbling", "Chattering", "Cracking", "Roaring", "Hooting",
    "Giggling", "Humming", "Murmuring", "Whistling", "Exploding",
    "Melting", "Freezing", "Flourishing", "Quivering", "Spinning",
    "Dribbling", "Sliding", "Flickering", "Juggling", "Bouncing",
    "Rumbling", "Stumbling", "Fluttering", "Dwindling", "Wandering",
    "Rambling", "Tumbling", "Twinkling", "Unraveling", "Stirring",
    "Beaming", "Reflecting", "Confusing", "Revolving", "Dissolving",
    "Guiding"
]

adjective_array = [
    "Sparkling", "Vivacious", "Mysterious", "Enchanting", "Whimsical",
    "Resplendent", "Serene", "Exuberant", "Majestic", "Luminous",
    "Jubilant", "Tranquil", "Radiant", "Mystical", "Vibrant",
    "Captivating", "Gleaming", "Alluring", "Piquant", "Whimsical",
    "Ethereal", "Quirky", "Harmonious", "Dazzling", "Intriguing",
    "Scintillating", "Ornate", "Opulent", "Whirlwind", "Jubilant",
    "Effervescent", "Mesmerizing", "Enigmatic", "Astounding", "Resplendent",
    "Pulsating", "Enthralling", "Piquant", "Spirited", "Radiant",
    "Zesty", "Eloquent", "Dynamic", "Vivid", "Lively",
    "Sprightly", "Ethereal", "Quixotic", "Flamboyant", "Ephemeral",
    "Panoramic", "Aesthetic", "Sublime", "Grandiose", "Picturesque",
    "Opulent", "Serendipitous", "Irresistible", "Ineffable", "Enigmatic",
    "Mellifluous", "Zenith", "Lustrous", "Nebulous", "Quizzical",
    "Captivating", "Zephyr", "Pinnacle", "Iridescent", "Mellifluous",
    "Glorious", "Tantalizing", "Nebulous", "Ethereal", "Awe-inspiring",
    "Ineffable", "Illustrious", "Rhapsodic", "Rapt"
]
plural_noun_array = [
    "Apples", "Bananas", "Cherries", "Dogs", "Cats",
    "Horses", "Hats", "Books", "Keys", "Bottles",
    "Flowers", "Trees", "Rivers", "Mountains", "Oceans",
    "Puppies", "Kittens", "Children", "Friends", "Houses",
    "Cars", "Bicycles", "Watches", "Glasses", "Shoes",
    "Penguins", "Elephants", "Giraffes", "Lions", "Tigers",
    "Dinosaurs", "Butterflies", "Dragonflies", "Stars", "Clouds",
    "Computers", "Phones", "Cameras", "Monkeys", "Penguins",
    "Fish", "Whales", "Snakes", "Dragons", "Robots",
    "Aliens", "Kangaroos", "Koalas", "Pandas", "Pigs",
    "Chickens", "Cows", "Sheep", "Hens", "Roosters",
    "Frogs", "Turtles", "Snails", "Crabs", "Jellyfish",
    "Bears", "Deer", "Wolves", "Foxes", "Squirrels",
    "Bats", "Spiders", "Bees", "Ants", "Ladybugs",
    "Ducks", "Geese", "Swans", "Owls", "Eagles",
    "Seagulls", "Peacocks", "Penguins", "Kangaroos", "Zebras",
    "Pigs", "Goats", "Donkeys", "Rabbits", "Frogs",
    "Lions", "Tigers", "Bears", "Wolves", "Elephants",
    "Giraffes", "Monkeys", "Gorillas", "Birds", "Cats",
    "Dogs", "Snakes", "Fish", "Insects", "Reptiles"

]

places_array = [
    "Paris", "New York City", "Tokyo", "London", "Rome",
    "Sydney", "Rio de Janeiro", "Venice", "Barcelona", "Cairo",
    "Dubai", "Moscow", "Los Angeles", "Berlin", "Amsterdam",
    "Bangkok", "Istanbul", "Mumbai", "Cape Town", "Vancouver",
    "Santorini", "Bora Bora", "Kyoto", "Prague", "Vienna",
    "Toronto", "Seoul", "Buenos Aires", "Copenhagen", "Edinburgh",
    "Auckland", "Marrakech", "Havana", "Reykjavik", "Singapore",
    "Dublin", "Athens", "Helsinki", "Zurich", "Stockholm",
    "New Orleans", "San Francisco", "Munich", "Cancun", "Montreal",
    "Helsinki", "Oslo", "Perth", "Melbourne", "Hobart",
    "Florence", "Budapest", "Beijing", "Shanghai", "Cape Town",
    "Krakow", "Manhattan", "Quebec City", "Oxford", "Cambridge",
    "Seville", "Granada", "Valencia", "Ibiza", "Tahiti",
    "Galapagos Islands", "Bali", "Himalayas", "Great Barrier Reef", "Machu Picchu",
    "Amazon Rainforest", "Grand Canyon", "Yellowstone National Park", "Everest Base Camp", "Antarctica",
    "Dubrovnik", "Salzburg", "Bruges", "Nice", "Marseille",
    "Cologne", "Agra", "Jaipur", "Amritsar", "Bangalore",
    "Kolkata", "Hiroshima", "Nairobi", "Cairo", "Casablanca",
    "Kiev", "Warsaw", "Prague", "Bratislava", "Lisbon",
    "Bucharest", "Sofia", "Dublin", "Copenhagen", "Reykjavik",
    "Nairobi", "Cape Town", "Kigali", "Jerusalem", "Tbilisi"

]
body_parts_array = [
    "Head", "Shoulders", "Knees", "Toes", "Eyes",
    "Ears", "Nose", "Mouth", "Neck", "Chest",
    "Back", "Arms", "Elbows", "Hands", "Fingers",
    "Thumbs", "Hips", "Legs", "Knees", "Feet",
    "Toes", "Ankles", "Heels", "Toenails", "Fingernails",
    "Hair", "Eyebrows", "Eyelashes", "Forehead", "Jaw",
    "Cheeks"

]

noun_array = [
    "Apple", "Banana", "Cherry", "Dog", "Cat",
    "Horse", "Hat", "Book", "Key", "Bottle",
    "Flower", "Tree", "River", "Mountain", "Ocean",
    "Puppy", "Kitten", "Child", "Friend", "House",
    "Car", "Bicycle", "Watch", "Glass", "Shoe",
    "Penguin", "Elephant", "Giraffe", "Lion", "Tiger",
    "Dinosaur", "Butterfly", "Dragonfly", "Star", "Cloud",
    "Computer", "Phone", "Camera", "Monkey", "Penguin",
    "Fish", "Whale", "Snake", "Dragon", "Robot",
    "Alien", "Kangaroo", "Koala", "Panda", "Pig",
    "Chicken", "Cow", "Sheep", "Hen", "Rooster",
    "Frog", "Turtle", "Snail", "Crab", "Jellyfish",
    "Bear", "Deer", "Wolf", "Fox", "Squirrel",
    "Bat", "Spider", "Bee", "Ant", "Ladybug",
    "Duck", "Goose", "Swan", "Owl", "Eagle",
    "Seagull", "Peacock", "Kangaroo", "Zebra", "Pig",
    "Goat", "Donkey", "Rabbit", "Frog", "Lion",
    "Tiger", "Bear", "Wolf", "Elephant", "Giraffe",
    "Monkey", "Gorilla", "Bird", "Cat", "Dog",
    "Snake", "Fish", "Insect", "Reptile"
]

game_array = [
    "Chess", "Monopoly", "Scrabble", "Checkers", "Jenga",
    "Risk", "Pictionary", "Catan", "Twister", "Battleship",
    "Clue", "Uno", "Yahtzee", "Connect Four", "Sorry",
    "Operation", "Guess Who", "Hungry Hungry Hippos", "Mouse Trap", "Trivial Pursuit",
    "Charades", "Dominos", "Cards Against Humanity", "Rummy", "Go Fish",
    "Mahjong", "Backgammon", "Dungeons & Dragons", "Poker", "Bridge",
    "Solitaire", "Mahjong", "Fortnite", "Minecraft", "Among Us",
    "Call of Duty", "League of Legends", "World of Warcraft", "Overwatch", "Halo",
    "Super Mario Bros", "The Legend of Zelda", "Pokémon", "Sonic the Hedgehog", "Final Fantasy",
    "Grand Theft Auto", "Assassin's Creed", "FIFA", "NBA 2K", "Madden NFL",
    "Rocket League", "Fortnite", "Apex Legends", "Fall Guys", "Among Us",
    "Mario Kart", "Super Smash Bros", "Street Fighter", "Tekken", "Mortal Kombat",
    "Candy Crush", "Angry Birds", "Clash of Clans", "FarmVille", "Words with Friends",
    "Fortnite", "PUBG", "Warframe", "Fortnite", "Apex Legends",
    "The Witcher", "Cyberpunk 2077", "Red Dead Redemption", "Dark Souls", "Skyrim",
    "Among Us", "Fall Guys", "Valorant", "Genshin Impact", "Fortnite",
    "Chess", "Monopoly", "Scrabble", "Checkers", "Jenga",
    "Risk", "Pictionary", "Catan", "Twister", "Battleship"
]

plant_array = [
    "Rose", "Sunflower", "Tree", "Fern", "Cactus",
    "Daisy", "Tulip", "Lily", "Ivy", "Bamboo",
    "Palm", "Maple", "Oak", "Pine", "Willow",
    "Hibiscus", "Aloe", "Basil", "Thyme", "Rosemary",
    "Mint", "Cilantro", "Sage", "Lemon", "Lime",
    "Orange", "Apple", "Banana", "Strawberry", "Tomato",
    "Cucumber", "Carrot", "Lettuce", "Pepper", "Potato"
]

number_array = [
    "Three", "Fifteen", "Two", "Seventy", "Eighty-nine",
    "Six", "Ninety-five", "Four", "Twenty-three", "Fifty",
    "Eight", "Sixty-eight", "Seventy-nine", "Thirteen", "Forty-two",
    "One Hundred", "Nine", "Sixty", "Twenty", "Seventeen",
    "Five", "Eighty", "Thirty-seven", "Fourteen", "Seventy-two",
    "Fifty-six", "Eleven", "Sixty-nine", "Forty-five", "Eighty-seven",
    "Sixty-four", "Three", "Nineteen", "Seventy-four", "Twenty-nine",
    "Two", "Eighty-three", "Forty-eight", "Eighty-six", "Sixty-one",
    "Twenty-eight", "Fifty-four", "One", "Sixty-three", "Ninety",
    "Forty", "Eighty-four", "Twelve", "Seventy-one", "Fifty-three",
    "Thirty-four", "Seventy-seven", "Forty-one", "Eighty-five", "Fifty-nine",
    "Seven", "Sixty-seven", "Twenty-two", "Ninety-eight", "Forty-nine",
    "Eighty-one", "Fifty-two", "Fifty-seven", "Thirty-six", "Ninety-nine",
    "Thirty", "Seventy-six", "Eighty-two", "Fifty-one", "Sixty-five",
    "Eighty-four", "Sixty-six", "Eighty", "Thirty-five", "Sixty-two",
    "Eighty-eight", "Ten", "Sixty-seven", "Eighty-four", "Fifty-five",
    "Ninety-seven", "Sixty-eight", "Forty-six", "Twenty-four", "Eighty-nine",
    "Sixty-nine", "Eighty-three", "Sixty-seven", "Ninety-four", "Seventy-three",
    "Sixty-six", "Fifty-four", "Eighty-five", "Thirty-one", "Sixty",
    "Ninety-one", "Fifty-one", "Twenty-six", "Eighty-nine", "Eighty-three",
    "Seventy-eight", "Twenty-five", "Fifty-six", "Eighty-two", "Thirty-three"
]


def randomizer(word_type):
    listVar = []
    match word_type.lower():
        case 'verb ending in -ing':
            listVar = verb_ing_array
        case 'adjective':
            listVar = adjective_array
        case 'a place':
            listVar = places_array
        case 'plural noun':
            listVar = plural_noun_array
        case 'part of the body':
            listVar = body_parts_array
        case 'noun':
            listVar = noun_array
        case 'game':
            listVar = game_array
        case 'plant':
            listVar = plant_array
        case 'number':
            listVar = number_array

    if listVar:
        return random.choice(listVar)
    else:
        print(f"No words available for word type: {word_type}")
        return "N/A"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for next request from client
    message = socket.recv_string()

    if message == 'close':
        break

    # Call randomizer and send the result back to the client
    result = randomizer(message)
    socket.send_string(result)
    print("Sent response: %s" % result)

socket.close()
context.term()