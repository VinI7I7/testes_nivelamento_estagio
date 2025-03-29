import axios from 'axios';

export default {
  async search(query) {
    const response = await axios.get(`http://localhost:5000/api/search?q=${query}`);
    return response.data.results;
  }
};

