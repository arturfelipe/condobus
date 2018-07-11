import React, { Component } from 'react';
import { ApolloProvider, Query } from "react-apollo";
import gql from 'graphql-tag';
import apiClient from './graphql';

import './App.css';

const Organizations = () => (
  <Query
    query={gql`
      {
        organizations {
          name
          logo
        }
      }`
  }>
    {({ data, error }) => {
      return data.organizations ? data.organizations.map(org => (
        <div key={`org-${org.name}`}>{org.name}</div>
      )) : null
    }}
  </Query>
);


class App extends Component {
  render() {
    return (
      <ApolloProvider client={apiClient}>
        <div className='App'>
          <Organizations />
        </div>
      </ApolloProvider>
    );
  }
}

export default App;
