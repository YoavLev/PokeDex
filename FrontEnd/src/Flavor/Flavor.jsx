import React from 'react'
import './Flavor.css'
//Display the flavor.
export default function Flavor({flavor}) {
  return (
    <div className="scrollable-div flavor">{flavor}</div>
  )
}

