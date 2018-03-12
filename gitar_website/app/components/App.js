var React = require('react');
var axios = require('axios');

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {persons: []};
  }

  handleClick() {
    // TODO Implement this. Also make space for button
  }

  componentDidMount() {
    axios.get(`https://jsonplaceholder.typicode.com/users`)
      .then(res => {
        const persons = res.data;
        this.setState({ persons });
      })
  }

  render() {
    return (
      <ul>

	<button></button>

        { this.state.persons.map(person => <li>{person.name}</li>)}
      </ul>
    )
  }

}


module.exports = App
