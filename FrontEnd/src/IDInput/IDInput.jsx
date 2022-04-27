import React from "react";
import { TextField, Button } from "@mui/material";
import "./IDInput.css";
// This component handles the Text input AND Buttons.
// Added basic client-side validation on user input.
export default function IDInput({ SetID, currentID }) {
  return (
    <div class="InputContainer">
      <div>
        <Button
          disabled={currentID === 898}
          onClick={() => {
            SetID((currentID += 1));
          }}
          sx={{
            "&.MuiButton-Next": { color: "#03fc7f" },
            border: "2px black solid",
          }}
          variant="Next"
        >
          Next
        </Button>

        <Button
          disabled={currentID === 1}
          onClick={() => {
            SetID((currentID -= 1));
          }}
          sx={{
            "&.MuiButton-Prev": { color: "#03fc7f" },
            border: "2px black solid",
          }}
          variant="Prev"
        >
          Prev
        </Button>
      </div>

      <div class="TextInput">
        <TextField
          sx={{ input: { color: "Blue" } }}
          inputProps={{
            type: "number",
            pattern: "[1-9]{0,3}",
            max: 898,
            min: 1,
            style: { textAlign: "center" },
          }}
          value={currentID}
          onChange={(e) =>
            e.target.value && e.target.validity.valid && SetID(e.target.value)
          }
        />
      </div>
    </div>
  );
}
