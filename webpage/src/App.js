import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MLab from 'mlab-data-api';

var mLab = MLab({
  key: '4Jf3PH27flXFBjUfpZu24nl-Pe1e2a-3',
  host:'https://api.mlab.com', //optional
  uri : '/api/1/databases/housing_data/collections/etuovi?',
  version :'1',
  database:'housing_data',
  timeout : 10000
})

class App extends Component {
  componentWillMount() {
    console.log("mongo client")
    console.log(mLab)
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Analyzing apartment rents in Helsinki region</h1>
        </header>
        <p className="App-intro">
          To get started, enter a postal code in the search bar.
        </p>
        <input type="text" name="postalcode" />
        <input type="submit" value="Submit" />
      </div>
    );
  }
}

export default App;
