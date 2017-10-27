import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';


//image imports
import avgsize from './images/averageApartmentSize.png'
import avgprice from './images/averagePriceSquareMap.png'
import abyall from './images/averageBuiltYearMap.png'
import pvsAll from './images/scatter/priceVersusSizeScatterAll.png'
import legend from './images/legend.png'

import aps00100 from './images/averagePriceMap/avgPricePerSquare00100.png'
import aps00120 from './images/averagePriceMap/avgPricePerSquare00120.png'
import aps00130 from './images/averagePriceMap/avgPricePerSquare00130.png'
import aps00140 from './images/averagePriceMap/avgPricePerSquare00140.png'
import aps00150 from './images/averagePriceMap/avgPricePerSquare00150.png'
import aps00700 from './images/averagePriceMap/avgPricePerSquare00700.png'
import aps00980 from './images/averagePriceMap/avgPricePerSquare00980.png'
import aps02230 from './images/averagePriceMap/avgPricePerSquare02230.png'
import asm00100 from './images/averageSizeMap/avgSize00100.png'
import asm00120 from './images/averageSizeMap/avgSize00120.png'
import asm00130 from './images/averageSizeMap/avgSize00130.png'
import asm00140 from './images/averageSizeMap/avgSize00140.png'
import asm00150 from './images/averageSizeMap/avgSize00150.png'
import asm00700 from './images/averageSizeMap/avgSize00700.png'
import asm00980 from './images/averageSizeMap/avgSize00980.png'
import asm02230 from './images/averageSizeMap/avgSize02230.png'
import pvs00100 from './images/scatter/priceVersusSizeScatter00100.png'
import pvs00120 from './images/scatter/priceVersusSizeScatter00120.png'
import pvs00130 from './images/scatter/priceVersusSizeScatter00130.png'
import pvs00140 from './images/scatter/priceVersusSizeScatter00140.png'
import pvs00150 from './images/scatter/priceVersusSizeScatter00150.png'
import pvs00700 from './images/scatter/priceVersusSizeScatter00700.png'
import pvs00980 from './images/scatter/priceVersusSizeScatter00980.png'
import pvs02230 from './images/scatter/priceVersusSizeScatter02230.png'
import aby00100 from './images/averageYearMap/avgBuiltYear00100.png'
import aby00120 from './images/averageYearMap/avgBuiltYear00120.png'
import aby00130 from './images/averageYearMap/avgBuiltYear00130.png'
import aby00140 from './images/averageYearMap/avgBuiltYear00140.png'
import aby00150 from './images/averageYearMap/avgBuiltYear00150.png'
import aby00700 from './images/averageYearMap/avgBuiltYear00700.png'
import aby00980 from './images/averageYearMap/avgBuiltYear00980.png'
import aby02230 from './images/averageYearMap/avgBuiltYear02230.png'



//helsinki region postal codes
var postalcodes = ['00100', '00120', '00130', '00140', '00150', '00160', '00170', '00180', '00190', '00200', '00210', '00220', '00230', '00240', '00250', '00260', '00270', '00280', '00290', '00300', '00310', '00320', '00330', '00340', '00350', '00360', '00370', '00380', '00390', '00400', '00410', '00420', '00430', '00440', '00500', '00510', '00520', '00530', '00540', '00550', '00560', '00570', '00580', '00590', '00600', '00610', '00620', '00630', '00640', '00650', '00660', '00670', '00680', '00690', '00700', '00710', '00720', '00730', '00740', '00750', '00760', '00770', '00780', '00790', '00800', '00810', '00820', '00830', '00840', '00850', '00860', '00870', '00880', '00890', '00900', '00910', '00920', '00930', '00940', '00950', '00960', '00970', '00980', '00990', '01200', '01230', '01260', '01280', '01300', '01340', '01350', '01360', '01370', '01380', '01390', '01400', '01420', '01450', '01480', '01510', '01520', '01530', '01600', '01610', '01620', '01630', '01640', '01650', '01660', '01670', '01680', '01690', '01700', '01710', '01720', '01730', '01740', '01750', '01760', '01770', '02100', '02110', '02120', '02130', '02140', '02150', '02160', '02170', '02180', '02200', '02210', '02230', '02240', '02260', '02270', '02280', '02290', '02300', '02320', '02330', '02340', '02360', '02380', '02600', '02610', '02620', '02630', '02650', '02660', '02680', '02700', '02710', '02720', '02730', '02740', '02750', '02760', '02770', '02780', '02810', '02820', '02860', '02920', '02940', '02970', '02980']


class App extends Component {


  constructor(props) {
        super(props);
        this.state = {
           inputPostalCode: '00100',
           inputCondition: 'Hyvä',
           inputAllowpets: '1997',
           inputSize: '35',
           location: '',
           data: '',
           img1: avgsize,
           img2: avgprice,
           img3: pvsAll,
           img4: abyall
        }

        this.updateState = this.updateState.bind(this);
        this.updateInputPostValue = this.updateInputPostValue.bind(this);
     };

  updateState() {
         let found = 0
         for (var i = 0; i<postalcodes.length; i++){
           if(this.state.inputPostalCode === postalcodes[i]){
             found = 1
           }
         }

         if(found === 1){
           if(this.state.inputPostalCode === "00100")
            this.setState({
              location: 'Helsinki Keskusta - Etu-Töölö',
              data: 'Predicted price: 1526.835 eur',
              img1: asm00100,
              img2: aps00100,
              img3: pvs00100,
              img4: aby00100
            })
            else if(this.state.inputPostalCode === "00120")
             this.setState({
               location: 'Punavuori',
               data: 'Predicted price: 692.25 eur',
               img1: asm00120,
               img2: aps00120,
               img3: pvs00120,
               img4: aby00120
             })
             else if(this.state.inputPostalCode === "00130")
              this.setState({
                location: 'Kaartinkaupunki',
                data: 'Predicted price: 1894.167 eur',
                img1: asm00130,
                img2: aps00130,
                img3: pvs00130,
                img4: aby00130
              })
              else if(this.state.inputPostalCode === "00140")
               this.setState({
                 location: 'Kaivopuisto - Ullanlinna',
                 data: 'Predicted price: 1860 eur',
                 img1: asm00140,
                 img2: aps00140,
                 img3: pvs00140,
                 img4: aby00140
               })
               else if(this.state.inputPostalCode === "00150")
                this.setState({
                  location: 'Eira - Hernesaari',
                  data: 'Predicted price: 1400 eur',
                  img1: asm00150,
                  img2: aps00150,
                  img3: pvs00150,
                  img4: aby00150
                })
               else if(this.state.inputPostalCode === "00700")
                this.setState({
                  location: 'Malmi',
                  data: 'Predicted price: 1100 eur',
                  img1: asm00700,
                  img2: aps00700,
                  img3: pvs00700,
                  img4: aby00700
                })
              else if(this.state.inputPostalCode === "00980")
               this.setState({
                 location: 'Etelä-Vuosaari',
                 data: 'Predicted price: 1095 eur',
                 img1: asm00980,
                 img2: aps00980,
                 img3: pvs00980,
                 img4: aby00980
               })
               else if(this.state.inputPostalCode === "02230")
                this.setState({
                  location: 'Matinkylä',
                  data: 'Predicted price: 798.68 eur',
                  img1: asm02230,
                  img2: aps02230,
                  img3: pvs02230,
                  img4: aby02230
                })

              else
                this.setState({
                location: 'Sorry, this demo version does not have all data. Please try one of [00100,00120,00130,00140,00150,00700,00980,02230]',
                data: '',
                img1: avgsize,
                img2: avgprice,
                img3: pvsAll,
                img4: abyall
                })

         }
         else{
           this.setState({
             data: 'Outside Helsinki region or invalid postal code. Here are some average statistics for Helsinki region:',
             location: ''
           })
         }

  }

    updateInputPostValue(e) {
         this.setState({inputPostalCode: e.target.value});

 }

  updateInputConditionValue(e) {
        this.setState({inputCondition: e.target.value });

}

  updateInputAllowpetsValue(e) {
       this.setState({inputAllowpets: e.target.value });

}

  updateInputSizeValue(e) {
       this.setState({inputSize: e.target.value});

}

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Analyzing apartment rents in Helsinki region</h1>
        </header>
        <div className="App-input">
        <p className="App-intro">
          To get an estimate of the rental price, please enter the required parameters in the text fields.
        </p>
        <div>
        <label className="label">Total Size</label>
        <label className="label">Condition</label>
        <label className="label">Built Year</label>
        <label className="label">Postal Code</label>
        </div>
        <input className="input" type="text" name="apartmentsize" value={this.state.inputSize} onChange={e => this.updateInputSizeValue(e)}/>
        <input className="input" type="text"  name="condition" value={this.state.inputCondition} onChange={e => this.updateInputConditionValue(e)}/>
        <input className="input" type="text"  name="allowpets" value={this.state.inputAllowpets} onChange={e => this.updateInputAllowpetsValue(e)}/>
        <input className="input" type="text"  name="postalcode" value={this.state.inputPostalCode} onChange={e => this.updateInputPostValue(e)}/>
        <div>
        <button className = "button" type="submit" onClick={this.updateState} value="Submit" > Submit </button>
        </div>
        </div>
        <div className="App-content">
        <h4 className="App-intro">{this.state.location}</h4>
        <h4 className="App-intro">{this.state.data}</h4>
        <div className="maps">
        <h4>Average Statistics</h4>
        <img src={this.state.img1} alt="" />
        <img src={this.state.img2} alt="" />
        <img src={this.state.img3} alt="" style={{left: '100px',top: '1300px',position: 'absolute'}}/>
        <img src={legend} alt="" style={{right: '150px',top: '1200px',position: 'absolute'}} />
        <img src={this.state.img4} alt="" className="img"/>
        </div>
        </div>
      </div>
    );
  }
}

export default App;
