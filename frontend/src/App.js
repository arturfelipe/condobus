import React, { Component } from 'react';
import gql from 'graphql-tag';
import apiClient from './graphql';

import './App.css';


class App extends Component {
  state = { organizations: [] }

  componentDidMount() {
    const query = gql`
      {
        organizations {
          name
          logo
        }
      }
    `
    apiClient
      .query({ query })
      .then(result => {
        const { organizations } = result.data;
        this.setState({ organizations })
      });
  }

  render() {
    const { organizations } = this.state;
    return (
      <div className='App'>
        {organizations.map(org => {
          return (
            <div key={`organization-${org.id}`}>
              {org.name}
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;
