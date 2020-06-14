import random as r
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as py
import time as t



scifi = ["Silent Running", "Mission to Mars","Screamers", "Futureworld", "The Brood",
 "Scanners", "The Entity", "They Live", "The Hidden", "The Dead Zone", "Dreamscape", "Brazil",
 "From Beyond", "Leviathan", "Deep Star Six", "Fortress", "Timescape", "Doctor Mordrid", "Brainscan",
 "No Escape", "The Arrival", "Mimic", "The Relic", "Cube", "Deep Rising", "The Time Shifters", "The Cell",
 "Supernova", "Equilibrium", "Ultraviolet", "Primer", "Serenity", "Children of Men", "The Thirteenth Floor",
 "Push", "Pandorum", "Cargo", "Moon", "Another Earth", "Europa Report", "Prometheus", "Snowpiercer", "The Machine",
 "Banshee Chapter","What Happened to Monday","District 9","Elysium","Riddick","Chappie","Guardians of The Galaxy",
 "2001: Space Oddysey","Serenity"]


drama = ["Nightcrawler", "Hereditary", "The Usual Suspects", "Shutter Island",
         "The unforgiven", "The Perfect Getaway", "The Others", "The Machinist",
         "Memento","Now you see me","Falling Down","Enemy","Triangle","The Innocents",
         "Fallen", "Sev7n","Gone Girl","Get Out", "Jacobs Ladder","Oldboy","The Mist",
         "Shelter","Identity", "The Others", "Tenebre", "What Lies Beneath", "The Life of David Gale",
         "House of 9", "The Belko Experiment", "Primal Fear", "Road Train", "The Secret In Their Eyes."
         "Never Talk to Strangers","Final Analysis","Devil","Colossal","Sorry to bother you",
         "A Beautiful Mind","Knieves Out","Lost in Translation","Eternal sunshine of the Spotless Mind",
         "American Beauty","GoodFellas","Braveheart","Farewell my concubine","Grave of the Fireflies",
         "Network","A Separation","Ikiru","Lawrence of Arabia","Schindler's List","The Searchers",
         "Shane","Hell or High Water","No Country for old men","El Topo","Paris Texas"]


horror = ["Possum","Murder me Monster","Ravenous","As Above,So Below","Cheap Thrills",
           "Hush","Goodnight Mommy","Pontypool","Bubba Ho-tep","Zombeavers","The Voices",
           "Little Evil","Life After Beth","The Perfection","Apostle","Im Just F*cking with you",
           "Treehouse","Cronos","Modern Vampire","Popcorn","The Resurrected","Dusr Devil",
           "Ready or Not","Tigers are not afraid","Crawl","Little Monsters","The Lodge",
           "Girl on the third floor","Dead Dicks","The Vigil","Color out of space","Saint Maud",
           "I Trapped the devil","Daniel Isn't Real","The Witch","The Wind","The hole in the ground",
          "Crawl","Bliss","Sweetheart","Depraved","Hagasuzussa: A Heathen's Curse","Greta",
          "Scary stories to tell in the dark","Midsommar","The Wicker Man","The Exorcist",
          "Annihilation","The prince of darkness","The thing","In the mouth of madness",
          "Event Horizon","The Last Wave","Possession","The Mist","Uzumaki","The Void"
          "Dagon"]

comedy = ["Bad words","Deadpool","Deadpool 2","The Interview","Superbad","30 Minutes or less",
          "Wedding Crashers","Ted","The Package","Zack and Miri Make a Porno","The Nice Guys",
          "Long Shot","Overboard","Mistress America","Sword of Trust","Results","Keanu",
          "The Incredible Jessica James","Juliet,Naked","Hunt for the wilderpeople","Another Year",
          "Toni Erdmann","The Trotsky","Hello,My Name is Doris","Force Majeure","The Wackness",
          "Win Win","Lars and the Real Girl","Safety Not Guaranteed","High Fidelity","Third Star",
          "Seven Psychopaths","The Grand Seduction","It's Kind of a Funny Story","Sorry to Bother you",
          "Dope","Thank you for smoking","In the loop","Four Lions","We are the Best!","Submarine",
          "Frequently Asked Questions about Time Travel","Hot Fuzz","Kiss Kiss Bang Bang","Adaptation",
          "Begin Again","Boy","Kung Fu Hustle","The Guard","Come as you are","Logan Lucky","Infinitely Polar Bear",
          "Perfetti Sconosciuti","Snatch","Soul Kitchen","The Sisters Brothers","The Peanut Butter Falcon",
          "Good Boys","I Don't Feel At Home In This World Anymore.","Mayhem","Sukiyaki Western Django"]

action = ["Saving Private Ryan","Gladiator","The Good the Bad The Ugly","The Godfather","Seven Samurai","Paths of Glory",
          "Apocalypse Now","Rancho Notorious","High Plains Drifter","Winchester 73","Unforgiven","Pat Garret and Billy the Kid",
          "Tombstone","Highnoon","Rio Bravo","The wild bunch", "The shootist","Fir a few dollars","Once upon a time in the west",
          "Shanghai Noon","Big trouble in little China","From Dusk till dawn","Shoot Em Up","Hanna","Ghost in the shell 2","Three",
          "The good the bad the weird","Dredd","Edge of Tomorrow","Elite Squad","13 Assassins","Skyfall","District B13","Unleashed",
          "The Bourne Identity","Drug War","Sicario","Hero","300","IP Man","The Guest","Dunkirk","Django"]

animated = ["Big Hero 6","Tangled","Kubo","Fantastic Mr.Fox","Gru","Chicken Little","Shrek","Iron Giant","Ratatouille",
            "The Incredibles","Finding Nemo","Monsters Inc","Inside Out","Toy Story","Up","Wall-E","Lion King"]

halloffame = ["Sorry to Bother you", "Midsommar"]

print (f"There are {str(len(scifi))} movies in scifi")
print (f"There are {str(len(drama))} movies in drama")
print (f"There are {str(len(horror))} movies in horror")
print (f"There are {str(len(comedy))} movies in comedy")
print (f"There are {str(len(action))} movies in action")
print (f"There are {str(len(animated))} movies in animated")

while True:
    try:
        choose = input("Which genre do you want to see ? scifi, drama, horror, comedy, action")
        genre = vars()[choose]
        numbr = r.randint(0, (int(len(genre) + 1)))
        movie = (str(genre[numbr]))
        print(movie)
    except KeyError:
        print("Please type the genre correctly.")
    else:
        reshuffle = input("Would you like another pick ?")
        if reshuffle == "no":
            break

url = ('https://www.youtube.com/results?search_query=' + movie + ' trailer')


trailer = input("would you like to see a trailer?")

if trailer == "yes":

    driver = webdriver.Firefox()
    driver.get(url)
    click = driver.find_element_by_css_selector('ytd-video-renderer.ytd-item-section-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)').click()
    t.sleep(2.5)
    py.typewrite("f")

elif trailer == "no":
    exit()

#Agregar input para escojer cual genero. check . done .

#Agregar metodo para que muestre trailer de pelicula que se escoje. check .

#Agregar GUI. Display de imagen de pelicula y boton para trailer

#Another Year not comedy