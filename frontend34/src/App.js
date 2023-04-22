import RecipeAll from './components/recipeAll.jsx'
import recipeOne from './components/recipeDetail.jsx'
import CategoriAll from './components/categori.jsx'
import './style/main.scss';
import {
  Routes,
  Link,
  Route,
} from 'react-router-dom';

function App() {

  return (
    <div className="App">
      <header>
      <nav>
        <ul>
          <li>
            <Link to="/">Главная</Link>
          </li>
        </ul>
      </nav>
    </header>
    <main>
      <Routes>
        <Route path="/recipe/:categories" Component={RecipeAll}></Route>
        <Route path="/detail/:id" Component={recipeOne}></Route>
        <Route path="/" Component={CategoriAll}></Route>
      </Routes>
    </main>
    </div>
  );
}

export default App;
