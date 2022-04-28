import aiohttp
from .static import pokemon_api_URLS


class PokemonData:
    """
    This class populate the Pokemon Object with the following data:
    { id, flavor, sprite image, and the static pokedex image }
    """

    def __init__(self, pokemon_id):
        self.id = pokemon_id
        self.flavor = ''
        self.sprite = ''

    async def _get_pokemon_sprite(self, session):
        """
        Get the pokemon sprite image
        :param session: aiohttp.ClientSession
        :return:
        """
        url = f"{pokemon_api_URLS.get('pokemon_url')}/{self.id}"
        try:
            async with session.get(url) as resp:
                pokemon = await resp.json()
                sprite_list = pokemon.get('sprites', None)  # Get the list of all sprite
                return sprite_list.get('front_default',
                                       None) if sprite_list else None  # get spcific sprite if sprite_list exist, else none
        except Exception as err:
            print("Could not get sprite ", err)

    async def _get_pokemon_flavor(self, session):
        """
        Get the pokemon flavor
        :param session: aiohttp.ClientSession
        :return: Flavor text
        """
        url = f"{pokemon_api_URLS.get('species_url')}/{self.id}"
        try:
            async with session.get(url) as resp:
                species = await resp.json()
                flavors_list = species.get('flavor_text_entries', None)
                return flavors_list[0].get('flavor_text', None)  # May not be english...

        except Exception as err:
            print("Could not get flavor ", err)

    @staticmethod
    async def fetch_pokemon_by_id(poke_id):
        """
        Create new PokemonData object
        Populate sprite and flavor async

        :return: the object, and Exception if something is missing
        """
        new_pokemon = PokemonData(poke_id)
        async with aiohttp.ClientSession() as session:  # Object that can be used for a number of individual requests
            new_pokemon.sprite = await new_pokemon._get_pokemon_sprite(session)
            new_pokemon.flavor = await new_pokemon._get_pokemon_flavor(session)
        if not new_pokemon.flavor or not new_pokemon.sprite:
            raise Exception
        return new_pokemon.__dict__
