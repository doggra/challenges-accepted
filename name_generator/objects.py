import sys
import datetime
import random

class Identity(object):

    """ Instance attributes:
    self.name       : New person's name
    self.surname    : New person's surname
    self.birthday   : New person's birthday datetime
    """

    def __init__(self, gender=None):
        self.name = None
        self.surname = None
        self.gender = gender
        self.birthday = None
        self.generate_new_id()

    def generate_new_id(self):
        self.set_name()
        self.set_birthday()
        self.print_id()

    def set_name(self):

        # random gender if not set
        if self.gender == None: self.gender = random.choice(['M', 'F'])

        if self.gender == 'M':
            self.name = self.get_rand_line_from_filename( \
                'data/names_pl_{0}.txt'.format(self.gender.lower()))

        elif self.gender == 'F':
            self.name = self.get_rand_line_from_filename( \
                'data/names_pl_{0}.txt'.format(self.gender.lower()))

        self.surname = self.get_rand_line_from_filename( \
            'data/names_pl_sn.txt')

    def set_birthday(self):
        """ Select age from reliable range of years """
        now = datetime.datetime.now()
        date_from = now - datetime.timedelta(days=13*365)
        date_to = now - datetime.timedelta(days=73*365)
        self.birthday = date_from - datetime.timedelta( \
            seconds=random.randint(0, int((date_from - date_to).total_seconds())))

    def get_rand_line_from_filename(self, filename):
        """ Get a random line from text file """
        with open(filename, 'r') as afile:
            line = next(afile)
            for num, aline in enumerate(afile):
              if random.randrange(num + 2): continue
              line = aline
            return line

    def print_id(self):
        """ Display generated person in console """
        name = self.name.strip()
        surname = self.surname.strip()
        birthday = self.birthday.strftime("%d %B %Y")
        text = "GENERATED :: {0} {1}, {2}.".format(name, surname, birthday)
        print(text)
