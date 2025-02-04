import React from "react";
import "../../styles/login.css"
import { useState } from "react";

export const Login = () => {
    

    const [nombre, setNombre] = useState("")
    const [contraseña, setContraseña] = useState("")
  
    const [error, setError] = useState(false)
  
    const handleSubmit = (e) => {
      e.preventDefault()
  
      if(nombre === "" || contraseña === ""){
        setError(true)
        return
      }
      
      setError(false)
  
      // setUser([nombre])
  
    }

    return(
    <>
    <section>
      <h1>Log in</h1>

      <form 
      className="formulario"
      onSubmit={handleSubmit}
      >
        <input 
        type="text"
        value={nombre}
        onChange={e => setNombre(e.target.value)} 
        />
        <input 
          type="password"
          value={contraseña}
          onChange={e => setContraseña(e.target.value)} 
        />
        <button> Entrar </button>
      </form>
      {error && <alert>Fill All</alert>}
    </section>
    </>
    )
}

export default Login