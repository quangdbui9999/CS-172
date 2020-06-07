
import abc


class Media(metaclass=abc.ABCMeta):
    def __init__(self, name = "None", rating = 0):
        self.__name = name
        self.__rating = rating

    def getName(self):
        return self.__name

    def getRating(self):
        return self.__rating

    def setName(self, newName):
        self.__name = newName

    def setRating(self, newRating):
        if (newRating >= 0) and (newRating <= 5):
            self.__rating = newRating
        else:
            self.__rating = 0

    def __str__(self):
        result = ""
        return result

    @abc.abstractmethod
    def add(self):
        pass


class Picture(Media):
    def __init__(self, resolution = 200):
        Media.__init__(self)
        self.__resolution = resolution

    def getResulution(self):
        return self.__resolution

    def setResulution(self, newResolution):
        if (newResolution >= 200):
            self.__resolution = newResolution
        else:
            self.__resolution = 200

    def __str__(self):
        result = ""
        result += f"Picture: {self.getName()}, {int(self.getRating())} stars, Resolution: {int(self.getResulution())} dpi."
        return result

    def show(self):
        result = f"Showing <{self.__resolution}>"
        return result

    def add(self):
        name_picture = input("Enter picture name: ")
        resolution_picture = int(input("Enter dpi: "))
        rating_picture = int(input("Enter rating: "))
        self.setName(name_picture)
        self.setRating(rating_picture)
        self.setResulution(resolution_picture)
        print(f"Picture added!")


class Song(Media):
    def __init__(self, artisit = "None", album = "None"):
        Media.__init__(self)
        self.__artist = artisit
        self.__album = album

    def getArtist(self):
        return self.__artist

    def getAlbum(self):
        return self.__album

    def setArtist(self, newArtist):
        self.__artist = newArtist

    def setAlbum(self, newAlbum):
        self.__album = newAlbum

    def __str__(self):
        result = ""
        result += f"Song: {self.getName()}, {int(self.getRating())} stars, Artist: {self.getArtist()}, Album: {self.getAlbum()}."
        return result

    def play(self):
        result = f"<{self.__album}> by <{self.__artist}>, playing now"
        return result

    def add(self):
        name_music = input("Enter song name: ")
        artist_music = input("Enter artist: ")
        album_music = input("Enter album: ")
        rating_music = int(input("Enter rating: "))
        self.setArtist(artist_music)
        self.setName(name_music)
        self.setAlbum(album_music)
        self.setRating(rating_music)
        print("Song added!")


class Movie(Media):
    def __init__(self, type = "None", running_time = 0):
        Media.__init__(self)
        self.__type = type
        self.__running_time = running_time

    def setType(self, newType):
        self.__type = newType

    def setRunningTime(self, newRunningTime):
        if(newRunningTime > 0):
            self.__running_time = newRunningTime
        else:
            self.__running_time = 0

    def __str__(self):
        result = ""
        result += f"Movie: {self.getName()}, {int(self.getRating())} stars, Directed by: {self.__type}, Running time: {int(self.__running_time)} minutes."
        result += Media.__str__(self)
        return result

    def play(self):
        result = f"<{self.getName()}>, playing now"
        return result

    def add(self):
        name_movie = input("Enter movie name: ")
        type_movie = input("Enter director: ")
        running_time_movie = int(input("Enter movie duration: "))
        rating_movie = int(input("Enter rating: "))
        self.setType(type_movie)
        self.setName(name_movie)
        self.setRunningTime(running_time_movie)
        self.setRating(rating_movie)
        print("Movie added!")


class MediaLibrary:
    def __init__(self, list_movie = [], list_picture = [], list_song = []):
        self.__list_movie = list_movie
        self.__list_picture = list_picture
        self.__list_song = list_song

    @staticmethod
    def menuMediaFunction():
        print(f"\n*** Media Library ***")
        print(f"a. Display all Media")
        print(f"b. Display only Songs")
        print(f"c. Display only Movies")
        print(f"d. Display only Pictures")
        print(f"e. Play a Song")
        print(f"f. Play a Movie")
        print(f"g. Show a Picture")
        print(f"h. Add a Song")
        print(f"i. Add a Movie")
        print(f"j. Add a Picture")
        print(f"k. Exit the program\n")

    def print_menu(self):
        menu_option = ""
        self.menuMediaFunction()

        while menu_option != "q":
            menu_option = input("Enter your choice: ")
            if menu_option == "a":
                print()
                for index in self.__list_song:
                    print(index)

                for index in self.__list_picture:
                    print(index)

                for index in self.__list_movie:
                    print(index)
                print()
                self.menuMediaFunction()
            elif menu_option == "b":
                for index in self.__list_song:
                    print(index)
                self.menuMediaFunction()
            elif menu_option == "c":
                for index in self.__list_movie:
                    print(index)
                self.menuMediaFunction()
            elif menu_option == "d":
                for index in self.__list_picture:
                    print(index)
                self.menuMediaFunction()
            elif menu_option == "e":
                search_song = input("Enter the music's name to plays: ")
                for index in self.__list_song:
                    print(index.getName())
                    if index.getName() == search_song:
                        print(index.play())
                    else:
                        print("Song is not in the media library.")
                self.menuMediaFunction()
            elif menu_option == "f":
                search_movie = input("Enter the movie's name to plays: ")
                for index in self.__list_movie:
                    print(index.getName())
                    if index.getName() == search_movie:
                        print(index.play())
                    else:
                        print("Movie is not in the media library.")
                self.menuMediaFunction()
            elif menu_option == "g":
                search_picture = input("Enter the Picture's name to display: ")
                for index in self.__list_picture:
                    print(index.getName())
                    if index.getName() == search_picture:
                        print(index.show())
                    else:
                        print("Picture is not in the media library.")
                self.menuMediaFunction()
            elif menu_option == "h":
                newSong = Song()
                newSong.add()
                self.__list_song.append(newSong)
                self.menuMediaFunction()
            elif menu_option == "i":
                newMovie = Movie()
                newMovie.add()
                self.__list_movie.append(newMovie)
                self.menuMediaFunction()
            elif menu_option == "j":
                newPicture = Picture()
                newPicture.add()
                self.__list_picture.append(newPicture)
                self.menuMediaFunction()
            elif menu_option == "k":
                print("Good-Bye!")
                break
            else:
                menu_option = input("Enter your choice: ")