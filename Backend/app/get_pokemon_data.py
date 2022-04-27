import aiohttp


class PokemonData():
    """
    This class populate the Pokemon Object with the following data:
    { id, flavor, sprite image, and the static pokedex image }
    """

    def __init__(self, pokemon_id):
        self.pokemon_api_path = "https://pokeapi.co/api/v2/"
        self.id = pokemon_id
        self.flavor = ''
        self.sprite = ''
        self.pokedex_img = 'https://www.pngitem.com/pimgs/m/541-5418323_gameboy-drawing-electronics-inside-of-a-pokedex' \
                           '-hd.png '

    async def _get_pokemon_sprite(self, session):
        """
        Get the pokemon sprite image
        :param session: aiohttp.ClientSession
        :return:
        """
        url = f'https://pokeapi.co/api/v2/pokemon/{self.id}'
        try:
            async with session.get(url) as resp:
                pokemon = await resp.json()
                return pokemon['sprites']['front_default']
        except Exception as err:
            print("Could not get sprite ", err)

    async def _get_pokemon_flavor(self, session):
        """
        Get the pokemon flavor
        :param session: aiohttp.ClientSession
        :return:
        """
        url = f'https://pokeapi.co/api/v2/pokemon-species/{self.id}'
        try:
            async with session.get(url) as resp:
                species = await resp.json()
                return species['flavor_text_entries'][0]['flavor_text']  # May not be english...
        except Exception as err:
            print("Could not get flavor ", err)

    async def fetch_poke_by_id(self):
        """
        Execute both requests async,

        :return: Exception if something is missing
        """
        async with aiohttp.ClientSession() as session:  # Object that can be used for a number of individual requests
            self.sprite = await self._get_pokemon_sprite(session)
            self.flavor = await self._get_pokemon_flavor(session)
            if not self.flavor or not self.sprite:
                raise Exception

