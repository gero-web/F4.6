import React from "react";
import { useState, useEffect } from "react";
import { getAll } from "../utils/api";
import { Link, useParams } from 'react-router-dom';


function RecipeAll() {

   const [all, setAll] = useState([]);
   const { categories } = useParams()
   
   useEffect( () => {
        getAll(setAll,categories);     
      
    }, [categories])

    
  return (
    <div className="container">
        <h1> Рецепты категории: {categories} </h1>
            { 
                all &&
                        all.map(item=>{
                            return  <div  className="container__list"  key={item.id}>
                                    <p>
                                        {item.title} --- Время готовки {item.time} минут
                                    </p>     
                                    
                                    <img className="mainImage" src={item.image} alt={item.title}/>
                                    
                                    <div className="buttonLink">
                                        <Link to={`/detail/${item.id}`}> Подробно </Link>
                                    </div>                 
                            </div>
                        }) 
            }
    </div>
  )

}

export default RecipeAll;
