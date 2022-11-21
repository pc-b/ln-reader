import {useState, useEffect} from "react";
import {Link} from "react-router-dom";

const Home = () => {
    const [title, setTitle] = useState('');

    const handleSubmit = () => {
        console.log('form submitted ✅');
      };

    useEffect(() => {
        const keyDownHandler = event => {
          console.log('User pressed: ', event.key);
    
          if (event.key === 'Enter') {
            event.preventDefault();
    
            // 👇️ call submit function here
            handleSubmit();
          }
        };
    
        document.addEventListener('keydown', keyDownHandler);
    
        return () => {
          document.removeEventListener('keydown', keyDownHandler);
        };
      }, []);



return (
<div>
    <form>
        <input type="text" id="title" name="title" autoComplete="off" value={title} onChange={event => setTitle(event.target.value)} />
        <Link to={{
            pathname: "/search",
            search: "title="+title
            }}>
        <button>Submit</button>
        </Link>


    </form>
</div>
);
};

export default Home;