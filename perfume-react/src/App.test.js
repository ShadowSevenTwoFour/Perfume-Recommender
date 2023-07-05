import React, { useState } from 'react';

function App() {
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const query = 'citrus'; // Replace with user input if desired

    const response = await fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });

    const data = await response.json();
    const mostSimilarCluster = data.most_similar_cluster;
    setResult(`Most similar cluster: ${mostSimilarCluster}`);
  };

  return (
    <div>
      <h1>ML Perfume Recommender</h1>
      <form onSubmit={handleSubmit}>
        <button type="submit">Predict</button>
      </form>
      <p>{result}</p>
    </div>
  );
}

export default App;
