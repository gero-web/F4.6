import React from "react";
import { useState, useEffect } from "react";
import { getAllCategori } from "../utils/api";
import { Link } from 'react-router-dom';


function CategoriAll() {

   const [all, setAll] = useState([]);
 
   useEffect( () => {
        getAllCategori(setAll);     
      
    }, [])

    
  return (
    <div className="container">
        <h1> Категории </h1>
            { 
                all &&
                        all.map(item=>{
                            return  <div  className="container__categori_list"  key={item.id}>
                                    <p>
                                           {item.title} 
                                    </p>     
                                    <div className="buttonLink">
                                        <Link to={`/recipe/${item.title}`}> Подробно </Link>
                                    </div>                 
                            </div>
                        }) 
            }
    </div>
  )

}

export default CategoriAll;
