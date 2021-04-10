############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name): #these are methods bc it's part of the class. you can't call these methods unless you already have created a melontype instance
        """Initialize a melon."""
        self.code = code #instance attribute; every method in this class can access these using self
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        #self.pairings = self.pairings.append(pairing) <- .append actually returns none
        self.pairings.append(pairing)

    def update_code(self, new_code): #these are the arguments; you can update code by calling melon.update_code(___)
        """Replace the reporting code with the new_code."""

        #self.code = self.new_code <- new_code is not a class or an instance attribute so this will give me an error
        self.code = new_code 

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk = MelonType(
        "musk",
        "Muskmelon",
        1998,
        "green",
        True,
        True
    )
    musk.add_pairing("mint")
    all_melon_types.append("musk")

    cas = MelonType(
        "cas",
        "Casaba",
        2003,
        "orange",
        False,
        None
    )
    cas.add_pairing("strawberries", "mint") #?
    all_melon_types.append("cas")

    cren = MelonType( #you have to match the order in the init method so assign
        code = "cren",
        name = "Crenshaw",
        1996,
        "green",
        False,
        None
    )
    cren.add_pairing("prociutto")
    all_melon_types.append("cren")

    yw = MelonType(
        "yw",
        "Yellow Watermelon",
        2013,
        "yellow",
        False,
        True
    )
    yw.add_pairing("ice cream")
    all_melon_types.append("yw")

    return all_melon_types

def print_pairing_info(melon_types): #melon_types is just a placeholder
    """Prints information about each melon type's pairings.""" 

    for melon in melon_types: #use self inside the class; melon here is an instance of the MelonType class
        print(f"{melon.name} pairs with") 
        print(f"- {melon.pairings}") #not self because you use self inside the class; here the variable comes from the for loop above

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    return dict()

melons = make_melon_types()
print_pairing_info(melons)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon instance."""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
    
    def is_sellable(self, is_sellable):
        self.is


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    #sellable if shape+color ratings > 5 & not from field 3


