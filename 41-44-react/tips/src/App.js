import React from 'react';
import logo from './logo.svg';
import './App.css';

const PAGE_TITLE = 'PyBites Python Tips API';
const TWITTER_ICON = 'https://codechallenge.es/static/img/icon-twitter.png'

function Tip(props) {
    return(
    <div className="tip">
        <p>{props.tip}
        { props.link &&
           <span> (<a href={props.link} target="_blank">source</a>) </span>
        }
        </p>
        <pre>{props.code}</pre>
        { props.share_link &&
          <p>
            <a href={props.share_link} target="_blank">
             <img src={TWITTER_ICON} alt="share"/>
            </a>
          </p>
        }
    </div>
    )
}

function App() {
  return (
    <div className="App">
      <h2>{PAGE_TITLE}</h2>

      <form id="searchTips">
        <input type="text"
            placeholder="filter tips"
            value=''
            onChange=''/>
       </form>
    </div>
  );
}

export default App;
