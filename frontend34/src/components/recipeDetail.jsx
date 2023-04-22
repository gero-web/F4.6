import React from "react";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { getOne } from "../utils/api";

function RecipeOne() {

   const [one, setOne] = useState({});
   const { id } = useParams();
   
   useEffect( () => {
         getOne(setOne, id);     
      
    }, [id])
  
    
  return (
    <div className="container">
        <div>
            <img  className="mainImage" alt={one.title} src={one.image} />
        </div>
        <div className="container__ingredient">
            {
                one.ingredient && one.ingredient.map(item=>{
                    return <div  key={item.id}>
                        <p>
                             {item.title}
                        </p>
                        <p>
                             {item.dimension}
                        </p>
                    </div>
                })
            }
        </div>
        <div className="container__step">
            {
                one.step_recipes && one.step_recipes.map(item=>{
                    return <div>
                        
                        <img alt={item.number} src={item.image} />
                        
                        <p className="step">
                           Шаг: {item.number}
                        </p>
                        <p>
                             {item.description}
                        </p>
                    </div>
                })
            }
        </div>
    </div>
  )

}

export default RecipeOne;
