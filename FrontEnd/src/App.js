import { useState, useEffect } from "react";
import PokeDex from "./Pokedex/PokeDex";

function App() {
  // All states need for the app, including the ID which is passed down the components
  const [data, setData] = useState(null); 
  const [pokemonId, setPokemonId] = useState("1");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch the api async and catch errors
  useEffect(() => {
    const getData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/${pokemonId}`);
        if (!response.ok) {
          throw new Error(
            `This is an HTTP error: The status is ${response.status}`
          );
        }
        let actualData = await response.json();
        console.log(actualData);
        setData(actualData);
        setError(null);
      } catch (err) {
        setError(err.message);
        setData(null);
      } finally {
        setLoading(false);
      }
    };
    getData();
  }, [pokemonId]);

  return (
    <div className="App">
      Pokedex
      {loading && <div>Fetching Data</div>}
      {error && (
        // <div>{`There is a problem fetching the post data - ${error}`}</div>
        alert("Oops, Somthing went wrong")
      )}
      {/* Invoke the first component, pass down data and pokemonID as props */}
      {data && <PokeDex pokemonData={data} SetID={setPokemonId} />}
    </div>
  );
}

export default App;
