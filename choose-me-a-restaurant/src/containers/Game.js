/*
Uses the connect utility from react-redux to pass state.messages 
to the message props of the App component
*/

import {connect} from 'react-redux';
import App from '../App';

const mapStateToProps = state => ({
    message: state.message,
});

const Game = connect(
    mapStateToProps,
)(App);

export default Game;
