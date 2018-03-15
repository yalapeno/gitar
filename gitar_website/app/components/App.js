var React = require('react');
var axios = require('axios');

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {posts: []};

	this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    axios.get('http://www.reddit.com/r/cyberpunk.json')
      .then(res => {
        const posts = res.data.data.children.map(obj => obj.data);
        this.setState({ posts });
      });
  }

  componentDidMount() {
    // do nothing.
  }

  render() {
    return (
      <ul>
	<button onClick={this.handleClick}>Click me!</button><p></p>

        <h1>{`/r/cyberpunk`}</h1>
        <ul>
          {this.state.posts.map(post =>
            <li key={post.id}>{post.title}</li>
          )}
        </ul>
      </ul>
    )
  }

}


module.exports = App
