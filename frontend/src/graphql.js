const GRAPHQL_URL = '/graphql/';

const apiClient = (query) => {
  let csrftoken;
  const cookies = ('; ' + document.cookie).split('; csrftoken=');
  if (cookies.length === 2) {
    csrftoken = cookies.pop().split(';').shift();
  }

  return fetch(GRAPHQL_URL, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ query }),
    credentials: 'include'
  })
  .then(resp => resp.json());
}

export default apiClient;
