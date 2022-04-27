import React from 'react'
import "./Sprite.css"
export default function Sprite({spriteUrl}) {
  return (

        <div>
            <img src={spriteUrl} className="sprite" alt="sprite"></img>
        </div>
    
  )
}
