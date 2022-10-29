from random import randint

brands = [
    "Amazon", "Apple", "Google", "Microsoft", "Samsung", "Meta", "Cisco", "Oracle", "Adobe", "Asus", "Dell", "HP", "NVIDIA", "MSI", "EVGA", "DX Racer", "Sony", "PlayStation 5", "PlayStation 4", "PlayStation 3", "PlayStation 2", "PlayStation 1", "Xiaomi", "Realme", "Oppo", "OnePlus", "Vivo", "Mojang Studios", "Ubisoft", "Roblox Corporation", "Gboard", "Facebook"
]

descriptor = [
    "Smart", "Gaming", "Home", "RTX", "HD", "Wifi Gaming", "High Precision Gaming", "High Accuracy Gaming", "Low Latency", "High Performance", "Responsive", "Fortnite"
]

items = [ 
    "Fridge", "Stove", "Oven", "Toaster", "TV", "Clock", "Subwoofer", "Plug", "Carpet", "Bed", "Cabinet", "Socks", "Blanket", "Chair", "Washing Machine", "Bread", "Jam", "Burger", "Pizza", "Car", "LED Lights", "Band", "Watch", "Fan", "Inverter Air Conditioner", "Beard Trimmer", "Condom", "Baby Formula", "Girlfriend", "EGirl", "Eboy", "Boyfriend", "Basket", "Curtain", "Door", "Cutlery", "Spoon", "Fork", "Soap", "Water Bottle"
]

suffix = [
  "Ultra", "Pro", "Max", "Premium", "Plus", "Extra", "5G", "4G LTE" , "Bluetooth", "Fold", "Flip", "SE", "Studio", "Lite", "Double", "Medium", "Large", "Chewable", "Online", "Free", "Unisex", "For Boys", "For Girls", "Minecraft Edition", "Roblox Edition", "Porter Robinson Special", "Python", "JavaScript", "C++", "C#", "C", "COBOL", "VBA", "Java", "LOLCAT"
]

reasons = [
  "Sexual Assault", "Profanity", "Hacking", "Threatening", "Racism", "Gender Discrimination", "Terrorism", "Exploitation", "Misbehaving", "Sexism", "Spamming"
]

def randomizeBrands():
    return str(brands[randint(0, len(brands) - 1)])

def randomizeDescriptors(): 
    return str(descriptor[randint(0, len(descriptor) - 1)])

def randomizeItems(): 
    return str(items[randint(0, len(items) - 1)])

def randomizeSuffix(): 
    real = randint(1, 5)
    curCount = 0
    curString = ""
    while curCount < real: 
      curString = curString + str(suffix[randint(0, len(suffix) - 1)]) + " "
      curCount += 1
    return curString

def randomizeReason():
    return str(reasons[randint(0, len(reasons) - 1)])