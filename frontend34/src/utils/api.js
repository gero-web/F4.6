import axios from 'axios';

const urlAll = 'http://127.0.0.1:8000/recipe-categori-list/';
const urlOne = 'http://127.0.0.1:8000/recipe-categori-detail/';
const urlCategoriAll = 'http://127.0.0.1:8000/recipe-categori';

const getAll =  (setAll, categories) => {
    return axios.get(urlAll +  categories).then(req=>{
        const data = req.data;
        setAll(data);
    });
}

const getAllCategori =  (setAll) => {
    return axios.get(urlCategoriAll).then(req=>{
        const data = req.data;
        setAll(data);
    });
}

const getOne = async (setDetail, id) => {
   await axios.get(urlOne + id).then(req=>{
        const data = req.data;
        setDetail(data);
    })
}



export {

    getAll,
    getOne,
    getAllCategori,

}