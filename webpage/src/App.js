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


  constructor(props) {
        super(props);

        this.state = {
           inputValue: 'Type e.g. 01120',
           data: 'Initial data...'
        }

        this.updateState = this.updateState.bind(this);
        this.updateState = this.updateState.bind(this);
     };

  updateState() {
         this.setState({data: 'Data updated...'})
         console.log(this.state.inputValue)
         
  }

  updateInputValue(e) {
         this.setState({inputValue: e.target.value });

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
        <input type="text" name="postalcode" value={this.state.inputValue} onChange={e => this.updateInputValue(e)}/>
        <input type="submit" onClick={this.updateState} value="Submit" />
        <h4>{this.state.data}</h4>
      </div>
    );
  }
}



export default App;
