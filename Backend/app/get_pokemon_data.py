import aiohttp
from .consts import pokemon_api_URLS


class PokemonData:
    """
    This class populate the Pokemon Object with the following data:
    { id, flavor, sprite image }
    Static URLs are imported from consts.py.
    """

    def __init__(self, pokemon_id):
        self.id = pokemon_id
        self.flavor = ''
        self.sprite = ''

    async def _send_pokemon_api_requests(self, session, url):
        """
        Send requests to Pokemon API
        :param session: aiohttp session
        :param url: request path to Pokemon API
        :return: JSON response
        """
        url = f'{url}/{self.id}'
        try:
            async with session.get(url) as resp:
                return await resp.json()

        except Exception as err:
            print(f"Could not get {url}: ", err)

    def _parse_flavor_from_response(self, res: dict):
        """
        Parse english-only flavor text from the 'Species' Response
        :param res: Species response from the Pokemon API
        :return:
        """
        flavors_list = res.get('flavor_text_entries')
        for flavor_text in flavors_list:
            flavor_languages_dict = flavor_text.get('language')
            if flavor_languages_dict.get('name') == 'en':
                self.flavor = flavor_text.get('flavor_text')
                return
        self.flavor = None

    def _parse_sprite_from_response(self, res: dict):
        """
        Parse the sprite link from the 'Pokemon' API call
        :param res: Pokemon response from the pokemon API
        :return:
        """
        sprite_list = res.get('sprites')  # Get the list of all sprite
        self.sprite = sprite_list.get('front_default')  # get specific sprite if sprite_list exist, else none

    @staticmethod
    async def fetch_pokemon_by_id(poke_id):
        """
        Static method that creates new PokemonData object
        Populate sprite and flavor async
        and returns the object.
        :return: Exception if something is missing
        """
        new_pokemon = PokemonData(poke_id)
        async with aiohttp.ClientSession() as session:  # interface that can be used for a number of individual requests
            # Pass session to each request to avoid creating new sessions
            species_res = await new_pokemon._send_pokemon_api_requests(session, pokemon_api_URLS.get('species_url'))
            pokemon_res = await new_pokemon._send_pokemon_api_requests(session, pokemon_api_URLS.get('pokemon_url'))
            # Populate Flavor text and Sprite
            new_pokemon._parse_flavor_from_response(species_res)
            new_pokemon._parse_sprite_from_response(pokemon_res)

        if not new_pokemon.flavor or not new_pokemon.sprite:
            # Basic error handling - Raise error if data is missing
            raise Exception
        return new_pokemon.__dict__  # Return client-ready data
