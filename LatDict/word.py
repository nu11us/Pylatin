class Word:

    def __init__(self, entry):
        self.word_page = entry

    @property
    def name(self):
        name = self.word_page.div.h3.a
        return name.get_text()

    @property
    def definitions(self):
        definition = self.word_page.ol.get_text().split('\n')[1:-1]
        return definition

    @property
    def age(self):
        age = self.word_page.find("li", class_="age-info").find("span",class_='value').get_text()
        return age

    @property
    def area(self):
        area = self.word_page.find("li", class_="area-info").find('span',class_='value').get_text()
        return area

    @property
    def geography(self):
        geography = self.word_page.find("li", class_="geography-info").find('span',class_='value').get_text()
        return geography

    @property
    def frequency(self):
        frequency = self.word_page.find("li", class_="frequency-info").find('span',class_='value').get_text()
        return frequency

    @property
    def source(self):
        source = self.word_page.find("li", class_="source-info").find('span',class_='value').get_text()
        return source

    @property
    def part_of_speech(self):
        part = self.word_page.find("p", class_="speech").get_text()
        return part

class Noun(Word):

    @property
    def gender(self):
        gender = str(self.word_page).split('gender')[1]
        gender = gender.split('value')[1]
        gender = gender.split('>')[1]
        gender = gender.split('<')[0]
        return gender
    @property
    def declension(self):
        declension = str(self.word_page).split('declension')[1]
        declension = declension.split('value')[1]
        declension = declension.split('>')[1]
        declension = declension.split('<')[0]
        return declension

class Adjective(Word):

    @property
    def declension(self):
        declension = str(self.word_page).split('declension')[1]
        declension = declension.split('value')[1]
        declension = declension.split('>')[1]
        declension = declension.split('<')[0]
        return declension

class Verb(Word):

    @property
    def conjugation(self):
        try:
            conjugation = str(self.word_page).split('conjugation')[1]
            conjugation = conjugation.split('value')[1]
            conjugation = conjugation.split('>')[1]
            conjugation = conjugation.split('<')[0]
            return conjugation
        except:
            return "Irregular"

    @property
    def voice(self):
        voice = str(self.word_page).split('voice')[1]
        voice = voice.split('value')[1]
        voice = voice.split('>')[1]
        voice = voice.split('<')[0]
        return voice

class Preposition(Word):

    @property
    def prep_type(self):
        prep_type = str(self.word_page).split('type')[1]
        prep_type = prep_type.split('value')[1]
        prep_type = prep_type.split('>')[1]
        prep_type = prep_type.split('<')[0]
        return prep_type

