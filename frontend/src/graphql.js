import ApolloClient from 'apollo-boost';

const getCsrfToken = () => {
  let csrftoken = '';
  const cookies = ('; ' + document.cookie).split('; csrftoken=');
  if (cookies.length === 2) {
    csrftoken = cookies.pop().split(';').shift();
  }
  return csrftoken;
};

const apiClient = new ApolloClient({
  uri: '/graphql/',
  credentials: 'include',
  headers: {
    'X-CSRFToken': getCsrfToken()
  }
});

export default apiClient;
