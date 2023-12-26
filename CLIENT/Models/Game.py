class Game():
    game_number=4
    def __init__(self, demo_file, description, gender, id:int, images, name, price:float, videos):
        Game.game_number+=1
        self.demo_file = demo_file
        self.description = description
        self.gender = gender
        self.id = id
        self.images = images
        self.name = name
        self.price = price
        self.videos = videos

    def toJson(self):
        return {
            'demo_file' : self.demo_file,
            'description' : self.description,
            'gender' : self.gender,
            'id' : self.id,
            'images' : self.images,
            'name' : self.name,
            'price' : self.price,
            'videos' : self.videos
        }
    
    @staticmethod
    def fromJson(jsonGame):
        newGame = Game(
            jsonGame['demo_file'],
            jsonGame['description'],
            jsonGame['gender'],
            int(jsonGame['id']),
            jsonGame['images'],
            jsonGame['name'],
            float(jsonGame['price']),
            jsonGame['videos']
        )
        return newGame