import React from "react";
import Sprite from "../Sprite/Sprite";
import Flavor from "../Flavor/Flavor";
import IDInput from "../IDInput/IDInput";
import "./Pokedex.css"
// This is the main component that handles all the other, smaller, components - Sprite, Flavor, and inputs.
export default function PokeDex({ pokemonData, SetID }) {
  return (
    <div>
      {/* Display the static image */}
      <img src={pokemonData.pokedex_img} className="responsive center" alt="pokedex"></img>   
      <Sprite spriteUrl={pokemonData.sprite}/>
      <Flavor flavor={pokemonData.flavor}/>
      <IDInput SetID={SetID} currentID={pokemonData.id} />
    </div>
    
  );
}
