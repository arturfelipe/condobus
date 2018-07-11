import React, { Component } from 'react';
import './App.css';

import apiClient from "./graphql";

class App extends Component {
  state = { timeSheets: [] }

  componentDidMount() {
    const query = '{ timeSheets { version } }'
    apiClient(query)
      .then(({ data }) => {
        this.setState({ timeSheets: data.timeSheets })
      });
  }

  render() {
    const { timeSheets } = this.state.timeSheets;
    return (
      <div className="App">
        {timeSheets && timeSheets.map(sheet => {
          return <div>{sheet.name}</div>
        })}
      </div>
    );
  }
}

export default App;
